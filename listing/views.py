from django.shortcuts import render
from .models import Listing


def index(request):
    return render(request, 'listing/index.html', {"listings": Listing.objects.all()})


def show(request, listing_id):
    return render(request, 'listing/single.html')


def search(request):
    return render(request, 'listing/search.html')
