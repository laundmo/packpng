from app.app_factory import create_app
from pathlib import Path

if __name__ == '__main__':
    extra_files = [str(p.resolve()) for p in Path('./').glob('**/*')] # list of all files in the project, so flask knows where to look for changes
    create_app().run(extra_files=extra_files, debug=True)
