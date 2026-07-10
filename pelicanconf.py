from datetime import date

AUTHOR = "Gael Espinosa"
SITENAME = "Gael Espinosa"
SITESUBTITLE = "Full Stack Engineer"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["blog", "projects"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

TIMEZONE = "America/Santiago"
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

# Create a form at https://formspree.io and paste its ID here (e.g. "mqkvyzab")
FORMSPREE_ID = "xkoldeey"

BIO = (
    "Full stack engineer with 10+ years across Python, JavaScript, and cloud "
    "infrastructure. Known for deep curiosity, fast learning, and being the "
    "person teammates turn to when problems get hard. Equally at home designing "
    "backend systems from scratch or diving into complex existing codebases."
)

ROLE = "Full Stack Engineer"
LOCATION = "Valparaíso, Chile"

SOCIAL_LINKS = [
    {"name": "GitHub", "url": "https://github.com/picklecillo", "icon": "github"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/gaelespinosa/", "icon": "linkedin"},
]

EXPERIENCE = [
    {
        "role": "Senior Software Engineer",
        "company": "tvScientific",
        "url": "https://www.tvscientific.com",
        "start": "May 2023",
        "end": "Sep 2025",
        "summary": (
            "Lead full stack engineer on a fast-paced adtech SaaS platform, owning "
            "backend architecture and frontend foundations across a major codebase "
            "overhaul. Led a backend refactor that reduced system complexity and "
            "improved performance, built the foundational architecture for a new "
            "core frontend app, and drove shift-left practices to catch bugs "
            "earlier in the pipeline."
        ),
        "stack": ["Python", "TypeScript", "React", "AWS"],
    },
    {
        "role": "Technical Lead",
        "company": "Unholster",
        "url": "https://unholster.com",
        "start": "Feb 2022",
        "end": "May 2023",
        "summary": (
            "Technical lead for multiple cloud-native SaaS products on AWS and GCP, "
            "responsible for system design, delivery, and team mentoring. Designed "
            "and led the implementation of a scalable near real-time HIPAA-compliant "
            "medical data ETL pipeline and built a serverless organizational "
            "governance platform."
        ),
        "stack": ["Python", "AWS", "GCP", "Serverless"],
    },
    {
        "role": "Software Engineer",
        "company": "BitterSweet",
        "start": "Jan 2021",
        "end": "Feb 2022",
        "summary": (
            "One of two engineers with full technical ownership over a data science "
            "platform for the oil and gas industry. Translated research notebooks "
            "into production-ready features and designed REST APIs, covering "
            "everything from infrastructure to UI for an oilfield resource "
            "optimization product."
        ),
        "stack": ["Python", "REST APIs", "Data science"],
    },
    {
        "role": "Consultant — Developer",
        "company": "ThoughtWorks",
        "url": "https://www.thoughtworks.com",
        "start": "Mar 2018",
        "end": "Dec 2020",
        "summary": (
            "Delivered CI/CD infrastructure and resource provisioning at scale for "
            "a major airline, enabling multiple parallel feature teams to develop "
            "and ship independently. Eliminated weekly CI/CD infrastructure "
            "failures by modernizing legacy Jenkins instances."
        ),
        "stack": ["CI/CD", "Jenkins", "DevOps"],
    },
    {
        "role": "Software Engineer",
        "company": "Unholster",
        "url": "https://unholster.com",
        "start": "Feb 2016",
        "end": "Mar 2018",
        "summary": (
            "Full stack engineer delivering mission-critical software for Chile's "
            "national power grid coordinator. Automated manual financial "
            "calculations with zero-tolerance accuracy requirements and built web "
            "platforms, real-time data processing pipelines, and reporting tools "
            "that eliminated error-prone manual processes."
        ),
        "stack": ["Python", "Data pipelines", "Integrations"],
    },
    {
        "role": "Software Engineer",
        "company": "Nuwit",
        "start": "Jan 2015",
        "end": "Feb 2016",
        "summary": (
            "Backend engineer building customer-facing web applications for a major "
            "retail mall — discovery, ticketing, and parking systems. Implemented a "
            "TF-IDF-based recommendation engine for similar product suggestions."
        ),
        "stack": ["Java", "Python", "NoSQL"],
    },
    {
        "role": "Software Engineer & Founder",
        "company": "QWERTY",
        "start": "Mar 2012",
        "end": "Dec 2015",
        "summary": (
            "Co-founded a software consultancy delivering web and mobile solutions "
            "across energy, legal, and small business sectors. Grew the client base "
            "to 10+ — the consultancy continues operating today — and established "
            "its core technical infrastructure and development processes."
        ),
        "stack": ["PHP", "WordPress", "Web & mobile"],
    },
]
