from applications.api_1_0 import api
from flask import jsonify, request, g
from applications.models.user import UserModel
from applications.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from applications.utils.response_code import RET, error_map
from applications.utils.commons import create_token


@api.route('/login', methods=['POST'])
def user_login():
    """
    @api {post} /login 用户登录
        @apiVersion 0.1.0
        @apiName user_login
        @apiGroup User
        @apiDescription 登录
        @apiParam {String} [username] 用户名(必填)
        @apiParam {String} [password] 密码(必填)
        @apiSuccessExample Response-Success:
            HTTP 1.1/ 200K
            {
                'status': 0,
                'msg': 'success',
                'data': {
                    'user_id': '001',
                    'username': 'admin',
                    'token': '000001',
                    'login_time': '2022-12-12',
                    'user_email': '***@qq.com',
                    'user_phone': '18899998888'

                }
            }
        @apiErrorExample Response-Fail:
            HTTP 1.1/ 404K
            {
                'status': 1,
                'msg': 'Fail'
            }
    :return:
    """
    result = {
        'code': '200',
        'data': None
    }
    user_data = request.get_json(silent=True)
    if not user_data:
        result['msg'] = '请输入用户名或密码！'
    else:
        user = UserModel.query.filter_by(username=user_data['username']).first()
        if user:
            if check_password_hash(user.password, user_data['password']):
                token = create_token(user.username, user.id)
                g.username = user.username
                g.user_id = user.id
                result['msg'] = '登录成功！'
                result['data'] = {
                    'user_id': user.id,
                    'user': user.username,
                    'user_email': user.user_email,
                    'token': token
                }
            else:
                result['msg'] = '密码错误！'
        else:
            result['msg'] = '没有这个用户！'
    # print('is ok')
    return jsonify(result)


@api.route("/login_out", methods=["DELETE"])
def login_out():
    """
    @api {delete} /login_out 用户登出
        @apiVersion 0.1.0
        @apiName login_out
        @apiGroup User
        @apiDescription 登出
        @apiSuccessExample Response-Success:
            HTTP 1.1/ 200K
            {
                'status': 0,
                'msg': 'success'
            }
    :return:
    """
    result = {
        'code': RET.OK,
        'msg': error_map.get(RET.OK)
    }
    g.username = None
    g.user_id = None
    # session.clear()
    return jsonify(result)


@api.route('/regiser', methods=['POST'])
def user_regiser():
    """
    @api {POST} /regiser 用户注册
        @apiVersion 0.1.0
        @apiName user_regiser
        @apiGroup User
        @apiDescription 注册
        @apiParam {String} [username] 用户名(必填)
        @apiParam {String} [password] 密码(必填)
        @apiParam {String} [user_email] 用户邮箱(必填)
        @apiParam {String} [user_phone] 用户电话(必填)
        @apiParam {String} [confirming] 确认密码(必填)
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
    :return:
    """
    result = {
        'code': '200'
    }
    user_data = request.json
    exists_user = UserModel.query.filter_by(username=user_data['username']).first()
    if user_data['password'] != user_data['confirming']:
        result['msg'] = '两次输入的密码不一致！'
    elif exists_user:
        result['msg'] = '该用户名已经存在'
    else:
        user_info = UserModel(
            username=user_data['username'],
            password=generate_password_hash(user_data['password']),
            user_email=user_data['user_email'],
            user_phone=user_data['user_phone'],
        )
        db.session.add(user_info)
        db.session.commit()
        result['msg'] = '用户注册成功！'
        print(result)
    result['data'] = None
    return jsonify(result)