from applications.extensions import db
from datetime import datetime


# 员工信息
class EmployeeModel(db.Model):
    __tablename__ = "employee_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_name = db.Column(db.String(100), nullable=False)  # 名称
    employee_gend = db.Column(db.String(100), nullable=False)  # 性别
    employee_nation = db.Column(db.String(100), nullable=False)  # 民族
    employee_phone = db.Column(db.String(100), nullable=False)  # 电话
    employee_birthday = db.Column(db.String(100), nullable=False)   # 生日
    employee_id_card = db.Column(db.String(100), nullable=False)    # 身份证号码
    employee_bank_card = db.Column(db.String(100), nullable=False)  # 银行卡号码
    employee_bank = db.Column(db.String(100), nullable=False)   # 所属银行
    employee_address = db.Column(db.String(300), nullable=False)    # 地址
    employee_occupation = db.Column(db.String(100), nullable=False)  # 职业
    employee_post = db.Column(db.String(100), nullable=False)  # 职务
    employee_content = db.Column(db.Text, nullable=False)   # 其他
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间

    # 像模型字段处理成list
    def to_dict(self):
        return {
            "employee_id": self.id,  # 名称
            "employee_name": self.employee_name,     # 名称
            "employee_gend": self.employee_gend,  # 性别
            "employee_nation": self.employee_nation,  # 民族
            "employee_phone": self.employee_phone,  # 电话
            "employee_birthday": self.employee_birthday,  # 生日
            "employee_id_card": self.employee_id_card,  # 身份证号码
            "employee_bank_card": self.employee_bank_card,  # 银行卡号码
            "employee_bank": self.employee_bank,  # 所属银行
            "employee_address": self.employee_address,  # 地址
            "employee_occupation": self.employee_occupation,  # 职业
            "employee_post": self.employee_post,  # 职务
            "employee_content": self.employee_content,  # 其他
            "create_time": self.create_time  # 创建时间
        }

# 考勤
# class AttendanceModel(db.Model):
#     __tablename__ = "attendance"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     attendance_days = db.Column(db.DateTime, default=datetime.now)  # 出勤天数
#     create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
#     attendance_id = db.Column(db.Integer, db.ForeignKey("employee_info.id"))
#     employee_id_card = db.relationship(EmployeeModel, backref=db.backref("attendance", order_by=create_time.desc()))  # 员工身份证号
#     employee_name = db.relationship(EmployeeModel, backref=db.backref("attendance", order_by=create_time.desc()))  # 员工姓名
#
# # 工资
# class WagesModel(db.Model):
#     __tablename__ = "wages"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     provide_time = db.Column(db.String(100), nullable=False)   # 生日
#     create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
#     payable = db.Column(db.DateTime, default=datetime.now)  # 应付工资
#     actual_paid = db.Column(db.DateTime, default=datetime.now)  # 实付工资
#     attendance_id = db.Column(db.Integer, db.ForeignKey("employee_info.id"))
#     employee_id_card = db.relationship(EmployeeModel, backref=db.backref("wages", order_by=create_time.desc()))  # 员工身份证号
#     attendance_days = db.relationship(AttendanceModel, backref=db.backref("wages", order_by=create_time.desc()))  # 出勤天数
#     employee_name = db.relationship(EmployeeModel, backref=db.backref("wages", order_by=create_time.desc()))  # 员工姓名
#     employee_bank_card = db.relationship(EmployeeModel, backref=db.backref("wages", order_by=create_time.desc()))  # 银行卡号