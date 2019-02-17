# Imports the Google Cloud client library
import json
import requests
import unicodedata
from google.cloud import translate
from flask import Flask, jsonify


def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

def yamabiko(request):
    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = ''
    request_json = request.get_json()
    if request.args and 'text' in request.args:
        text = request.args.get('text')
    elif request_json and 'text' in request_json:
        text = request_json['text']
    elif request.form and 'text' in request.form:
        text = request.form['text']
    else:
        print('no data')
        return 'no data'

    if not is_japanese(text):
        print('It is not Japanese.')
        return 'It is not Japanese.'

    if ':coffee:' in text:
        print('It is a bot message.')
        return 'It is a bot message.'

    translation = translate_client.translate(
        text,
        target_language='en')

    translatedText = translation['translatedText'] + ' :coffee:'
    return jsonify(text=translatedText)
