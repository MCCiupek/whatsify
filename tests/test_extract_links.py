from src.extract_links import extract_links, filter_urls


def test_extract_links():
    filename = "tests/data/test_data.txt"
    urls = extract_links(filename)
    assert urls == [
        "https://open.spotify.com/track/2xLMifQCjDGFmkHkpNLD9h",
        "https://open.spotify.com/album/4eLPsYPBmXABThSJ821sqY",
        "https://goo.gl/maps/Choq5Hj7unhwm8c98",
        "https://www.google.com/maps/place/Red+Rocks+Park+and+Amphitheatre/@39.6657237,-105.2055982",
        "https://open.spotify.com/album/57xjPyRgpFz3f3I65sBh2u",
    ]


def test_filter_urls():
    urls = [
        "https://open.spotify.com/track/2xLMifQCjDGFmkHkpNLD9h",
        "https://open.spotify.com/album/4eLPsYPBmXABThSJ821sqY",
        "https://goo.gl/maps/Choq5Hj7unhwm8c98",
        "https://www.google.com/maps/place/Red+Rocks+Park+and+Amphitheatre/@39.6657237,-105.2055982",
        "https://open.spotify.com/album/57xjPyRgpFz3f3I65sBh2u",
    ]
    filtered_urls = filter_urls(urls)
    assert filtered_urls == [
        "https://open.spotify.com/track/2xLMifQCjDGFmkHkpNLD9h",
        "https://open.spotify.com/album/4eLPsYPBmXABThSJ821sqY",
        "https://open.spotify.com/album/57xjPyRgpFz3f3I65sBh2u",
    ]
