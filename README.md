###  collect-infor-admin

<p align="center">
    <img src="https://img.shields.io/badge/Vue-3.3.1-brightgreen.svg"/>
    <img src="https://img.shields.io/badge/Vite-4.3.5-green.svg"/>
    <img src="https://img.shields.io/badge/Element Plus-2.3.4-blue.svg"/>
    <img src="https://img.shields.io/badge/license-MIT-green.svg"/>
</p>


## 项目介绍

基于 Vue3 + Vite4+ TypeScript5 + Element-Plus + Pinia 等最新主流技术栈构建的前端项目。

项目有以下特性：

- 权限系统功能齐全，包括用户管理、角色管理、菜单管理、字典管理和部门管理等，以满足您对权限管理的需求。
- 项目还提供了基础设施支持，包括动态路由、按钮级别的权限控制、国际化支持、代码规范、Git 提交规范以及常用组件的封装，以便开发人员更高效地开发和维护项目。
## 项目预览




|     环境     | 名称版本    | 备注            |
| ----------- | :-------- | --------------|
| **开发工具**         | VSCode       | [下载地址](https://code.visualstudio.com/Download)                                                            |
| **运行环境**         | Node 16+                 |  [下载地址](http://nodejs.cn/download)   |
| **VSCode插件(必装)** | 1. `Vue Language Features (Volar) ` <br/> 2. `TypeScript Vue Plugin (Volar) `  <br/>3. 禁用 Vetur | ![image-20230224222541797](https://s2.loli.net/2023/02/24/Qt4XDGHFOWqfsyB.png) |


## 项目启动

```bash
# 克隆代码
git clone https://gitee.com/zhixi0912/collect-infor.git

# 进入前端根目录
cd collect-infor-admin

# 安装依赖
npm install

# 或使用npm淘宝源
npm install --registry=http://registry.npm.taobao.org

# 启动运行
npm run dev
```


## GIT提交规则

```
# 提交类型
[
	'build', // 改变构建流程、或者增加依赖库、工具等 如webpack.config.js,package.json yarn.lock
	'chore', // 构建过程或辅助工具的变动，各种配置文件的修改，如.gitignore,tsconfig.json,.vscode,.tenone, eslint/stylelint,envConfig
	'ci', // 对CI自动化流程配置文件或脚本进行了修改
	'docs', // 只修改了项目说明文档
	'feat', // 新增功能，一个新的特性
	'fix', // 修复一个Bug
	'perf', // 性能优化
	'refactor', // 代码重构，既不是修复Bug(fix)也不是添加功能(feat)
	'revert', // 版本回滚，代码回退
	'test', // 修改或添加一个测试用例
	'clean', // 清理过时无用文件
	'merge', // 合并代码分支
	'style', //  只修改了样式文件(包括css/less/sass,图片,字体文件)
	'format', // 格式化,不影响代码含义的修改，比如空格、格式缩进、缺失的分号等
]

# 例如
git add .
git commit -m "feat: add menu"
git push origin master
```

## 项目部署

```bash
# 项目打包
pnpm run build:prod

# 上传文件至远程服务器
将打包生成在 `dist` 目录下的文件拷贝至 `/usr/share/nginx/html` 目录

# nginx.cofig 配置
server {
	listen     80;
	server_name  localhost;
	location / {
			root /usr/share/nginx/html;
			index index.html index.htm;
	}
	# 反向代理配置
	location /prod-api/ {
			proxy_pass http://vapi.baidu.com/; # vapi.youlai.tech替换成你的后端API地址
	}
}
```




###  collect-infor-py

<p align="center">
    <img src="https://img.shields.io/badge/python-v3.9.6-green"/>
    <img src="https://img.shields.io/badge/Flask-v2.2.2-yellowgreen"/>
    <img src="https://img.shields.io/badge/redis-v4.3.4-orange"/>
    <img src="https://img.shields.io/badge/license-MIT-green.svg"/>
</p>


## 项目介绍

基于 Python3.9.6 + Flask2.2.2 + Mysql8 + Redis4.3.4 + SQLAlchemy1.4.44 等最新主流技术栈构建的后端项目。

项目有以下特性：