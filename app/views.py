from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'tHiS iS mY FiLtER','dt':dt,'c':6 }
    return render(request,'filters.html',d)

def user(request):
    d={'data':'TOday We ARE dealing with Userdefined FilTERs'}
    return render(request,'user.html',d)