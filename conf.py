from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

project = u'AliceOS'
copyright = u'2018 AliceOS Developers'  # pylint: disable=redefined-builtin
author = u'AliceOS Developers'

def setup(app):
    app.add_stylesheet('custom.css')