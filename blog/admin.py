from django.contrib import admin
from .models import Category,Tag,Post,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    list_per_page = 10

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    list_per_page = 10 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author',]
    list_filter = ['created_at']
    search_fields = ['title','content']
    raw_id_fields = ['author',]
    list_per_page = 10 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created_at','active']
    list_filter = ['active','created_at']
    search_fields = ['name','email','comment']
    list_editable = ['active',]
    list_per_page = 10
