from django.shortcuts import render


def home(request):
    return render(request, "example/index.html", {})


def projects(request):
    return render(request, 'projects.html')


def about(request):
    return render(request, 'about.html')


def cv(request):
    return render(request, 'example/cv.html')
