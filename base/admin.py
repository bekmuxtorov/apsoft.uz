from django.contrib import admin
from .models import Client, Contact
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_at', 'view_image')
    list_filter = ('name', 'added_at')
    search_fields = ('name', 'added_at')

    def view_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width=50px height=50px />')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'email', 'added_at')
    search_fields = ('full_name', 'subject', 'email', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Client, TranslatableAdmin)
