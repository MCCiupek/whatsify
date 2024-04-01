import re


def extract_links(filename):
    with open(filename) as f:
        data = f.read()
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+(?![^\s.,?!])")
    urls = re.findall(url_pattern, data)
    sanitized_urls = [url.rstrip(".").rstrip(",") for url in urls]
    return sanitized_urls


def filter_urls(urls, filter_on="spotify"):
    return [url for url in urls if filter_on in url]
