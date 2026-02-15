import requests
from urllib.parse import urlsplit, urljoin

from flask import Blueprint, abort

dict_bp = Blueprint("dict_bp",__name__)

@dict_bp.route("/<word>", methods=["GET"])
def dictionary(word):
    try:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        url = urljoin(url, word)
        r = requests.get(url)
        return r.json()
    except Exception as e:
        abort(e)
    
