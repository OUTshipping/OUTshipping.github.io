// GitHub API 工具模块
// 用于后台管理页面通过 GitHub REST API 操作仓库文件

const REPO_API = 'https://api.github.com/repos/OUTshipping/OUTshipping.github.io'
const BRANCH = 'source'
const MAIN_BRANCH = 'main'

/**
 * 构建请求头
 * @param {string} token - GitHub Personal Access Token
 * @returns {object} 请求头对象
 */
function getHeaders(token) {
  return {
    'Authorization': `Bearer ${token}`,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
  }
}

/**
 * 验证 Token 是否有效，并检查对仓库的写入权限
 * @param {string} token - GitHub PAT
 * @returns {Promise<{valid: boolean, message: string}>}
 */
export async function validateToken(token) {
  try {
    const res = await fetch(`${REPO_API}`, {
      headers: getHeaders(token)
    })
    if (!res.ok) {
      return { valid: false, message: '无效的 Token 或无权访问此仓库' }
    }
    const data = await res.json()
    // 检查是否有 push 权限
    if (!data.permissions || !data.permissions.push) {
      return { valid: false, message: 'Token 没有对此仓库的写入权限' }
    }
    return { valid: true, message: '验证成功' }
  } catch (err) {
    return { valid: false, message: `网络错误: ${err.message}` }
  }
}

/**
 * 获取仓库中指定文件的内容和 SHA
 * @param {string} token - GitHub PAT
 * @param {string} path - 文件路径（相对仓库根目录）
 * @returns {Promise<{content: string, sha: string}>}
 */
export async function getFileContent(token, path) {
  const res = await fetch(`${REPO_API}/contents/${path}?ref=${BRANCH}`, {
    headers: getHeaders(token)
  })
  if (!res.ok) {
    throw new Error(`获取文件失败: ${res.status} ${res.statusText}`)
  }
  const data = await res.json()
  // GitHub API 返回 Base64 编码的内容
  const content = decodeURIComponent(escape(atob(data.content.replace(/\n/g, ''))))
  return { content, sha: data.sha }
}

/**
 * 更新仓库中已有文件
 * @param {string} token - GitHub PAT
 * @param {string} path - 文件路径
 * @param {string} content - 新的文件内容（纯文本）
 * @param {string} sha - 文件当前的 SHA 值
 * @param {string} message - commit 消息
 * @returns {Promise<object>} GitHub API 响应
 */
export async function updateFile(token, path, content, sha, message) {
  const res = await fetch(`${REPO_API}/contents/${path}`, {
    method: 'PUT',
    headers: getHeaders(token),
    body: JSON.stringify({
      message,
      content: btoa(unescape(encodeURIComponent(content))),
      sha,
      branch: BRANCH
    })
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(`更新文件失败: ${err.message}`)
  }
  return await res.json()
}

/**
 * 在仓库中创建新文件
 * @param {string} token - GitHub PAT
 * @param {string} path - 文件路径
 * @param {string} content - 文件内容（纯文本）
 * @param {string} message - commit 消息
 * @returns {Promise<object>} GitHub API 响应
 */
export async function createFile(token, path, content, message) {
  const res = await fetch(`${REPO_API}/contents/${path}`, {
    method: 'PUT',
    headers: getHeaders(token),
    body: JSON.stringify({
      message,
      content: btoa(unescape(encodeURIComponent(content))),
      branch: BRANCH
    })
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(`创建文件失败: ${err.message}`)
  }
  return await res.json()
}

/**
 * 上传图片文件（Base64 编码）
 * @param {string} token - GitHub PAT
 * @param {string} path - 图片存储路径
 * @param {string} base64Content - 图片的 Base64 编码内容（不含 data:image 前缀）
 * @param {string} message - commit 消息
 * @returns {Promise<object>} GitHub API 响应
 */
export async function uploadImage(token, path, base64Content, message) {
  const res = await fetch(`${REPO_API}/contents/${path}`, {
    method: 'PUT',
    headers: getHeaders(token),
    body: JSON.stringify({
      message,
      content: base64Content,
      branch: BRANCH
    })
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(`上传图片失败: ${err.message}`)
  }
  return await res.json()
}

/**
 * 删除仓库中的文件
 * @param {string} token - GitHub PAT
 * @param {string} path - 文件路径
 * @param {string} sha - 文件当前的 SHA 值
 * @param {string} message - commit 消息
 * @returns {Promise<object>} GitHub API 响应
 */
export async function deleteFile(token, path, sha, message) {
  const res = await fetch(`${REPO_API}/contents/${path}`, {
    method: 'DELETE',
    headers: getHeaders(token),
    body: JSON.stringify({
      message,
      sha,
      branch: BRANCH
    })
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(`删除文件失败: ${err.message}`)
  }
  return await res.json()
}

/**
 * 将 source 分支的 vehicles.json 部署到 main 分支
 * 直接通过 GitHub API 跨分支同步数据文件，无需本地构建
 * @param {string} token - GitHub PAT
 * @returns {Promise<object>} GitHub API 响应
 */
export async function deployToMain(token) {
  // 1. 读取 source 分支上的 vehicles.json 原始 Base64 内容
  const sourceRes = await fetch(`${REPO_API}/contents/public/data/vehicles.json?ref=${BRANCH}`, {
    headers: getHeaders(token)
  })
  if (!sourceRes.ok) {
    throw new Error(`读取 source 分支数据失败: ${sourceRes.status} ${sourceRes.statusText}`)
  }
  const sourceData = await sourceRes.json()
  const base64Content = sourceData.content.replace(/\n/g, '')

  // 2. 获取 main 分支上 data/vehicles.json 的当前 SHA
  const mainRes = await fetch(`${REPO_API}/contents/data/vehicles.json?ref=${MAIN_BRANCH}`, {
    headers: getHeaders(token)
  })
  if (!mainRes.ok) {
    throw new Error(`读取 main 分支数据失败: ${mainRes.status} ${mainRes.statusText}`)
  }
  const mainData = await mainRes.json()
  const mainSha = mainData.sha

  // 3. 将 source 的内容写入 main 分支
  const updateRes = await fetch(`${REPO_API}/contents/data/vehicles.json`, {
    method: 'PUT',
    headers: getHeaders(token),
    body: JSON.stringify({
      message: 'deploy: sync vehicles data to live site',
      content: base64Content,
      sha: mainSha,
      branch: MAIN_BRANCH
    })
  })
  if (!updateRes.ok) {
    const err = await updateRes.json()
    throw new Error(`部署到 main 失败: ${err.message}`)
  }
  return await updateRes.json()
}
