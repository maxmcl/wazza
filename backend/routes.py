from pathlib import Path

from flask import Blueprint, current_app, request

from utils import group_overlapping_spans, save_to_state, strip_script


api = Blueprint("api", __name__)


def _get_from_db():
    while True:
        for file in Path("./test/").iterdir():
            file = file.open("r").read()
            yield file


db = _get_from_db()


def get_from_db():
    return next(db)


@api.route("/get", methods=["GET"])
def get():
    current_app.logger.debug("Vue app requesting data")
    try:
        html_page = strip_script(get_from_db())
        status = 200
    except Exception as e:
        current_app.logger.exception(e)
        html_page = ""
        status = 500
    return {"html_page": html_page, "id": 0}, status


@api.route("/post", methods=["POST"])
def post():
    current_app.logger.debug("Receiving data from Vue app")
    try:
        data = request.form
        current_app.logger.debug(f"Got data = {data}")
        status = 200
    except Exception as e:
        current_app.logger.exception(e)
        status = 500
    return status
