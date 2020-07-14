from datetime import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse

from shortener.forms import LinkCreationForm
from shortener.db_services import urls_create
from shortener.db_selectors import urls_get


def index(request):
    if request.method == "POST":
        form = LinkCreationForm(request.POST)

        target = form.data['target']
        expires = form.data['expire_date']
        short = urls_create(url=target, expires=expires)

        resp = JsonResponse({'status': 'success',
                             'short': short,
                             'expires': expires})
        return resp

    context = {'form': LinkCreationForm}
    return render(request, 'index.html', context)


def short_link(request, link_id):
    url = urls_get(short=link_id)
    return redirect(url)
