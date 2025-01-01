from django.contrib import admin
from .models import Post,Comment,Contact
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','category','postname','time']
    list_filter = ['user','category']
    search_fields = ['user','postname','category']
    ordering = ['user','category']

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ['id','post','view','client_ip','path']
    list_filter = ['post']
    search_fields = ['post']
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','time']
    list_filter = ['user','post']
    search_fields = ['user','post']
    ordering = ['time']

@admin.register(Contact)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'
