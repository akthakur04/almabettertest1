from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import studmarks
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

def marks(request):
    if request.method == 'POST':
        mk = studmarks()
        mk.name = request.POST.get('name')
        mk.roll = request.POST.get('roll')
        mk.math = request.POST.get('math')
        mk.phy = request.POST.get('phy')
        mk.chem = request.POST.get('chem')
        mk.save()
        return render(request, 'marks.html')
    else:
        return render(request, 'marks.html')


def rank(request):
    # alldta = studmarks.objects.all()
    alldta = studmarks.objects.all().order_by('-percentage')

    return render(request, 'rankng.html', {'alldta': alldta})
def sortnsearch(request):
    # alldta = studmarks.objects.all()
    QUERY=request.GET.get('q')
    quer = request.GET.get('qu')  # new
    alldta = studmarks.objects.all().filter( Q(name__icontains=quer) | Q(roll__icontains=quer) | Q(total__contains=quer)| Q(percentage__icontains=quer)).order_by(QUERY)

    return render(request, 'rankng.html', {'alldta': alldta})


