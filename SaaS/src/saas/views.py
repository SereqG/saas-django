from django.shortcuts import render

from visits.models import Visit


def home_page(request, *args, **kwargs):
    qs = Visit.objects.all()
    Visit.objects.create()

    print(qs.count())

    my_context = {"page_visit_count": qs.count()}
    return render(request, "home.html", my_context)
