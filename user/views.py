from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'cart.html')


def userprofile(request):
    return render(request, template_name='userprofile.html')


def feedback(request):
    return render(request, 'feedback.html')
