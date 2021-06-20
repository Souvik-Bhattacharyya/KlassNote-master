from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name='index'),
    path("about/", views.about_view, name="about"),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('contact/', views.contact_view, name='contact'),
    path("news/", views.news_view, name='news'),
    path("news/<int:category>/", views.news_view, name="news_category"),
    path("news_details/<int:nid>/", views.news_details_view, name="news_details"),
    path("service/", views.service_view, name="service"),
    path("gallery/", views.gallery_view, name="gallery")
]
