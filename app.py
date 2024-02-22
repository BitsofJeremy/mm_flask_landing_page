"""landing_page app"""
# Import the app
from landing_page import app


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
    )
