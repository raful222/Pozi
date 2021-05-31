from django.urls import path, re_path, reverse_lazy
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "chat"

urlpatterns = [
    url(r'^cost_chat/$', views.cost_chat, name='cost_chat'),
    url(r'^cost_chat/Expert_questions$', views.Expert_questions, name='Expert_questions'),
    url(r'^cost_chat/Payment_all', views.Payment_all, name='Payment_all'),

    path('Inbox/', views.Inbox, name='Inbox'),
    path('free_chat/<username>', views.Directs, name='free_chat'),
    path('send/', views.SendDirect, name='send_direct'),
    path('new/', views.UserSearch, name='usersearch'),
    path('new/<username>', views.NewConversation, name='newconversation'),

    path('profile_search/', views.profile_search, name='profilesearch'),

    path('Inbox_cost/', views.Inbox_cost, name='Inbox_cost'),
    path('Directs_cost/<username>', views.Directs_cost, name='Directs_cost'),
    path('send_cost/', views.SendDirect_cost, name='SendDirect_cost'),
    path('new_cost/', views.UserSearch_cost, name='usersearch_cost'),
    path('new_cost/<username>', views.NewConversation_cost, name='newconversation_cost'),

    url(r'^Daliy_Tip/$', views.Daliy_Tip, name='Daliy_Tip'),
    url(r'^Daliy_Tip/Daliy_Tip_add/$', views.Daliy_Tip_add, name='Daliy_Tip_add'),
    path('Daliy_Tip/tip_detail/<int:id>/', views.tip_detail, name='tip_detail'),
    path('Daliy_Tip/edit_tip/<int:id>/', views.edit_tip, name='edit_tip'),
    path('Daliy_Tip/delete_tip/<int:id>/', views.delete_tip, name='delete_tip'),

    url(r'^QA/$', views.QA, name='QA'),
    url(r'^QA/QA_add/$', views.QA_add, name='QA_add'),
    path('QA/QA_detail/<int:id>/', views.QA_detail, name='QA_detail'),
    path('QA/edit_QA/<int:id>/', views.edit_QA, name='edit_QA'),
    path('QA/delete_QA/<int:id>/', views.delete_QA, name='delete_QA'),

]
