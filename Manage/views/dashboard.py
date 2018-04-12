from django.shortcuts import render
from Disease.models import Disease, SubDisease


# Create your views here.
def index(request):
    return render(request, 'backend/user/user_info.html')




