import whois
from datetime import datetime
from urllib.parse import urlparse

def get_domain_age(url: str):
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)

        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if not creation_date:
            return None

        return (datetime.now() - creation_date).days

    except Exception:
        return None
