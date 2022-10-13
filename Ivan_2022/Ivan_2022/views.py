from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed = user_text[::-1]
    return render(request, 'reverse.html', {'reversed': reversed})
