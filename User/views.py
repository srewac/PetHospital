from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'User/sign_in.html')

def sign_up(request):
    return render(request,'User/sign_up.html')

def sign_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request,'User/sign_up.html')
