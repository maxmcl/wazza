import lxml
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True


def strip_script(html):
    html = lxml.html.fromstring(html)
    cleaner(html)
    return lxml.html.tostring(html).decode('utf8').replace("'", '"')
