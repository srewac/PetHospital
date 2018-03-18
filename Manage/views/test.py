from django.shortcuts import render


def test_index(request):
    return render(request, 'backend/test/tables.html')


def testpapaer_index(request):
    return render(request, 'backend/test/tables.html')
