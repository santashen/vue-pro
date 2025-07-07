from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)

    # 创建数据库
    with app.app_context():
        db.create_all()
    
    # 创建 API
    api = Api(app)
    
    # 注册蓝图和路由
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    # 注册 API 资源
    from app.resources import PersonInfoResource, PersonInfoListResource
    api.add_resource(PersonInfoListResource, '/api/persons')
    api.add_resource(PersonInfoResource, '/api/persons/<int:id>')
    
    return app 