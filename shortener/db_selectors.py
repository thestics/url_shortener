#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko


from shortener.models import Urls


def urls_get(*, short: str):
    """
    Derives original url from short.

    Checks if it expired. If so -- returns None and removes from DB
    """
    ...