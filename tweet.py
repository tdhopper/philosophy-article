#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import twitter as tw
import os
import requests


def get_article():
    r = requests.get("http://plato.stanford.edu/cgi-bin/encyclopedia/random")
    title = re.findall(r"<title>(.*) \(.*\)</title>", r.text.replace("\n", ""))[0]
    url = r.url
    return title, url


def tweet(event, context):
    cred = {
        "consumer_key": os.environ["CONSUMER_KEY"].strip(),
        "consumer_secret": os.environ["CONSUMER_SECRET"].strip(),
        "token": os.environ["TOKEN"].strip(),
        "token_secret": os.environ["TOKEN_SECRET"].strip(),
    }
    auth = tw.OAuth(**cred)
    t = tw.Twitter(auth=auth)

    title, url = get_article()
    status = f"{title} {url}"
    t.statuses.update(status=status)
