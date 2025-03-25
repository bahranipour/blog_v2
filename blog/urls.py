from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('category/<int:category_id>/',views.post_list,name='post_by_category'),
    path('detail/<int:id>/',views.post_detail,name='post_detail'),
    path('tag/<int:tag_id>/',views.post_by_tag,name='post_by_tag'),
    path('share/<int:post_id>/',views.post_share,name='post_share'),
    path('about/',views.about,name='about'),
]