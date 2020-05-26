from myapp import db,create_app

app = create_app()
# 数据迁移
import myapp.models
from flask_migrate import Migrate
migrate = Migrate(app,db)


if __name__ == '__main__':
    app.run(debug=True)