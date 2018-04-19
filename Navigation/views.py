from django.shortcuts import render, render_to_response, HttpResponseRedirect


# Create your views here.
def hall(request):
    return render(request, 'Navigation/hall.html')


def ward(request):
    return render(request, 'Navigation/ward.html')
