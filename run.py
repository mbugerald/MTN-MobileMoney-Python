# App / Lib imports
import os
from app import create_app
from app import Config

# Declare app
app = create_app(os.getenv('APP_ENV') or 'DEVELOPMENT')

#######################
#    For Dev only     #
#######################
# Grand execute access.
if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
