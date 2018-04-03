from django.shortcuts import render,render_to_response,HttpResponseRedirect

# Create your views here.
def hall(request):
    if request.session.get('username', None):
        return render(request, 'Navigation/hall.html')
    else:
        return HttpResponseRedirect('/User/sign_in/')


def ward(request):
    if request.session.get('username', None):
        return render(request, 'Navigation/ward.html')

    else:
        return HttpResponseRedirect('/User/sign_in/')
