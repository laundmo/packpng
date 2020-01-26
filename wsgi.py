# for running production WSGI server
from app.app_factory import create_app
import data.contributors_to_json
import app.static.generate_thumbnails

app = create_app()

if __name__ == "__main__":
    app.run()