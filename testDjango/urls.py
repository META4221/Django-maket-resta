"""testDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.shortcuts import render


def index(request):
    return HttpResponse(render_to_string('index.html'))


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class SingleBlogView(TemplateView):
    template_name = 'single-blog.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('blog.html/',BlogView.as_view()),
    path('single-blog.html/', SingleBlogView.as_view()),
    path('about.html/', AboutView.as_view())
]
