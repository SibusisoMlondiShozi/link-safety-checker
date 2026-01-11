from urllib.parse import urlparse
from checker.heuristics import *
from checker.domain import get_domain_age
from checker.redirects import count_redirects

def score_url(url: str):
    score = 0
    reasons = []
    meta = {}

    # --- Basic checks ---
    if uses_ip_address(url):
        score += 30
        reasons.append("Uses IP address instead of a domain")

    if not has_https(url):
        score += 20
        reasons.append("Does not use HTTPS")

    if contains_suspicious_keywords(url):
        score += 25
        reasons.append("Contains suspicious keywords")

    if is_long_url(url):
        score += 10
        reasons.append("URL is unusually long")

    # --- Domain age ---
    age = get_domain_age(url)
    meta["domain_age_days"] = age if age is not None else "Unavailable"

    if age is not None:
        if age < 180:
            score += 20
            reasons.append("Domain is very new (less than 6 months)")
        elif age > 1825:
            score -= 10
            reasons.append("Domain is well-established")

    # --- Redirects ---
    redirects = count_redirects(url)
    meta["redirects"] = redirects

    if redirects >= 3:
        score += 15
        reasons.append(f"Multiple redirects detected ({redirects})")
    else:
        reasons.append("No suspicious redirects detected")

    # --- Advanced malicious indicators ---
    p_len = path_length(url)
    meta["path_length"] = p_len

    if p_len > 150:
        score += 25
        reasons.append("Extremely long URL path")

    path = urlparse(url).path
    entropy = shannon_entropy(path)
    meta["path_entropy"] = round(entropy, 2)

    if entropy > 4.5:
        score += 30
        reasons.append("High randomness in URL path (possible obfuscation)")

    if suspicious_tld(url):
        score += 15
        reasons.append("Uses a high-risk top-level domain")

    # --- Verdict ---
    if score <= 30:
        verdict = "SAFE"
        if not reasons:
            reasons.append("No suspicious patterns detected")
    elif score <= 60:
        verdict = "SUSPICIOUS"
    else:
        verdict = "DANGEROUS"

    return score, verdict, reasons, meta
