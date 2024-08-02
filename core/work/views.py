from django.shortcuts import render
from .models import workType
from django.shortcuts import get_object_or_404

# Create your views here.
def allWork(req):
    works = workType.objects.all()
    return render(req, "work/allWork.html", {"works": works})

def workDetails(req, work_id):
    work = get_object_or_404(workType, pk=work_id)
    return render(req, "work/workDetails.html", {"work": work})
