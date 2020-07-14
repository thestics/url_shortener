#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import random
import string

import datetime

from shortener.models import Url
from shortener.const import URL_SIZE


def _rand_identifier(size: int):
    source = string.ascii_letters + string.digits
    res = ''

    for i in range(size):
        res += random.choice(source)

    return res


def urls_create(*, url: str, expires: str):
    """Create new short url from long url"""
    new_id = _rand_identifier(URL_SIZE)
    expires += '+00:00'
    expire_date = datetime.datetime.fromisoformat(expires)

    # add new
    Url.objects.create(short=new_id, long=url, expire_date=expire_date)
    return new_id
