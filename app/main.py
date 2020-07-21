from flask import Blueprint, render_template, request
from .extensions import limiter, cache
import requests
import json
from .misc import get_contributors_json

main_blueprint = Blueprint("main", __name__)

# example route config
#
# @main_blueprint.route('/mypage/')
# @limiter.limit("50 per 2 hour; 1 per 8 seconds")
# @cache.cached(timeout=50)
# def mypage():
#     a = 1 + 1
#     return render_template('mypage.html', a=a)


@main_blueprint.route('/')
@cache.cached(timeout=120)
def index():
    with open('./data/seeds.json', encoding="utf8") as seeds_json:
        with open('./data/what_we_know.json', encoding="utf8") as wwk_json:
            seeds = json.load(seeds_json)
            what_we_know = json.load(wwk_json)
            return render_template('index.html', seeds=seeds, what_we_know=what_we_know)


@main_blueprint.route('/faq/')
@main_blueprint.route('/FAQ/')
@cache.cached(timeout=120)
def faq():
    with open('./data/faq.json', encoding="utf8") as faq_json:
        faq = json.load(faq_json)
        return render_template('faq.html', faq=faq)

@main_blueprint.route('/contributors/')
@cache.cached(timeout=120)
def contributors():
    with open('./data/contributors.json', encoding="utf8") as contrib_json:
        contributors = json.load(contrib_json)
        return render_template('contributors.html', contributors=contributors)

@main_blueprint.route('/method/')
@cache.cached(timeout=120)
def method():
    return render_template('method.html')

@main_blueprint.route('/timeline/')
@cache.cached(timeout=120)
def timeline():
    return render_template('timeline.html')

@main_blueprint.route('/gallery/')
@cache.cached(timeout=120)
def gallery():
    with open('./data/image_captions.json', encoding="utf8") as images_json:
        images = json.load(images_json)
        return render_template('gallery.html', images=images)

@main_blueprint.route('/about/')
@limiter.limit("5 per minute; 1 per 10 seconds")
@cache.cached(timeout=120)
def about():
    contributors = get_contributors_json()
    return render_template('about.html', contributors=contributors)

@main_blueprint.route('/details/')
@cache.cached(timeout=120)
def details():
    with open('./data/pack_metadata.txt', encoding="utf8") as metadata_file:
        lines = metadata_file.readlines()
        lines = filter(lambda l: l[0] != "-", lines)
        lines = [[f.strip() for f in l.split(":", 1)] for l in lines]
        return render_template('details.html', metadata=lines)

@main_blueprint.route('/roadmap/')
@cache.cached(timeout=120)
def roadmap():
    return render_template('roadmap.html')

@main_blueprint.route('/panoramasearch/')
@cache.cached(timeout=120)
def panoramasearch():
    return render_template('panoramasearch.html')

