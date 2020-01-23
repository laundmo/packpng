# for running production WSGI server
from app.app_factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run()