from django.contrib import admin  # admin side
from .models import Post, Tag, Support # import Post from models

# Register your models here.


class PostAdmin(admin.ModelAdmin):  # edit field in admin site
    list_display = ('post_name', 'pub_date', 'contact_information')  # display post_name, date, and contact
    list_filter = ['pub_date']  # filters through pub_date
    fieldsets = [  # fields in the admin site that is separated
        ('Image of Product', {'fields': ['image']}),
        ('Product information', {'fields': ['post_name', 'item', 'description', 'creator.email']}),
        ('Price $', {'fields': ['price']}),
        ('Dorm location', {'fields': ['contact_information']}),
        ('Categories', {'fields': ['tags']}),
    ]


admin.site.register(Post, PostAdmin)  # register changes and database to the admin
admin.site.register(Tag)  # register Tag model in admin page
admin.site.register(Support)  # register Support model in admin page
