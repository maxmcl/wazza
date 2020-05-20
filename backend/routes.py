from pathlib import Path

from flask import current_app, Blueprint

from utils import strip_script


api = Blueprint("api", __name__)


def get_from_db():
    return Path("./test/file.html").open("r").read()


@api.route("/")
def get_html():
    current_app.logger.debug("Calling get_html")
    try:
        html_page = strip_script(get_from_db())
        status = 200
    except Exception as e:
        current_app.logger.exception(e)
        html_page = ""
        status = 500
    return {"html_page": html_page, "id": 0}, status
