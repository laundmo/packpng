
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import os

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
    cache = Cache(config={'CACHE_TYPE': 'null'}) # use type 'simple' to test caching