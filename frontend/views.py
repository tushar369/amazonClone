from django.shortcuts import render

# Create your views here.

def main(request, *args, **kwargs):
    return render(request, 'frontend/index.html')