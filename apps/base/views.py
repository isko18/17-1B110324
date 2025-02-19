from django.shortcuts import render
from apps.base.models import Base, Popular_category, Our_chef
# Create your views here.

def index(request):
    base = Base.objects.latest('id')
    category = Popular_category.objects.all()
    chef = Our_chef.objects.all().order_by('?')[:3]
    return render(request, 'index-dark.html', locals())
