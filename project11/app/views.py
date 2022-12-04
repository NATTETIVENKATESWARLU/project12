from django.shortcuts import render

# Create your views here.
def venkey(request):
    return render(request,'venkey.html')


def ravi(request):
    return render(request,'ravi.html')

def mass(request):
    return render(request,'mass.html')