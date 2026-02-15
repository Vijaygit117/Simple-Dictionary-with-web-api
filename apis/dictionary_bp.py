import requests
import json
from urllib.parse import urlsplit, urljoin

from flask import Blueprint, abort, jsonify

dict_bp = Blueprint("dict_bp",__name__)

@dict_bp.route("/<word>", methods=["GET"])
def dictionary(word):

    try:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        url = urljoin(url, word)

        res = requests.get(url)
        data = res.json()

        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        partsofspeech = data[0]["meanings"][0]["partOfSpeech"]
        url = data[0]["sourceUrls"]
        return jsonify({
                    "Word": word,
                    "Meaning": meaning,
                    "Part of speech": partsofspeech,
                    "url": url
                })

    except (IndexError, KeyError):
        abort(404, description="Meaning not found")

    except Exception as e:
        abort(500, description=str(e))
    
