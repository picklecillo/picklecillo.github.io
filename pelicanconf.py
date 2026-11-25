from datetime import date

AUTHOR = "Gael Espinosa"
SITENAME = "Gael Espinosa"
SITESUBTITLE = "Generalist Software Engineer"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ["blog", "projects"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["extra", "images"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
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
    "Generalist software engineer with 10+ years across the stack: Python, "
    "JavaScript, cloud infrastructure, and lately Flutter. Known for deep curiosity and fast learning. I try to "
    "leave every team better than I found it. Equally at home designing "
    "backend systems from scratch or diving into complex existing codebases. "
    "Now running Pickle Labs, a small software studio in Valparaíso."
)

ROLE = "Software engineer & founder"
LOCATION = "Valparaíso, Chile"

SOCIAL_LINKS = [
    {"name": "GitHub", "url": "https://github.com/picklecillo", "icon": "github"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/gaelespinosa/", "icon": "linkedin"},
]

# What I'm doing now, shown above the themes.
EXPERIENCE_NOW = [
    {
        "company": "Pickle Labs",
        "url": "https://picklelabs.cl",
        "years": "2026–now",
        "text": (
            "Founded a small software studio in Valparaíso. Custom web apps, "
            "backend and cloud work, and technical consulting. Same work as "
            "always, my name on the door this time."
        ),
    },
    {
        "company": "Fichario",
        "url": "https://fichario.cl",
        "years": "2026–now",
        "text": (
            "Our first product: encrypted, offline-first clinical records for therapists "
            "in Chile, built ahead of the new data protection law (Ley 21.719). "
            "The hard part is security a non-technical user can't get wrong."
        ),
        "more": "projects/fichario-encrypted-clinical-records-for-therapists/",
    },
]

# Experience grouped by theme. A job can show up under more than one theme.
EXPERIENCE_THEMES = [
    {
        "title": "Data that can't be wrong",
        "tags": ["Python", "Data pipelines", "AWS", "GCP"],
        "items": [
            {
                "company": "Unholster",
                "url": "https://unholster.com",
                "years": "2016–18",
                "text": (
                    "Replaced hand-run financial calculations for Chile's national "
                    "power grid coordinator. Zero tolerance for being off by a peso."
                ),
                "lesson": "When the numbers are money, boring and provable beats clever.",
            },
            {
                "company": "Unholster",
                "url": "https://unholster.com",
                "years": "2022–23",
                "text": (
                    "Designed a near real-time medical data pipeline under HIPAA. "
                    "Fast was easy. Fast and compliant was the job."
                ),
                "lesson": "Compliance is a design input, not a checklist at the end.",
            },
            {
                "company": "BitterSweet",
                "years": "2021–22",
                "text": (
                    "Turned data scientists' research notebooks into production "
                    "features for oilfield resource optimization."
                ),
                "lesson": "A notebook that works once is a hypothesis.",
            },
            {
                "company": "Nuwit",
                "years": "2015–16",
                "text": (
                    "Built a TF-IDF recommender for a retail mall's discovery app, "
                    "alongside its ticketing and parking systems."
                ),
                "lesson": "Simple models, well applied, go a long way.",
            },
        ],
    },
    {
        "title": "Ground other teams stand on",
        "tags": ["TypeScript", "React", "CI/CD", "Jenkins"],
        "items": [
            {
                "company": "ThoughtWorks",
                "url": "https://www.thoughtworks.com",
                "years": "2018–20",
                "text": (
                    "An airline's CI/CD fell over every week. I rebuilt the Jenkins "
                    "setup and provisioning so parallel feature teams could ship "
                    "without waiting on each other. It stopped falling over."
                ),
                "lesson": "Good infra is invisible. That's the point.",
            },
            {
                "company": "tvScientific",
                "url": "https://www.tvscientific.com",
                "years": "2023–25",
                "text": (
                    "Untangled an adtech backend, laid the foundations for a new core "
                    "frontend app, and pushed testing left so bugs died in PRs, not prod."
                ),
                "lesson": "Shortcuts in shared code get paid back by someone else, with interest.",
            },
        ],
    },
    {
        "title": "Owning the whole thing",
        "tags": ["System design", "Mentoring", "Web & mobile"],
        "items": [
            {
                "company": "QWERTY",
                "years": "2012–15",
                "text": (
                    "Co-founded a small consultancy building web and mobile apps for "
                    "10+ clients in energy, legal, and small business. It's still running."
                ),
                "lesson": "Clients don't buy code. They buy the problem going away.",
            },
            {
                "company": "BitterSweet",
                "years": "2021–22",
                "text": "One of two engineers. Infra, APIs, UI: if it broke, it was ours.",
                "lesson": "Owning everything teaches you which parts actually matter.",
            },
            {
                "company": "Unholster",
                "url": "https://unholster.com",
                "years": "2022–23",
                "text": (
                    "Tech lead across several cloud products: system design, delivery, "
                    "and mentoring."
                ),
                "lesson": "The job shifted from writing the best code to making the team's code better.",
            },
        ],
    },
]

# Compact chronology, shown as "the short version" under the themes.
EXPERIENCE = [
    {"role": "Founder", "company": "Pickle Labs", "years": "2026–now"},
    {"role": "Senior Software Engineer", "company": "tvScientific", "years": "2023–25"},
    {"role": "Technical Lead", "company": "Unholster", "years": "2022–23"},
    {"role": "Software Engineer", "company": "BitterSweet", "years": "2021–22"},
    {"role": "Consultant — Developer", "company": "ThoughtWorks", "years": "2018–20"},
    {"role": "Software Engineer", "company": "Unholster", "years": "2016–18"},
    {"role": "Software Engineer", "company": "Nuwit", "years": "2015–16"},
    {"role": "Co-founder", "company": "QWERTY", "years": "2012–15"},
]
