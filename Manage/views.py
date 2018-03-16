from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Backend/pages/index.html')


def forms(request):
    return render(request, 'Backend/pages/forms.html')
