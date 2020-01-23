from flask import Blueprint, render_template, request
from .extensions import limiter, cache
import requests
import json
import subprocess
import hmac
import hashlib

redeploy_blueprint = Blueprint("redeploy", __name__)

@redeploy_blueprint.route('/redeploy', methods = ['POST'])
def redeploy():
    signature = request.headers.get('X-Hub-Signature')
    data = request.data
    if verify_hmac_hash(data, signature):
        if request.headers.get('X-GitHub-Event') == "ping":
            return "OK"
        elif request.headers.get('X-GitHub-Event') == "push":
            payload = request.get_json()
            if "deploy" in payload['ref']:
                subprocess.Popen("./pull_restart.sh", shell=True, executable='/bin/bash')
                return "started"
            return "wrong branch"
        else:
            return ("wrong event type", 401)
    else:
        return (f"could not verify signature", 401)

def verify_hmac_hash(data, signature):
    github_secret = bytes(os.environ['GITHUB_SECRET'], 'UTF-8')
    mac = hmac.new(github_secret, msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest('sha1=' + mac.hexdigest(), signature)