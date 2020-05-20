from flask import Flask

from routes import api


app = Flask(__name__)
app.register_blueprint(api)


@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
