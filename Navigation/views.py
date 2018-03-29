from django.shortcuts import render

# Create your views here.
def hall(request):
    return render(request, 'Navigation/hall.html')

def ward(request):
    return render(request, 'Navigation/ward.html')

def ward2(request):
    return render(request, 'Navigation/ward2.html')