import time

BLOG_AUTHOR = "team"  # (translatable)
BLOG_TITLE = "texture.design"  # (translatable)

SITE_URL = "https://texture.design/"
BASE_URL = "https://texture.design/"
BLOG_EMAIL = "hi@texture.design"

BLOG_DESCRIPTION = ""  # (translatable)
DEFAULT_LANG = "en"
DEFAULT_PREVIEW_IMAGE = "/assets/profile.png"

TRANSLATIONS = { DEFAULT_LANG: "", }
TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

NAVIGATION_LINKS = {
    DEFAULT_LANG: []
        # ("/archive.html", "Archives"),
        # ("/categories/index.html", "Tags"),
        # ("/rss.xml", "RSS feed"),
}

NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

THEME = "td"
THEME_COLOR = '#5f783b'

THEME_CONFIG = {
    DEFAULT_LANG: {
        'featured_large': False,
        'featured_small': True,
        'featured_on_mobile': True,
        'featured_large_image_on_mobile': True,
        'featured_strip_html': True,
        'sidebar': ''
    }
}

POSTS = (
    ("posts/*.rst", "blog", "post.tmpl"),
)
# INDEX_PATH = "blog"
INDEX_TEASERS = True

PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
)

TIMEZONE = "UTC"
DATE_FANCINESS = 0


COMPILERS = {
    "rest": ['.rst'],
    "html": ['.html'],
}

# ONE_FILE_POSTS = True
HIDDEN_TAGS = ['mathjax']
CATEGORY_ALLOW_HIERARCHIES = False
CATEGORY_OUTPUT_FLAT_HIERARCHY = False
HIDDEN_CATEGORIES = []
HIDDEN_AUTHORS = ['Guest']

FRONT_INDEX_HEADER = { DEFAULT_LANG: '' }

ATOM_FILENAME_BASE = "feed"
REDIRECTIONS = []

IMAGE_FOLDERS = {'images': 'images'}
IMAGE_THUMBNAIL_SIZE = 512
IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'
FEED_LINKS_APPEND_QUERY = False

LICENSE = ""
CONTENT_FOOTER = 'Copyright &copy; {date}, texture.design.'

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

SHOW_SOURCELINK = False

RSS_COPYRIGHT = 'Copyright (c) {date}, texture.design.'
RSS_COPYRIGHT_PLAIN = 'Copyright (c) {date}, texture.design.'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

STRIP_INDEXES = True
PRETTY_URLS = True

USE_CDN = False
USE_TAG_METADATA = False

GLOBAL_CONTEXT = {}
GLOBAL_CONTEXT_FILLER = []