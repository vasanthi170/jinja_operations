from django.shortcuts import render

# Create your views here.

def conditions(request):
    d = {'name':'vikash','age':21,'gender':'male','salary':25000,'shift':'dayshift'}
    return render(request,'conditions.html',context=d)
