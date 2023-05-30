from applications.extensions import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)  # 用户名
    password = db.Column(db.String(300), nullable=False)  # 密码
    user_email = db.Column(db.String(100), nullable=False)  # 用户邮箱
    user_phone = db.Column(db.String(100), nullable=False)  # 用户电话
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
