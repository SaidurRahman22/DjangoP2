from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .models.product import Product
from django.contrib import messages, auth
from django.contrib.auth.models import User


def index(request):
    prds = Product.get_all_products()
    print('You are the :', request.session.get('username'))
    return render(request, 'index.html', {'products': prds})


def login(request):
    if request.method == "POST":
        method_dict = request.POST.copy()

        username = method_dict.get('username')

        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        request.session['user_id'] = user.id
        request.session['username'] = user.username

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You sucessfully login')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid Credential!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'login.html')


def reg(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken!')
                else:
                    User.objects.create_user(username=username,
                                             password=password,
                                             email=email
                                             )
                    messages.success(request, 'You are successfully registered!')
                    return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Password does not match!')

        return HttpResponseRedirect(reverse('reg'))
    return render(request, 'reg.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.error(request, 'You are now loggd out')
        return HttpResponseRedirect(reverse('index'))


def shop(request):
    prds = Product.get_all_products()
    return render(request, 'shop.html', {'products': prds})


def single(request):
    cprds = Product.objects.get(id=3)
    return render(request, 'single.html', {'product': cprds})


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def checkout(request):
    return render(request, 'checkout.html')
