from django.shortcuts import get_object_or_404, render

from .models import Hosting


def home(request):
    hosting_list = Hosting.objects.all()

    context = {
        'hosting_list': hosting_list,
    }

    return render(request, 'hosting/home.html', context)


def review(request, hosting_slug):
    hosting = get_object_or_404(Hosting, slug=hosting_slug)
    top_hostings = Hosting.objects.all()

    context = {
        'hosting': hosting,
        'top_hostings':  top_hostings,

    }

    return render(request, 'hosting/review.html', context)
