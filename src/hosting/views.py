from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect


from .models import Hosting, Click
from .functions import get_client_ip


def home(request):
    hosting_list = Hosting.objects.all().order_by('-score')
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


def click(request, hosting_slug):
    hosting = get_object_or_404(Hosting, slug=hosting_slug)

    ip = get_client_ip(request)

    # Create click object
    click = Click(hosting=hosting, ip=ip)
    click.save()

    return redirect(hosting.affiliate_link)
