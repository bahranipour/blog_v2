from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته ها'


    def __str__(self):
        return self.title 
    

class Tag(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='عنوان')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title 
    

class Post(models.Model):
    image = models.ImageField(upload_to='post_img/',null=True,blank=True,verbose_name='تصویر')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='دسته')
    tags = models.ManyToManyField(Tag,blank=True,verbose_name='برچسب ها')
    title = models.CharField(max_length=100,verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='بروزرسانی شده')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title 
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',verbose_name='پست')
    name = models.CharField(max_length=100,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    comment = models.TextField(verbose_name='نظر')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')
    active = models.BooleanField(default=False,verbose_name='فعال')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name 

