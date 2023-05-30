# collect-infor-py

#### 介绍
**以下是 collect-infor-py 平台说明简介**  
    这是一个对员工信息采集的项目  
    主要分为3个模块  
1，微信小程序，可以在手机访问，使用手机相机扫描身份证和银行卡，进行员工信息采集  
2，PC后台管理，通过后台模型对员工数据进行审核，修改，更新、删除，导出等操作  
3，服务端，对微信小程序和PC后台管理提供服务支持  


#### 软件架构
软件架构说明

微信小程序端：  
技术栈：uni-app vue2  
https://gitee.com/zhixi0912/collect-infor-uniapp

PC后台管理：  
技术栈：vite + vue3 + typescript + pinia + axios + element-plus  
https://gitee.com/zhixi0912/collect-infor-admin

服务端：  
技术栈：python3.9.6 + flask + mysql  
https://gitee.com/zhixi0912/collect-infor-py

#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

    /**
     * @api {post} /api-security/get-token 获取TOKEN
     * @apiVersion 1.0.0
     * @apiName getToken
     * @apiGroup 安全校验类
     *
     * @apiParam {string} aes 来源
     * @apiParam {string} key 签名
     *
     * @apiSuccess {string} error 状态码1.成功、0.失败
     * @apiSuccess {string} code 错误码码10000.Successful、10005.非法请求、10007.参数错误、2001.验证码过期、2002.验证码错误，2003.尚未生成验证码
     * @apiSuccess {string} msg 返回详情
     * @apiSuccess {array[]} result 结果集
     *
     * @apiSuccessExample Success-Response:
     * HTTP/1.1 10000 OK
     * {
     * 　　"error":1,
     * 　　"code":"10000",
     * 　　"msg":"成功创建新TOKEN",
     * 　　"result":{
     * 　　　　"token":"2cea24050cfe8bc37f55fc03487cb9a5"
     * 　　}
     * }
     */

注解	含义
@apiVersion	接口版本
@apiDescription	接口具体说明
@apiGroup	接口所属分组
@apiParam	入参
@apiParamExample	入参样例
@apiSuccess	出参
@apiSuccessExample	返回成功样例
@apiErrorExample	


#### 参考文献

1.  https://docs.pythontab.com/flask/flask0.10/index.html
2.  https://element.eleme.cn/2.0/#/zh-CN
3.  https://cn.vuejs.org/api/
4.  https://uniapp.dcloud.net.cn/
5.  https://mp.weixin.qq.com/cgi-bin/wx
