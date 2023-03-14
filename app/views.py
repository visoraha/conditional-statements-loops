from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':20,'b':50,'c':40}
    return render(request,'conditions.html',context=d)
def loop(request):
    x={'name':'vinayvicky'}
    return render(request,'forloop.html',context=x)
