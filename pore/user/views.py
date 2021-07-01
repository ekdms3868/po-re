from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'user/main.html')

def login(request):
    return render(request, 'user/login.html')