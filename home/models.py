from django.db import models
from django.contrib.auth.models import User


class NewsCategory(models.Model):
    name = models.CharField(max_length=1000, default='', null=False)

    class Meta:
        verbose_name = 'News Category'
        verbose_name = 'News Categories'

    def __str__(self):
        return self.name

    def get_news(self):
        return News.objects.filter(category=self)


class News(models.Model):
    category = models.ForeignKey(
        NewsCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=1000, default='', null=False)
    date = models.DateField(null=True)
    image = models.ImageField(upload_to="news_images/", null=True, blank=False)
    heading = models.CharField(max_length=1000, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    post_by = models.CharField(max_length=100, default="", null=False)
    embedded = models.TextField(
        null=True, blank=True, help_text="YouTube video or Facebook Post or Google Map (optional)")
    reference = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-date', '-id']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return Comment.objects.filter(news=self)

    @property
    def total_comments(self):
        return len(self.get_comments)


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="", null=False)
    email = models.EmailField(null=True, blank=False)
    comment = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=200, null=False, default='')
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(verbose_name='Message')
    date_time = models.DateTimeField(
        verbose_name='Date and time', auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name


class NewsLetterSubscriber(models.Model):
    email = models.EmailField(
        verbose_name='Subscriber\'s Email', null=False, default='')


class NewsLetter(models.Model):
    subject = models.CharField(verbose_name='Subject', default='', null=False, max_length=300,
                               help_text='Subject of the newsletter. Can\'t be more than 300 characters.')
    text = models.TextField(verbose_name='Text')
    date_time = models.DateTimeField(
        verbose_name='Send Date Time', auto_now_add=True)

    def save(self, *args, **kwargs):
        emails = NewsLetterSubscriber.objects.all().values_list('email', flat=True)
        send_mail(self.subject, self.text, settings.SERVER_EMAIL, emails)
        super(NewsLetter, self).save(*args, **kwargs)


class AboutUs(models.Model):
    about_cover = models.ImageField(upload_to="about_img/", null=True)
    about_image = models.ImageField(upload_to="about_img/", null=True)
    about_text = models.TextField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class Director(models.Model):
    image = models.ImageField(upload_to="director/", null=True)
    name = models.CharField(max_length=200, default='', null=False)
    role = models.CharField(max_length=500, default='', null=False)
    text = models.TextField()


class WhatWeDo(models.Model):
    header = models.CharField(max_length=200, default='', null=False)
    text = models.TextField(max_length=500, default="", null=False)

    class Meta:
        verbose_name = 'What we do'
        verbose_name_plural = 'What we do'


class Service(models.Model):
    name = models.CharField(max_length=200, default="", null=False)
    intro = models.TextField()
    image = models.ImageField(upload_to="service_image/", null=True)

    def __str__(self):
        return self.name

    @property
    def get_points(self):
        return ServicePoint.objects.filter(service=self)


class ServicePoint(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, default='', null=False)


class Gallery(models.Model):
    image = models.FileField(upload_to='gallery/')
    caption = models.CharField(max_length=200, default='', null=False)
    media_type = models.CharField(max_length=1, default='0', choices=[
                                  ('0', 'Image'), ('1', 'Video')], null=False)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
