<template>
  <div class="vehicle-list">
    <div class="list-header">
      <span>Total: {{ vehicles.length }} vehicles</span>
      <button class="btn-refresh" @click="$emit('refresh')" :disabled="listLoading">
        {{ listLoading ? 'Loading...' : 'Refresh' }}
      </button>
    </div>
    <table class="vehicle-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Image</th>
          <th>Name</th>
          <th>Type</th>
          <th>Range</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="v in vehicles" :key="v.id">
          <td>{{ v.id }}</td>
          <td><img :src="v.coverImage" :alt="v.name" class="thumb" /></td>
          <td>{{ v.name }}</td>
          <td>{{ v.type }}</td>
          <td>{{ v.range }} km</td>
          <td>
            <label class="switch">
              <input type="checkbox" :checked="v.enabled" @change="$emit('toggle-enabled', v)" />
              <span class="slider"></span>
            </label>
          </td>
          <td class="actions-cell">
            <button class="btn-edit" @click="$emit('edit', v)">Edit</button>
            <button class="btn-delete" @click="$emit('delete', v)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
defineProps({
  vehicles: { type: Array, required: true },
  listLoading: { type: Boolean, default: false }
})

defineEmits(['refresh', 'edit', 'delete', 'toggle-enabled'])
</script>

<style scoped>
.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  color: #64748b;
  font-weight: 500;
}

.btn-refresh {
  background: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.5rem 1.25rem;
  border-radius: 9999px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 40px;
}

.btn-refresh:hover { background: var(--accent-color-dark); transform: translateY(-1px); }
.btn-refresh:disabled { background: #94a3b8; cursor: not-allowed; transform: none; }

.vehicle-list { overflow-x: auto; }

.vehicle-table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: var(--shadow);
  min-width: 700px;
}

.vehicle-table th {
  background: var(--primary-color);
  color: #fff;
  padding: 0.875rem 1rem;
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.vehicle-table td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #f1f5f9;
  font-size: 0.875rem;
  vertical-align: middle;
}

.vehicle-table tbody tr:hover { background: #f8fafc; }

.thumb {
  width: 64px;
  height: 42px;
  object-fit: cover;
  border-radius: 0.5rem;
}

.actions-cell {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.btn-edit {
  background: var(--accent-color);
  color: #fff;
  border: none;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 36px;
}
.btn-edit:hover { background: var(--accent-color-dark); }

.btn-delete {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.375rem 1rem;
  border-radius: 9999px;
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.2s;
  font-family: inherit;
  min-height: 36px;
}
.btn-delete:hover { background: #dc2626; }

/* Toggle Switch */
.switch { position: relative; display: inline-block; width: 44px; height: 24px; }
.switch input { opacity: 0; width: 0; height: 0; }
.slider {
  position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
  background-color: #cbd5e1; transition: 0.3s; border-radius: 24px;
}
.slider:before {
  position: absolute; content: ""; height: 18px; width: 18px; left: 3px; bottom: 3px;
  background-color: white; transition: 0.3s; border-radius: 50%;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
}
input:checked + .slider { background-color: #10b981; }
input:checked + .slider:before { transform: translateX(20px); }

@media (max-width: 768px) {
  .vehicle-table { min-width: unset; }
  .vehicle-table thead { display: none; }
  .vehicle-table tbody { display: flex; flex-direction: column; gap: 0.75rem; }
  .vehicle-table tr {
    display: flex; flex-wrap: wrap; background: #fff; border-radius: 0.75rem;
    box-shadow: var(--shadow-sm); padding: 1rem; border: 1px solid #f1f5f9; gap: 0.5rem;
  }
  .vehicle-table td {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0.375rem 0; border-bottom: none; font-size: 0.875rem; width: 100%;
  }
  .vehicle-table td::before {
    font-weight: 600; color: #64748b; font-size: 0.75rem;
    text-transform: uppercase; letter-spacing: 0.05em; min-width: 70px;
  }
  .vehicle-table td:nth-child(1)::before { content: 'ID'; }
  .vehicle-table td:nth-child(2)::before { content: 'Image'; }
  .vehicle-table td:nth-child(3)::before { content: 'Name'; }
  .vehicle-table td:nth-child(4)::before { content: 'Type'; }
  .vehicle-table td:nth-child(5)::before { content: 'Range'; }
  .vehicle-table td:nth-child(6)::before { content: 'Status'; }
  .vehicle-table td:nth-child(7)::before { content: 'Actions'; }
  .thumb { width: 80px; height: 52px; }
  .actions-cell {
    justify-content: flex-end; gap: 0.5rem;
    padding-top: 0.5rem !important; border-top: 1px solid #f1f5f9 !important;
  }
  .btn-edit, .btn-delete { min-height: 44px; padding: 0.5rem 1.25rem; font-size: 0.875rem; }
}
</style>

