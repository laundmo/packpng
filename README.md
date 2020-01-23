# packpng.com rewrite
[![Coverage Status](https://coveralls.io/repos/github/laundmo/packpng/badge.svg?branch=master&service=github)](https://coveralls.io/github/laundmo/packpng?branch=master) [![Build Status](https://travis-ci.com/laundmo/packpng.svg?branch=master)](https://travis-ci.com/laundmo/packpng)

because the original page was made in a website builder and thats just oof

## how to run

you need a recent python 3, i tested on 3.8.0

first install requirements `pip install -r requirements.txt`

run file `python run.py`

now you can access the page on localhost. the server will restart if it detects changes in existing files.

## directory structure
```
packpng/
├───app/                    main code files
│   ├───static/             static files such as css, js, images
│   │   ├───gallery/        gallery images
│   │   └───thumbnails/     thumbnails for the gallery images
│   └───templates/          jinja2 templates
├───data/                   json and other data files, used for templates
└───tests/                  tests folder
```
## writing templates/pages.

you have to add a path to the page in app/main.py. the basic structure of this is
```python
@main_blueprint.route("/mypage") # the path to the page
def mypage(): # function doesnt have to be the same name as route
    a = [1,2,3] # example variable
    return render_template("mypage.html", a=a) # render the template named "mypage.html" from the templates folder, and pass the value of "a" with the name "a" to the template
```
[related flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing)

then you have to add the page to the navbar, if it should appear there.
go to `app/templates/layout.html` and look at the top of the file. add a new element to the list like this `('main_blueprint.mypage', 'mypage', 'My Page'),`, the first string is the name of the python function + blueprint, the second the arbitrary name used to set the active navbar page, and the last the display name.

make sure to set the correct active page in your template using `{% set active_page = "mypage" %}`. here we use the arbitrary name we defined before

link to pages with `{{ url_for('blueprint.function') }}` and to static files with `{{ url_for('static', filename='pack.png') }}`
