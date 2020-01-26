from flask import Blueprint, render_template, request
from .extensions import limiter, cache
import requests
import json
import subprocess
import hmac
import hashlib
import os

redeploy_blueprint = Blueprint("redeploy", __name__)

@redeploy_blueprint.route('/redeploy', methods = ['POST'])
def redeploy():
    signature = request.headers.get('X-Hub-Signature') # get signature
    data = request.data # get request data
    if verify_hmac_hash(data, signature):
        if request.headers.get('X-GitHub-Event') == "ping":
            return "OK" # github will error without a ping
        elif request.headers.get('X-GitHub-Event') == "push":
            payload = request.get_json() # get the json
            if "deploy" in payload['ref']: # only react to refs with "deploy" in the name
                subprocess.Popen("./pull_restart.sh", shell=True, executable='/bin/bash') # start a subprocess for the bash script to restart the page
                return "started" # return sucess, github only cares about status 200
            return "wrong branch" #a push to the wrong branch should not show up as error in github, return status 200
        else:
            return ("wrong event type", 401) # github should only send ping and push. anythign else is a error
    else:
        return ("could not verify signature", 401) # not gonna allow wrong signatures lul

def verify_hmac_hash(data, signature):
    """ verify the hash against the data"""
    github_secret = bytes(os.environ['GITHUB_SECRET'], 'UTF-8')
    mac = hmac.new(github_secret, msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest('sha1=' + mac.hexdigest(), signature)