from datetime import date

AUTHOR = "Gael Espinosa"
SITENAME = "Gael Espinosa"
SITESUBTITLE = "Software Engineer"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["blog", "projects"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.svg": {"path": "favicon.svg"},
}

TIMEZONE = "America/Mexico_City"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%b %d, %Y"

THEME = "theme"
DIRECT_TEMPLATES = ["index"]
PAGINATED_TEMPLATES = {}

# Folder name (blog/projects) becomes the category
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Feeds off during development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

# --- Site data ---------------------------------------------------------------

CURRENT_YEAR = date.today().year
GITHUB_USERNAME = "picklecillo"
CONTACT_EMAIL = "gael.espinosa.h@gmail.com"

# Create a form at https://formspree.io and paste its ID here (e.g. "mqkvyzab")
FORMSPREE_ID = "YOUR_FORM_ID"

BIO = (
    "I'm a software engineer who enjoys building reliable backend systems, "
    "developer tools, and the occasional side project that gets out of hand. "
    "Currently focused on Python, distributed systems, and making software "
    "that's a pleasure to maintain."
)

ROLE = "Software Engineer"

SOCIAL_LINKS = [
    {"name": "GitHub", "url": "https://github.com/picklecillo", "icon": "github"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/your-profile", "icon": "linkedin"},
    {"name": "Email", "url": "mailto:gael.espinosa.h@gmail.com", "icon": "email"},
]

EXPERIENCE = [
    {
        "role": "Senior Software Engineer",
        "company": "Acme Corp",
        "url": "https://example.com",
        "start": "2023",
        "end": "Present",
        "summary": (
            "Lead backend development for the core platform. Designed a "
            "high-throughput event pipeline and mentored a team of four engineers."
        ),
        "stack": ["Python", "PostgreSQL", "Kafka", "AWS"],
    },
    {
        "role": "Software Engineer",
        "company": "Startup Inc",
        "url": "https://example.com",
        "start": "2020",
        "end": "2023",
        "summary": (
            "Built REST and GraphQL APIs powering the customer-facing product. "
            "Cut p95 API latency by 60% through query optimization and caching."
        ),
        "stack": ["Python", "Django", "Redis", "Docker"],
    },
    {
        "role": "Junior Developer",
        "company": "First Job LLC",
        "url": "https://example.com",
        "start": "2018",
        "end": "2020",
        "summary": (
            "Full-stack development on internal tools. Automated manual reporting "
            "workflows, saving the operations team ~10 hours a week."
        ),
        "stack": ["Python", "JavaScript", "MySQL"],
    },
]
