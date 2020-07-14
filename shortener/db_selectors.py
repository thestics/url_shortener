#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import pytz
from datetime import datetime

from django.http import Http404

from shortener.models import Urls


def urls_get(*, short: str):
    """
    Derives original url from short.

    Checks if it expired. If so -- returns None and removes from DB
    """
    try:
        url = Urls.objects.get(short=short)

        if datetime.now(pytz.utc) > url.expire_date:
            url.delete()
            raise Http404(f'Link expired.')

        # count used times
        url.used_times += 1
        url.save()
        return url

    except Exception as e:
        raise Http404(f'Not found: {short}') from e
