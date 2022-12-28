from django.shortcuts import render

# Create your views here.

def tracking(request):
    context = {
        
    }
    return render(request, "dashbord/pages/tracking.html", context)