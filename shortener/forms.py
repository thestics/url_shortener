#!/usr/bin/env python3
# -*-encoding: utf-8-*-
# Author: Danil Kovalenko

from django.forms import Form, CharField, DateTimeField, DateTimeInput, TextInput


class LinkCreationForm(Form):
    target = CharField(max_length=2048,
                       widget=TextInput(attrs={'class': 'form-control w-25'}))
    expire_date = DateTimeField(widget=DateTimeInput(
        attrs={'type': 'datetime-local', 'class': 'form-control w-25'}))
