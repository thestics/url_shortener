#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

import datetime

from shortener.models import Urls


def urls_create(*, url: str, expires: datetime.datetime):
    ...