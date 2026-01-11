import re
import math
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account",
    "bank", "update", "free", "win", "bonus"
]

SUSPICIOUS_TLDS = {
    "xyz", "top", "shop", "click", "monster", "buzz", "live", "free"
}

def uses_ip_address(url: str) -> bool:
    domain = urlparse(url).netloc
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", domain) is not None

def has_https(url: str) -> bool:
    return url.startswith("https://")

def contains_suspicious_keywords(url: str) -> bool:
    url = url.lower()
    return any(word in url for word in SUSPICIOUS_KEYWORDS)

def is_long_url(url: str) -> bool:
    return len(url) > 75

def path_length(url: str) -> int:
    return len(urlparse(url).path)

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    probabilities = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probabilities)

def suspicious_tld(url: str) -> bool:
    domain_parts = urlparse(url).netloc.split(".")
    return domain_parts[-1] in SUSPICIOUS_TLDS
