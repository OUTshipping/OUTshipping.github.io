<template>
  <div class="login-container">
    <div class="login-card">
      <h1>TG Automobile Admin</h1>
      <p class="login-desc">Enter your GitHub Personal Access Token to manage vehicles.</p>
      <div class="login-form">
        <input
          v-model="tokenInput"
          type="password"
          placeholder="GitHub Personal Access Token"
          @keyup.enter="handleLogin"
        />
        <button @click="handleLogin" :disabled="loginLoading">
          {{ loginLoading ? 'Verifying...' : 'Login' }}
        </button>
        <p v-if="loginError" class="error-msg">{{ loginError }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { validateToken } from '@/utils/github.js'

const emit = defineEmits(['login-success'])

const tokenInput = ref('')
const loginLoading = ref(false)
const loginError = ref('')

async function handleLogin() {
  loginLoading.value = true
  loginError.value = ''
  try {
    const result = await validateToken(tokenInput.value)
    if (result.valid) {
      emit('login-success', tokenInput.value)
    } else {
      loginError.value = result.message
    }
  } catch (err) {
    loginError.value = err.message
  } finally {
    loginLoading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, var(--primary-color), var(--dark-color));
}

.login-card {
  background: #fff;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow-lg);
  width: 420px;
  max-width: 90vw;
  text-align: center;
}

.login-card h1 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
  font-size: 1.75rem;
  font-weight: 700;
}

.login-desc {
  color: #64748b;
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
}

.login-form input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.75rem;
  font-size: 0.875rem;
  box-sizing: border-box;
  margin-bottom: 1rem;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
}

.login-form input:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.login-form button {
  width: 100%;
  padding: 0.75rem;
  background: var(--accent-color);
  color: #fff;
  border: none;
  border-radius: 9999px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 44px;
}

.login-form button:hover {
  background: var(--accent-color-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow);
}

.login-form button:disabled {
  background: #94a3b8;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.error-msg {
  color: #ef4444;
  margin-top: 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
}

@media (max-width: 480px) {
  .login-card {
    padding: 1.5rem;
  }

  .login-card h1 {
    font-size: 1.35rem;
  }
}
</style>

