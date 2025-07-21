<template>
  <div class="main-inner">
    <div class="about-container">
      <h1>关于小工具之家</h1>
      <div class="about-content">
        <div class="about-section">
          <h2>🎯 项目介绍</h2>
          <p>小工具之家是一个个人开发的工具集合网站，旨在提供实用的在线工具和应用程序。我们专注于创建简单、高效、易用的工具来解决日常生活和工作中的各种需求。</p>
        </div>
        
        <div class="about-section">
          <h2>🛠️ 技术栈</h2>
          <div class="tech-stack">
            <div class="tech-item">
              <strong>前端：</strong>Vue.js, HTML5, CSS3, JavaScript
            </div>
            <div class="tech-item">
              <strong>后端：</strong>Flask, Python
            </div>
            <div class="tech-item">
              <strong>地图服务：</strong>Leaflet.js
            </div>
            <div class="tech-item">
              <strong>数据处理：</strong>NumPy, SQLite
            </div>
            <div class="tech-item">
              <strong>部署：</strong>Nginx, Linux Server
            </div>
          </div>
        </div>

        <div class="about-section">
          <h2>🌟 特色功能</h2>
          <ul class="feature-list">
            <li>简洁直观的用户界面设计</li>
            <li>响应式布局，支持多端访问</li>
            <li>多样化的实用工具集合</li>
            <li>快速、稳定的服务体验</li>
            <li>持续更新和功能扩展</li>
          </ul>
        </div>

        <div class="about-section">
          <h2>📞 联系方式</h2>
          <p>如果你有任何问题、建议或合作意向，欢迎通过以下方式与我联系：</p>
          <div class="contact-info">
            <div class="contact-item">
              <strong>网站：</strong><a href="http://windsong.top" target="_blank">windsong.top</a>
            </div>
            <div class="contact-item">
              <strong>邮箱：</strong>联系方式请通过主站获取
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// About page logic here
</script>

<style scoped>
.main-inner {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

.about-container {
  background: white;
  border-radius: 12px;
  padding: 2.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.about-container h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 2rem;
  text-align: center;
  border-bottom: 3px solid #3498db;
  padding-bottom: 1rem;
}

.about-content {
  line-height: 1.7;
}

.about-section {
  margin-bottom: 2.5rem;
}

.about-section h2 {
  color: #34495e;
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.about-section p {
  color: #555;
  margin-bottom: 1rem;
}

.tech-stack {
  display: grid;
  gap: 0.8rem;
}

.tech-item {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  border-left: 4px solid #3498db;
}

.tech-item strong {
  color: #2c3e50;
}

.feature-list {
  list-style: none;
  padding: 0;
}

.feature-list li {
  background: #f8f9fa;
  padding: 0.8rem 1rem;
  margin-bottom: 0.5rem;
  border-radius: 6px;
  border-left: 3px solid #27ae60;
  color: #555;
}

.feature-list li:before {
  content: "✓";
  color: #27ae60;
  font-weight: bold;
  margin-right: 0.5rem;
}

.contact-info {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid #e9ecef;
}

.contact-item {
  margin-bottom: 0.8rem;
}

.contact-item:last-child {
  margin-bottom: 0;
}

.contact-item strong {
  color: #2c3e50;
}

.contact-item a {
  color: #3498db;
  text-decoration: none;
  transition: color 0.2s ease;
}

.contact-item a:hover {
  color: #2980b9;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .about-container {
    padding: 1.5rem;
    margin: 1rem;
  }
  
  .about-container h1 {
    font-size: 2rem;
  }
}
</style> 