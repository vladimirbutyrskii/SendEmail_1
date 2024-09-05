from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

import config.settings
from main.forms import ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
# from config.settings import EMAIL_HOST_USER
from django.conf import settings


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            """mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'noreply@oscarbot.ru',
                             ['vlaver@mail.ru'], fail_silently=True)"""
            mail = send_mail('Заявка', 'сообщение', settings.EMAIL_HOST_USER,
                             ['vlaver@mail.ru'], fail_silently=True, )
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'news/test.html', {"form": form})
