from datetime import datetime


project = 'Cybel'
description = 'Multi-purpose Discord bot'
author = 'Deeapk Raj'
release = '0.2.3'
year = datetime.now().year
copyright = "{} Py-Contributors".format(year)
source_suffix = ".rst"
source_encoding = "utf-8-sig"

master_doc = "index"
templates_path = ['_templates']
html_static_path = ['_static']
releases_github_path = "Py-Contributors/Cybel"

extensions = [
    'sphinx.ext.autosectionlabel'
]

autosectionlabel_prefix_document = True

html_theme = 'sphinx_rtd_theme'  # 'pydata_sphinx_theme' 'alabaster'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}

rst_epilog = """
.. |project| replace:: Discord Bot
"""

# epub settings
epub_basename = project
epub_theme = 'epub'
epub_description = description
epub_author = author
epub_contributor = 'Py-Contributors'
epub_language = 'en'
epub_publisher = 'Py-Contributors'
epub_copyright = copyright
