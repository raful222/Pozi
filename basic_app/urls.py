from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^consultation/$', views.consultation, name='consultation'),
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^font_changing/$', views.font_changing, name='font_changing'),
    url(r'^Videos/$', views.Videos, name='Videos'),
    url(r'^settings/Review/$', views.Review, name='Review'),
    url(r'^about/$', views.about, name='about'),
    path('stories/detail/<int:id>/', views.detail, name='detail'),
    path('stories/edit_story/<int:id>/', views.edit_story, name='edit_story'),
    path('delete_story/<int:id>/', views.delete_story, name='delete_story'),

]
