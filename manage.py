import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import api
from api.init import api, db


api.config.from_object(
    os.environ['APP_SETTINGS']
)

migrate = Migrate(api, db)
manager = Manager(api)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
