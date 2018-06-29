from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'contents'

html_theme_options = {
    'logo_only': True,
    'display_version': False
}

html_logo = '_static/logo.png'

project = u'AliceOS'
copyright = u'2018 AliceOS Developers'
author = u'AliceOS Developers'

def setup(app):
    app.add_stylesheet('custom.css')