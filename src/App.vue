<template>
  <div class="app-layout">
    <aside class="sidebar">
      <div class="sidebar-title">🧸 小玩具项目</div>
      <ul class="sidebar-menu">
        <li class="active">主页</li>
      </ul>
    </aside>
    <main class="main-content">
      <div class="main-inner">
        <div class="card-list">
          <div class="card" v-for="project in projects" :key="project.name">
            <img :src="project.img" class="card-img" alt="项目图片" />
            <div class="card-body">
              <h3>{{ project.name }}</h3>
              <p>{{ project.desc }}</p>
              <a :href="project.link" target="_blank">访问项目</a>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
const projects = [
  { name: "Flask Hello", desc: "最小可运行 Flask 页面", link: "http://windsong.top/hello/", img: "https://flask.palletsprojects.com/en/stable/_images/flask-name.svg" },
  { name: "个人信息管理", desc: "Flask+Bootstrap 个人信息 CRUD 系统", link: "http://windsong.top/personal/", img: "https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" }
]
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
.main-inner {
  width: 100%;
}
.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}
.card {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: box-shadow 0.2s;
}
.card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
.card-img {
  width: 100%;
  height: 140px;
  object-fit: cover;
  background: #eee;
}
.card-body {
  padding: 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.card a {
  color: #3498db;
  text-decoration: none;
  margin-top: 0.5rem;
  font-weight: bold;
}
</style>
