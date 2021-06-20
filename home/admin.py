from django.contrib import admin
from django.utils.html import format_html
from . import models


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_time']
    search_fields = ['name', 'email', 'meessage']
    list_filter = ['date_time']
    readonly_fields = ['name', 'email', 'date_time', 'message']

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_change_permission(self, *args, **kwargs):
        return False


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date_time']
    list_filter = ['date_time']
    search_fields = ['subject', 'text', 'date_time']

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return False


class DirectorAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.image.url}' style='width: 240px; height: 320px; object-fit: scale-down;' />")

    list_display = ['name', 'role']
    fields = ['thumbnail', 'image', ('name', 'role'), 'text']
    readonly_fields = ['thumbnail']


class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ['header', 'text']


class AboutUsAdmin(admin.ModelAdmin):
    def cover_thumb(self, obj):
        return format_html(f"<img src='{obj.about_cover.url}' style='width: 480px; height: 240px; object-fit: scale-down;' />")

    def image_thumb(self, obj):
        return format_html(f"<img src='{obj.about_image.url}' style='width: 240px; height: 240px; object-fit: scale-down' />")

    list_display = ['about_text']
    fields = [('cover_thumb', 'image_thumb'),
              'about_cover', 'about_image', 'about_text']
    readonly_fields = ['cover_thumb', 'image_thumb']

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


class NewsInlines(admin.TabularInline):
    def goto_news_details(self, obj):
        return format_html(f"<a href='/admin/home/news/{obj.id}/change/'>Details</a>")

    model = models.News
    fields = ['title', 'post_by', 'goto_news_details']
    readonly_fields = ['title', 'post_by', 'goto_news_details']
    extra = 0

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [NewsInlines]


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0
    fields = [('name', 'email', 'date_time'), 'comment']
    readonly_fields = ['date_time']


class NewsAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src='{obj.image.url}' style='width: 240px; height: 240px; object-fit: scale-down;' />")

    list_display = ['title', 'category', 'date']
    list_filter = ['category', 'date']
    search_field = ['title']
    fields = ['thumbnail', 'title',
              ('post_by', 'date'), ('image', 'category'), 'body', 'embedded', 'reference']
    readonly_fields = ['thumbnail', ]
    inlines = [CommentInline]


class ServicePointInline(admin.TabularInline):
    model = models.ServicePoint
    fields = ['text']
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro']
    search_field = ['name', 'intro']
    inlines = [ServicePointInline]


class GalleryAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if(obj.media_type == '0'):
            return format_html(f"<img src='{obj.image.url}' style='width: 240px; height: 240px; object-fit: scale-down;' />")
        else:
            return format_html(f"<video width='320' height='240' controls ><source src='{obj.image.url}' type='video/mp4' >Your browser does not support the video tag.</video >")

    list_display = ['media_type', 'thumbnail', 'caption']
    fields = ['thumbnail', 'image', 'media_type', 'caption']
    readonly_fields = ['thumbnail']


admin.site.register(models.ContactUs, ContactUsAdmin)
admin.site.register(models.NewsLetterSubscriber, NewsLetterSubscriberAdmin)
admin.site.register(models.NewsLetter, NewsLetterAdmin)
admin.site.register(models.Director, DirectorAdmin)
admin.site.register(models.WhatWeDo, WhatWeDoAdmin)
admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsCategory, NewsCategoryAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Gallery, GalleryAdmin)
