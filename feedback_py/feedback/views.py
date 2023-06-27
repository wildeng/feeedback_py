# myapp/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserLoginForm


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("feedback")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})
# myapp/views.py


def feedback_view(request):
    return render(request, 'feedback/feedback.html')

