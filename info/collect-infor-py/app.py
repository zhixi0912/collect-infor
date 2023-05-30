from applications import create_app
from applications.extensions import db
from flask_migrate import Migrate

app = create_app("develop")
# app = create_app("product")    # 部署线上时打开
Migrate(app, db)


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')   # 部署线上时打开

# ORM模型映射成表
# flask db init
# flask db migrate
# flask db upgrade

# apidoc生成api文档
# apidoc -i 项目路径 -o 输出路径

# 生成依赖配置文件
# pip freeze > requirements.txt
# pip install -r requirements.txt
