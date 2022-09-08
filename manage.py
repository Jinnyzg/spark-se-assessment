from flask_script import Manager
from project.server import app
from flask_migrate import MigrateCommand


manager = Manager(app)

# Add the flask migrate
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()