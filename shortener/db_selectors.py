#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import typing as tp
import pytz
from datetime import datetime

from django.http import Http404

from shortener.models import Url


def urls_get(*, short: str) -> Url:
    """
    Derives original url from short.

    Checks if it expired. If so -- returns None and removes from DB
    """
    try:
        url = Url.objects.get(short=short)

        if datetime.now(pytz.utc) > url.expire_date:
            url.delete()
            raise Http404(f'Link expired.')

        # count used times
        url.used_times += 1
        url.save()
        return url

    except Exception as e:
        raise Http404(f'Not found: {short}') from e


def urls_used_times() -> tp.Iterable[tp.Tuple[str, str, int]]:
    """
    Query DB to show how many times each link was used

    :return:
    """
    urls = Url.objects.all().order_by('-used_times')
    stats = [(url.short, url.long, url.used_times) for url in urls]
    return stats
