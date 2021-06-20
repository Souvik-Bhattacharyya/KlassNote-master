from django.core import paginator
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from . import models


def index_view(request):
    return render(request, 'index.html')


def contact_view(request):
    status = 0
    if request.method == 'POST':
        if 'name' in request.POST and 'email' in request.POST and 'message' in request.POST:
            print(request.POST)
            contact = models.ContactUs(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message'])
            contact.save()
            print("hello")
            status = 1
        else:
            status = -1
    return render(request, 'contact.html', {'status': status})


def about_view(request):
    # about info
    about = models.AboutUs.objects.all()[0]
    about.about_text = about.about_text.replace('\r\n', '<br />')

    # directors
    directors = models.Director.objects.all()
    directors_list = []
    for index, director in enumerate(directors):
        director.text = director.text.replace("\r\n", "<br />")
        if index % 2 == 0:
            directors_list.append((1, director))
        else:
            directors_list.append((0, director))

    # what we do
    do_s = models.WhatWeDo.objects.all()
    return render(request, 'about.html',
                  {'directors': directors_list, 'do_s': do_s, 'about': about})


def news_view(request, category=None):
    categories = models.NewsCategory.objects.all()
    if category == None:
        all_news = Paginator(models.News.objects.all(), 15)
    else:
        all_news = Paginator(
            models.News.objects.filter(category__id=category), 15)
    all_news = all_news.get_page(request.GET.get('page'))
    return render(request, 'news.html',
                  {'all_news': all_news, 'categories': categories, 'category': category})


def news_details_view(request, nid):
    try:
        details = models.News.objects.get(id=nid)
    except models.News.DoesNotExist:
        return redirect(reverse('not_found'))
    if request.method == 'POST':
        comment = models.Comment(
            news=details,
            name=request.POST['name'],
            email=request.POST['email'],
            comment=request.POST['comment'].replace("\r\n", "<br />"))
        comment.save()
    return render(request, 'news_details.html', {'details': details})


def service_view(request):
    services = models.Service.objects.all()
    services_list = []
    for index, service in enumerate(services):
        services_list.append((index % 2 == 0, service))
    return render(request, 'service.html', {'services': services_list})


def subscribe_view(request):
    if request.method == 'POST' and 'email' in request.POST:
        try:
            models.NewsLetterSubscriber.objects.get(
                email=request.POST['email'])
        except models.NewsLetterSubscriber.DoesNotExist:
            subscriber = models.NewsLetterSubscriber(
                email=request.POST['email'])
            subscriber.save()
    return redirect(reverse('index'))


def gallery_view(request):
    photos = models.Gallery.objects.all()
    photos = Paginator(photos, 5)
    photos = photos.get_page(request.GET.get('page'))
    photos_list = []
    for i, img in enumerate(photos):
        photos_list.append((i % 2 == 0, img))
    return render(request, 'gallery.html', {'photos': photos_list})
