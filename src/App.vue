<template>
  <div class="app-layout">
    <aside class="sidebar">
      <div class="sidebar-title">🌉 小工具之家</div>
      <ul class="sidebar-menu">
        <li 
          :class="{ active: $route.name === 'Home' }" 
          @click="$router.push('/')"
        >
          主页
        </li>
        <li 
          :class="{ active: $route.name === 'About' }" 
          @click="$router.push('/about')"
        >
          关于
        </li>
      </ul>
    </aside>
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
// App.vue logic here
</script>

<style>
body {
  font-family: sans-serif;
}
.app-layout {
  display: flex;
  min-height: 100vh;
}
.sidebar {
  width: 200px;
  background: #222;
  color: #fff;
  padding: 2rem 1rem 1rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.sidebar-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
}
.sidebar-menu {
  list-style: none;
  padding: 0;
  width: 100%;
}
.sidebar-menu li {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  margin-bottom: 0.5rem;
  background: none;
  color: #fff;
  transition: background 0.2s;
}
.sidebar-menu li.active, .sidebar-menu li:hover {
  background: #444;
}
.main-content {
  flex: 1;
  padding: 2rem;
  background: #f5f6fa;
}
</style>
