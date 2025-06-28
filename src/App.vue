<template>
  <div class="container">
    <h1>🧸 小玩具项目</h1>
    <div class="card-list">
      <div class="card" v-for="project in projects" :key="project.name">
        <h3>{{ project.name }}</h3>
        <p>{{ project.desc }}</p>
        <a :href="project.link" target="_blank">访问项目</a>
      </div>
    </div>
  </div>
</template>

<script setup>
const projects = [
  { name: "Flask Hello", desc: "最小可运行 Flask 页面", link: "http://windsong.top/hello/" },
  { name: "Todo 工具", desc: "任务清单 Web 应用", link: "http://windsong.top/todo/" }
]
</script>

<style>
body {
  font-family: sans-serif;
}
.container {
  padding: 2rem;
}
.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}
.card {
  border: 1px solid #ccc;
  border-radius: 12px;
  padding: 1rem;
  background: #f9f9f9;
}
.card a {
  color: #3498db;
  text-decoration: none;
}
</style>
