from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django import template
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from django.contrib import messages
from .models import Message, tip_model, QA_model, Message_cost, payment
from .forms import chat_first_question_form, payment_form, tip_form, QA_form
from accounts.decorators import allowed_users, unatenticated_user
from datetime import datetime

from datetime import date, timedelta


def cost_chat(request):
    payments = payment.objects.all()
    payment3 = list(filter(lambda x: x.user == request.user, payments))
    if (payment3):
        aa = payment.objects.filter(user=request.user).last()
        some_day_last_week = aa.payment_date + timedelta(days=7)

        is_year = (datetime.today().year >= some_day_last_week.year)
        is_month = (datetime.today().month >= some_day_last_week.month)
        is_day = (datetime.today().day <= some_day_last_week.day)
        is_week = False
        if is_year:
            if is_month:
                if is_day:
                    is_week = True
    else:
        return render(request, 'chat/cost_chat.html')

    context = {
        'is_week': is_week,
        'aa': aa,
    }
    return render(request, 'chat/cost_chat.html', context)


def Inbox(request):
    messages = Message.get_messages(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('chat/free_chat.html')

    return HttpResponse(template.render(context, request))


def UserSearch(request):
    aa = User.objects.all()

    query = request.GET.get("q")
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            "story": aa
        }

    template = loader.get_template('chat/free_chat/search_user_doc.html')

    return HttpResponse(template.render(context, request))


def Directs(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('chat/free_chat.html')

    return HttpResponse(template.render(context, request))


def NewConversation(request, username):
    from_user = request.user
    body = 'שלום'
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('chat:usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('chat:Inbox')


def SendDirect(request):
    Messages = Message.objects.all()
    Message3 = list(filter(lambda x: x.user == request.user, Messages))
    if (Message3):
        from_user = request.user
        to_user_username = request.POST.get('to_user')
        body = request.POST.get('body')

        if request.method == 'POST':
            to_user = User.objects.get(username=to_user_username)
            Message.send_message(from_user, to_user, body)
            return redirect('chat:Inbox')
        else:
            HttpResponseBadRequest()
    else:
        messages.warning( request,'you dont have any chat open yet ,please open a new one')
        return redirect('index')


def checkDirects(request):
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message.objects.filter(user=request.user, is_read=False).count()

    return {'directs_count': directs_count}


def Inbox_cost(request):
    messages = Message_cost.get_messages(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user_cost'].username
        directs = Message_cost.objects.filter(user=request.user, recipient=message['user_cost'])
        directs.update(is_read=True)
        for message in messages:
            if message['user_cost'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('chat/cost_chat/chat.html')

    return HttpResponse(template.render(context, request))


def Directs_cost(request, username):
    user_cost = request.user
    messages = Message_cost.get_messages(user=user_cost)
    active_direct = username
    directs = Message_cost.objects.filter(user=user_cost, recipient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user_cost'].username == username:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('chat/cost_chat/chat.html')

    return HttpResponse(template.render(context, request))


def SendDirect_cost(request):
    Messages = Message_cost.objects.all()
    Message3 = list(filter(lambda x: x.user == request.user, Messages))
    if (Message3):
        from_user_cost = request.user
        to_user_cost_username = request.POST.get('to_user_cost')
        body = request.POST.get('body_cost')

        if request.method == 'POST':
            to_user_cost = User.objects.get(username=to_user_cost_username)
            Message_cost.send_message(from_user_cost, to_user_cost, body)
            return redirect('chat:Inbox_cost')
        else:
            HttpResponseBadRequest()
    else:
        messages.warning( request,'you dont have any chat open yet ,please open a new one')
        return redirect('index')


def NewConversation_cost(request, username):
    from_user = request.user
    body = 'שלום'
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('chat:usersearch_cost')
    if from_user != to_user:
        Message_cost.send_message(from_user, to_user, body)
    return redirect('chat:Inbox_cost')


def UserSearch_cost(request):
    aa = User.objects.all()

    query = request.GET.get("q")
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            "story": aa
        }

    template = loader.get_template('chat/cost_chat/search_user.html')

    return HttpResponse(template.render(context, request))


def checkDirects_cost(request):
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message_cost.objects.filter(user=request.user, is_read=False).count()

    return {'directs_count': directs_count}


def Expert_questions(request):
    form = chat_first_question_form()
    if request.method == "POST":
        form = chat_first_question_form(request.POST or None)

        if form.is_valid():
            user = request.user
            form.instance.user = user
            form.save()
        else:
            print('EROOR FORM INVALID')
        return redirect("chat:cost_chat")

    return render(request, 'chat/cost_chat/expert_questions.html', {'form': form})


def Payment_all(request):
    form = payment_form()
    if request.method == "POST":

        form = payment_form(request.POST or None)

        if form.is_valid():
            user = request.user
            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            email_subject = "Aprovel Payment POZI"
            email_body = 'Hi ' + user.username + "you payment was approved  50INS was received \nyou have one week\n " \
                                                 "for using the chat Pozi for you anytime "

            email = EmailMessage(
                email_subject,
                email_body,
                'rafulhelp@gmail.com',
                [user.email],
            )
            user.save()

            email.send(fail_silently=False)


        else:
            print('EROOR FORM INVALID')
        return redirect("chat:Inbox_cost")

    return render(request, 'chat/cost_chat/payment.html', {'form': form, })


def Daliy_Tip(request):
    All_Tips = tip_model.objects.all()
    context = {
        "Daliy_Tips": All_Tips
    }
    return render(request, 'chat/Daliy_Tip.html', context)


def tip_detail(request, id):
    All_Tips = tip_model.objects.get(id=id)

    context = {
        "Daliy_Tips": All_Tips
    }
    return render(request, 'chat/daliy_tip/tip_detail.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def Daliy_Tip_add(request):
    form = tip_form()
    if request.method == 'POST':
        form = tip_form(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
            messages.success(request, 'Tip was created !')
        else:
            print('EROOR FORM INVALID')
            messages.error(request, 'Tip was not created !')
        return redirect("chat:Daliy_Tip")
    return render(request, 'chat/Daliy_Tip/add_Tip.html', {'form': form})


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_tip(request, id):
    tip = tip_model.objects.get(id=id)

    if request.method == "POST":
        form = tip_form(request.POST, instance=tip)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("chat:tip_detail", id)
    else:
        form = tip_form(instance=tip)
    return render(request, 'chat/Daliy_Tip/add_Tip.html', {"form": form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_tip(request, id):
    daliy_tip = tip_model.objects.get(id=id)

    daliy_tip.delete()
    return redirect("chat:Daliy_Tip")


def QA(request):
    All_QA = QA_model.objects.all()
    context = {
        "QA": All_QA
    }
    return render(request, 'chat/QA.html', context)


def QA_detail(request, id):
    All_QA = QA_model.objects.get(id=id)

    context = {
        "QA": All_QA
    }
    return render(request, 'chat/QA/QA_detail.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def QA_add(request):
    form = QA_form()
    if request.method == 'POST':
        form = QA_form(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
            messages.success(request, 'QA was created !')
        else:
            print('EROOR FORM INVALID')
            messages.error(request, 'QA was not created !')

        return redirect("chat:QA")
    return render(request, 'chat/QA/add_QA.html', {'form': form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_QA(request, id):
    QA = QA_model.objects.get(id=id)

    if request.method == "POST":
        form = QA_form(request.POST, instance=QA)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("chat:QA_detail", id)
    else:
        form = QA_form(instance=QA)
    return render(request, 'chat/QA/add_QA.html', {"form": form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_QA(request, id):
    QA = QA_model.objects.get(id=id)

    QA.delete()
    return redirect("chat:QA")


def profile_search(request):
    aa = User.objects.all()

    query = request.GET.get("q")
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            "profile_search": profile_search
        }

    template = loader.get_template('chat/cost_chat/search_profile.html')

    return HttpResponse(template.render(context, request))
