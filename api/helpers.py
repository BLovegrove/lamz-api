from urllib.parse import parse_qs, urlparse


def parse_url(url):
    
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)