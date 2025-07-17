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
  { name: "Flask Hello", desc: "最小可运行 Flask 页面", link: "http://windsong.top/toy/hello/", img: "https://flask.palletsprojects.com/en/stable/_images/flask-name.svg" },
  { name: "个人信息管理", desc: "Flask+Bootstrap 个人信息 CRUD 系统", link: "http://windsong.top/toy/personal/", img: "https://getbootstrap.com/docs/5.0/assets/brand/bootstrap-logo.svg" },
  { name: "我的旅行地图", desc: "基于 Leaflet.js 的互动旅行足迹地图，记录个人旅行回忆", link: "http://windsong.top/toy/travel/", img: "https://leafletjs.com/docs/images/logo.png" },
  { name: "水换热计算器", desc: "Flask + NumPy 开发的水加热功率计算器，支持多种流量单位", link: "http://windsong.top/toy/heat/", img: "https://www.thechemicalengineer.com/media/18707/976thumbpic.jpg" }
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
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
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
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-body h3 {
  margin: 0 0 0.8rem 0;
  color: #2c3e50;
  font-size: 1.3rem;
  font-weight: 600;
}

.card-body p {
  color: #7f8c8d;
  line-height: 1.5;
  margin: 0 0 1rem 0;
  flex-grow: 1;
}

.card a {
  color: #3498db;
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  transition: color 0.2s ease;
}

.card a:hover {
  color: #2980b9;
  text-decoration: underline;
}
</style>
