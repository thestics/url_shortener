#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

from django.http import Http404

from shortener.models import Urls


def urls_get(*, short: str):
    """
    Derives original url from short.

    Checks if it expired. If so -- returns None and removes from DB
    """
    try:
        url = Urls.objects.get(short=short)
        return url.long
    except Exception as e:
        raise Http404(f'Not found: {short}') from e
