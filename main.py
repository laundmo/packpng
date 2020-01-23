import json
from pathlib import Path
import os
import requests
from flask import Flask, render_template
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
try:
    if os.environ["PRODUCTION"] == "True":
        production = True
    else:
        production = False
except KeyError:
    production = False

if production:
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["30 per minute", "1 per second"]
    )
else:
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["100 per second"]
    )

if production:
    cache = Cache(config={'CACHE_TYPE': 'uwsgi', 'CACHE_UWSGI_NAME':'packpng@localhost:3031'})
else:
    cache = Cache(config={'CACHE_TYPE': 'null'})

limiter.init_app(app)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=120)
def index():
    with open('./data/seeds.json', encoding="utf8") as seeds_json:
        with open('./data/what_we_know.json', encoding="utf8") as wwk_json:
            seeds = json.load(seeds_json)
            what_we_know = json.load(wwk_json)
            return render_template('index.html', seeds=seeds, what_we_know=what_we_know)


@app.route('/faq/')
@cache.cached(timeout=120)
def faq():
    with open('./data/faq.json', encoding="utf8") as faq_json:
        faq = json.load(faq_json)
        return render_template('faq.html', faq=faq)

@app.route('/contributors/')
@cache.cached(timeout=120)
def contributors():
    with open('./data/contributors_no_edit.json', encoding="utf8") as contrib_json:
        contributors = json.load(contrib_json)
        return render_template('contributors.html', contributors=contributors)

@app.route('/google_doc/')
@cache.cached(timeout=120)
def google_doc():
    return render_template('google_doc.html')

@app.route('/timeline/')
@cache.cached(timeout=120)
def timeline():
    return render_template('timeline.html')

@app.route('/gallery/')
@cache.cached(timeout=120)
def gallery():
    with open('./data/image_captions.json', encoding="utf8") as images_json:
        images = json.load(images_json)
        return render_template('gallery.html', images=images)

@app.route('/about/')
@limiter.limit("50 per hour; 1 per 2 seconds")
@cache.cached(timeout=120)
def about():
    contributors = requests.get("https://api.github.com/repos/laundmo/packpng/stats/contributors").json()
    contributors = sorted(contributors, key=lambda x: x['total'], reverse=True)
    for contrib in contributors:
        added = sum([w['a'] for w in contrib['weeks']])
        deleted = sum([w['d'] for w in contrib['weeks']])
        contrib["added"] = added
        contrib["deleted"] = deleted
    return render_template('about.html', contributors=contributors)

# example route config
#
# @app.route('/mypage/')
# @limiter.limit("50 per 2 hour; 1 per 8 seconds")
# @cache.cached(timeout=50)
# def mypage():
#     a = 1 + 1
#     return render_template('mypage.html', a=a)


if __name__ == '__main__':
    extra_files = [str(p.resolve()) for p in Path('./').glob('**/*')] # list of all files in the project, so flask knows where to look for changes
    app.run('0.0.0.0', extra_files=extra_files, debug=True)
