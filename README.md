# packpng.com rewrite
[![Coverage Status](https://coveralls.io/repos/github/laundmo/packpng/badge.svg?branch=master&service=github)](https://coveralls.io/github/laundmo/packpng?branch=master) [![Build Status](https://travis-ci.com/laundmo/packpng.svg?branch=master)](https://travis-ci.com/laundmo/packpng)

because the original page was made in a website builder and thats just oof

![](https://i.vgy.me/KPsCYW.png)

## how to run

you need a recent python 3, i tested on 3.8.0

first install requirements `pip install -r requirements.txt`

run file `python main.py`

now you can access the page on localhost. the server will restart if it detects changes in existing files.

## directory structure

data/ - json files with data displayed on page, such as FAQ and tested seeds. i went with json for easy editing.

static/ - static files such as images or js/css. get url to static files in a template like this `{{ url_for('static', filename='pack.png') }}`

templates/ - jinja2 templates. layout.html is the base template, in which other content gets inserted using blocks.

## writing templates/pages.

you have to add a path to the page in main.py. the basic structure of this is
```python
@app.route("/mypage") # the path to the page
def mypage(): # function doesnt have to be the same name as route
    a = [1,2,3] # example variable
    return render_template("mypage.html", a=a) # render the template named "mypage.html" from the templates folder, and pass the value of "a" with the name "a" to the template
```
[related flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing)

then you have to add the page to the navbar, if it should appear there.
go to `templates/layout.html` and look at the top of the file. add a new element to the list like this `('/mypage', 'mypage', 'My Page'),`, where the first string is the route, the second is the ID, and the third the displayed name.

make sure to set the correct active page in your template using `{% set active_page = "mypage" %}`. here we use the ID we defined before
