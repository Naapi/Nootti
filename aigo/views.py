from django.shortcuts import render

from aigo.models import Aigo

# # Create your views here.

def home_view(request):
    """Query SELECT * FROM aigo_aigo"""
    aigos = Aigo.objects.all()
    return render(request, 'aigo/list.html', {'aigos':aigos})
