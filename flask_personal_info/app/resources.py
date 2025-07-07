from flask_restful import Resource
from flask import request
from app import db
from app.models import PersonInfo
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import ValidationError

# 使用 SQLAlchemyAutoSchema 自动生成 Schema
class PersonInfoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonInfo
        sqla_session = db.session
        load_instance = True
        include_fk = True
    id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

person_schema = PersonInfoSchema()
persons_schema = PersonInfoSchema(many=True)

def resp(code=0, message='success', data=None):
    return {'code': code, 'message': message, 'data': data}, 200 if code == 0 else 400

class PersonInfoListResource(Resource):
    def get(self):
        """获取所有个人信息"""
        persons = PersonInfo.query.all()
        return resp(data={'persons': persons_schema.dump(persons)})
    
    def post(self):
        """创建新的个人信息"""
        json_data = request.get_json()
        if not json_data:
            return resp(code=1, message='请求体必须为JSON')
        try:
            person = person_schema.load(json_data)
        except ValidationError as err:
            return resp(code=1, message='参数校验失败', data=err.messages)
        db.session.add(person)
        db.session.commit()
        return resp(message='创建成功', data={'person': person_schema.dump(person)})

class PersonInfoResource(Resource):
    def get(self, id):
        """获取单个个人信息"""
        person = PersonInfo.query.get_or_404(id)
        return resp(data={'person': person_schema.dump(person)})
    
    def put(self, id):
        """更新个人信息"""
        person = PersonInfo.query.get_or_404(id)
        json_data = request.get_json()
        if not json_data:
            return resp(code=1, message='请求体必须为JSON')
        try:
            updated = person_schema.load(json_data, instance=person, partial=True)
        except ValidationError as err:
            return resp(code=1, message='参数校验失败', data=err.messages)
        db.session.commit()
        return resp(message='更新成功', data={'person': person_schema.dump(updated)})
    
    def delete(self, id):
        """删除个人信息"""
        person = PersonInfo.query.get_or_404(id)
        db.session.delete(person)
        db.session.commit()
        return resp(message='删除成功') 