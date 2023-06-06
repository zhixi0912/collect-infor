from applications.api_1_0 import api
from flask import jsonify, request
from applications.models.employee import EmployeeModel
from applications.extensions import db
from applications.utils.commons import login_required


@api.get("/employee")
@login_required
def get_employee_info():
    """
    @api {GET} /employee 获取员工信息
    @apiVersion 0.1.0
    @apiName get_employee_info
    @apiGroup Employee
    @apiDescription 获取员工所有信息
    @apiSuccessExample Response-Success:
        HTTP 1.1/ 200K
        {
            'status': 0,
            'msg': 'success',
            'data': [
                }
                  "create_time": "Thu, 24 Nov 2022 17:32:02 GMT",
                  "employee_address": "上海市黄浦区南京路219弄1号东方小区2栋1201室",
                  "employee_bank": "中国人民银行",
                  "employee_bank_card": "62002131321232342323",
                  "employee_birthday": "1989-03-02",
                  "employee_content": "平平无奇",
                  "employee_gend": "男",
                  "employee_id_card": "1211321999091232397",
                  "employee_name": "李四",
                  "employee_nation": "回",
                  "employee_occupation": "木工",
                  "employee_phone": "18877776666",
                  "employee_post": "1队队长"
                }
            ]
        }
    @apiErrorExample Response-Fail:
        HTTP 1.1/ 404K
        {
            'status': 1,
            'msg': 'Fail',
            'data': null
        }
    """
    result = {
        "code": "200",
        "msg": "信息查询成功!",
        "data": None
    }
    employee_info = EmployeeModel.query.order_by(EmployeeModel.create_time.desc()).all()
    employee_info_list = []
    for item in employee_info:
        employee_info_list.append(item.to_dict())
    result['data'] = employee_info_list
    return jsonify(result)


@api.post("/employee")
@login_required
def add_employee():
    """
        @api {POST} /employee 新增员工信息
        @apiVersion 0.1.0
        @apiName add_employee
        @apiGroup Employee
        @apiDescription 新增员工所有信息
        @apiParam {String} employee_name 员工姓名(必填)
        @apiParam {String} [employee_gend] 员工性别(必填)
        @apiParam {String} [employee_nation] 员工民族(必填)
        @apiParam {String} [employee_phone] 员工电话(必填)
        @apiParam {String} [employee_birthday] 员工生日(必填)
        @apiParam {String} [employee_id_card] 员工身份证号码(必填)
        @apiParam {String} [employee_bank_card] 银行卡号码(必填)
        @apiParam {String} [employee_bank] 所属银行(必填)
        @apiParam {String} [employee_address] 地址(必填)
        @apiParam {String} [employee_occupation] 职业(必填)
        @apiParam {String} [employee_post] 职务(必填)
        @apiParam {String} [employee_content] 其他(必填)
        @apiSuccessExample Response-Success:
            HTTP 1.1/ 200K
            {
                'status': 0,
                'msg': 'success'
            }
        @apiErrorExample Response-Fail:
            HTTP 1.1/ 404K
            {
                'status': 1,
                'msg': 'Fail'
            }
    """
    result = {}
    employee_data = request.json
    employee_info = EmployeeModel(
        employee_name=employee_data['employee_name'],  # 名称
        employee_gend=employee_data['employee_gend'],  # 性别
        employee_nation=employee_data['employee_nation'],  # 民族
        employee_phone=employee_data['employee_phone'],  # 电话
        employee_birthday = employee_data['employee_birthday'],  # 生日
        employee_id_card = employee_data['employee_id_card'],  # 身份证号码
        employee_bank_card = employee_data['employee_bank_card'],  # 银行卡号码
        employee_bank = employee_data['employee_bank'],  # 所属银行
        employee_address = employee_data['employee_address'],  # 地址
        employee_occupation = employee_data['employee_occupation'],  # 职业
        employee_post = employee_data['employee_post'],  # 职务
        employee_content = employee_data['employee_content']    # 其他
    )
    db.session.add(employee_info)
    db.session.commit()
    result['code'] = '200'
    result['msg'] = '信息插入成功！'
    result['data'] = None
    # print(employee_info)
    return jsonify(result)


@api.put("/employee")
@login_required
def edit_employee():
    """
        @api {PUT} /employee 修改员工信息
        @apiVersion 0.1.0
        @apiName edit_employee
        @apiGroup Employee
        @apiDescription 修改员工所有信息
        @apiParam {String} employee_name 员工姓名(必填)
        @apiParam {String} [employee_gend] 员工性别(必填)
        @apiParam {String} [employee_nation] 员工民族(必填)
        @apiParam {String} [employee_phone] 员工电话(必填)
        @apiParam {String} [employee_birthday] 员工生日(必填)
        @apiParam {String} [employee_id_card] 员工身份证号码(必填)
        @apiParam {String} [employee_bank_card] 银行卡号码(必填)
        @apiParam {String} [employee_bank] 所属银行(必填)
        @apiParam {String} [employee_address] 地址(必填)
        @apiParam {String} [employee_occupation] 职业(必填)
        @apiParam {String} [employee_post] 职务(必填)
        @apiParam {String} [employee_content] 其他(必填)
        @apiSuccessExample Response-Success:
            HTTP 1.1/ 200K
            {
                'status': 0,
                'msg': 'success'
            }
        @apiErrorExample Response-Fail:
            HTTP 1.1/ 404K
            {
                'status': 1,
                'msg': 'Fail'
            }
    """
    result = {}
    result['code'] = '200'
    result['data'] = None
    employee_data = request.json
    id = int(employee_data['employee_id'])
    employee_data.pop('employee_id')
    employee_data.pop('create_time')
    updateEmp = EmployeeModel.query.filter(id == EmployeeModel.id).update(employee_data)
    if updateEmp:
        db.session.commit()
        result['msg'] = '信息修改成功！'
    else:
        result['msg'] = '信息修改失败！'
    # print(employee_info)
    return jsonify(result)


@api.delete("/employee")
@login_required
def delete_employee():
    """
        @api {DELETE} /employee 删除员工信息
        @apiVersion 0.1.0
        @apiName delete_employee
        @apiGroup Employee
        @apiDescription 删除员工信息
        @apiParam {String} employee_id 员工id(必填)
        @apiSuccessExample Response-Success:
            HTTP 1.1/ 200K
            {
                'status': 0,
                'msg': 'success'
            }
        @apiErrorExample Response-Fail:
            HTTP 1.1/ 404K
            {
                'status': 1,
                'msg': 'Fail'
            }
    """
    result = {}
    result['code'] = '200'
    result['data'] = None
    employee_data = request.json
    id = int(employee_data['employee_id'])
    delEmployee = EmployeeModel.query.filter(EmployeeModel.id == id).delete()
    if delEmployee:
        db.session.commit()
        print('success')
        result['msg'] = '信息删除成功！'
    else:
        result['msg'] = '这个员工不存在！'
    # print(employee_info)
    return jsonify(result)




