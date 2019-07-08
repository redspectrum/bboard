from django.shortcuts import redirect

def redirect_bboard(request):
    return redirect('index', permanent=True)