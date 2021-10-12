from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def ordened_list():
    return {
        "data": sorted(request.json, reverse=True, key=lambda x: x['puntuacion'])
    }


if __name__ == '__main__':
    app.run()
