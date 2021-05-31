from pyexpat.errors import messages

from accounts.form import register_extra
from django import template

from django.contrib.auth.models import User, Group
from django.core.mail import EmailMessage
from chat.models import tip_model
from . import forms
from .models import stories_model
from .forms import ContactForm, stories_form
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.contrib import messages
import random
from django.shortcuts import render, redirect
from accounts.decorators import allowed_users, unatenticated_user
from django.template import RequestContext, loader


def index(request):
    query = request.GET.get("title")
    items = tip_model.objects.all()

    # if you want only a single random item
    random_item = random.choice(items)
    all_stories = None
    if query:
        all_stories = stories_model.objects.filter(subject__icontains=query)
    else:
        all_stories = stories_model.objects.all()
    context = {
        "stories": all_stories,
        "popup": random_item.text
    }
    return render(request, 'basic_app/index.html', context)


def consultation(request):
    return render(request, 'basic_app/Menu/consultation.html')


def stories(request):
    form = stories_form()
    if request.method == 'POST':
        form = stories_form(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
        else:
            print('EROOR FORM INVALID')
        return redirect("basic_app:index")
    return render(request, 'basic_app/Menu/stories.html', {'form': form})


def font_changing(request):
    return render(request, 'basic_app/settings/font_changing.html', {})


def Videos(request):
    return render(request, 'basic_app/Menu/Videos.html', {})


def about(request):
    return render(request, 'basic_app/settings/about.html', {})


def Review(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)

        else:
            print('EROOR FORM INVALID')
        return redirect("basic_app:index")

    return render(request, "basic_app/settings/Review.html", {'form': form})


def detail(request, id):
    storie = stories_model.objects.get(id=id)

    context = {
        "story": storie
    }
    return render(request, 'basic_app/Menu/stories/detail.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_story(request, id):
    story = stories_model.objects.get(id=id)

    if request.method == "POST":
        form = stories_form(request.POST, instance=story)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("basic_app:detail", id)
    else:
        form = stories_form(instance=story)
    return render(request, 'basic_app/Menu/stories.html', {"form": form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_story(request, id):
    story = stories_model.objects.get(id=id)

    story.delete()
    return redirect("index")
