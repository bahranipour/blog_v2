from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Tag,Category
from .forms import CommentForm,SearchForm,EmailPostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q,Count
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail


def about(request):
    return render(request,'blog/about.html')

def post_list(request,category_id=None):
 
    post_list = Post.objects.all().order_by('-created_at')
    query = request.GET.get('query')
    category = None 
    if category_id:
        category = get_object_or_404(Category,id=category_id)
        post_list = Post.objects.filter(category=category).order_by('-created_at')

    

    if query:
        post_list = post_list.filter(Q(title__icontains=query)|Q(content__icontains=query))

    
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    search_form = SearchForm(request.GET)

    context = {
        'posts':posts,
        'search_form':search_form,
        'category':category
        
    }

    return render(request,'blog/post_list.html',context)

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    comments = post.comments.filter(active=True)

    post_tags_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,'نظر شما با موفقیت ثبت و پس از تایید قابل مشاهده خواهد بود')
            return redirect('blog:post_detail',id=post.id)
    else:
        form = CommentForm()

    context = {
        'post':post,
        'comments':comments,
        'form':form, 
        'similar_posts':similar_posts,
    }

    return render(request,'blog/post_detail.html',context)



def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    sent = False 

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(reverse('blog:post_detail',args=[post.id]))
            send_mail(f'{cd["name"]} ({cd["email"]}) recommends you read this post',post_url,'admin@gmail.com',[cd['to']])
            sent=True
            if sent == True:
                messages.success(request,'ایمیل با موفقیت ارسال شد')
                return redirect('blog:post_detail',id=post.id)
            else: 
                messages.error(request,'خطا! ایمیل ارسال نشد')
                return redirect('blog:post_detail',id=post.id)
    else:
        form = EmailPostForm()

    context = {
        'post':post,
        'form':form,
    }

    return render(request,'blog/post_share.html',context)


def post_by_tag(request,tag_id):
    tag = get_object_or_404(Tag,id=tag_id)
    post_list = Post.objects.filter(tags=tag).order_by('-created_at')


 
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    search_form = SearchForm(request.GET)

    context = {
        'tag':tag,
        'posts':posts,
       
    }

    return render(request,'blog/post_by_tag.html',context)






