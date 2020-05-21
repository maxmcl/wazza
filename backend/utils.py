import lxml
from flask import current_app
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True


def strip_script(html):
    html = lxml.html.fromstring(html)
    cleaner(html)
    return lxml.html.tostring(html).decode("utf8").replace("'", '"')


def group_overlapping_spans():
    pass


def save_to_state():
    pass
