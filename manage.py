from app import manager, create_app
from config import config, GLOBALS

app = create_app(GLOBALS.ENV)
manager.run()
