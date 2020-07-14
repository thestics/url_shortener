from django.shortcuts import render
from django.http import JsonResponse

from shortener.forms import LinkCreationForm
from shortener.db_services import urls_create


def index(request):
    print(request.POST)

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
