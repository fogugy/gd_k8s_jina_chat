import os
import requests
import json

from flask import Flask, Response, jsonify, request
from flask import render_template

from jina import Client, Document
from jina.types.document.generators import from_csv

PORT = os.environ['SERVICE_PORT']
JINA_HOST = os.environ['JINA_HOST']
JINA_PORT = int(os.environ['JINA_PORT'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    item = {
        'tags': {
            'caption': 'None',
            'image': 'None',
        },
        'score': {
            'value': 'None'
        }
    }

    payload = 'Payload stub'
    return render_template('index.html',
                           text='Multimodal neural search',
                           item=item,
                           payload=payload)


@app.route('/init_index', methods=['POST'])
def init_index():
    with open('./data/dataset.csv') as fp:
        c = Client(host=JINA_HOST, port_expose=JINA_PORT, restful=True)
        return c.post('/index', from_csv(fp, field_resolver={'question': 'text'}))


@app.route('/search', methods=['POST'])
def search():
    r_jina = requests.post(f'http://{JINA_HOST}:{JINA_PORT}/search', json=json.loads(request.data))

    r = Response(
        r_jina.text,
        status=r_jina.status_code,
        content_type=r_jina.headers['content-type']
    )
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r


@app.route('/ping', methods=['GET'])
def ping():
    return Response('pong\n', status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
