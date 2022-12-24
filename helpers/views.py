from django.shortcuts import render

# Create your views here.

def page_404(request, exception):
    return render(request, "dashbord/error-404/page_404.html")