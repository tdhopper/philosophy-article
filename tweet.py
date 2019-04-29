import re
import requests
import sys
import twitter as tw
import json


def get_article():
    r = requests.get("http://plato.stanford.edu/cgi-bin/encyclopedia/random")
    try:

        title = re.findall(r"<title>(.*) \(.*\)</title>", r.text.replace("\n", ""))[0]
        url = r.url
    except IndexError:
        sys.exit(0)
    return title, url


def update_twitter(title, url):
    with open("twitter.json", "r") as f:
        credentials = json.load(f)
    t = tw.Api(**credentials)
    try:
        status = "{} {}".format(title, url)
        t.PostUpdate(status=status)
        return "Tweeted {}".format(status)
    except Exception as e:
        return e.message[0]['message']


def update(event=None, context=None):
    title, url = get_article()
    twitter_log = update_twitter(title, url)
    return twitter_log


if __name__ == '__main__':
    print(update())
