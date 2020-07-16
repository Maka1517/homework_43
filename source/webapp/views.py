from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def user_view(request):
    return render(request,'index1.html')

def info_view(request):
    return render(request,'index2.html')

def contact_view(request):
    return render(request,'index3.html')