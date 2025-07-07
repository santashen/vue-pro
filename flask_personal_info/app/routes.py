from flask import Blueprint, render_template
from app.models import PersonInfo

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """主页"""
    return render_template('index.html')

@main_bp.route('/data')
def data():
    """数据页面"""
    persons = PersonInfo.query.all()
    return render_template('data.html', persons=persons) 