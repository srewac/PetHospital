from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'Test/test.html')

def select_paper(request):
    return render(request, 'Test/select_paper.html')

def test_management(request):
    return render(request, 'Test/test_management.html')