from django import forms 
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50,label='نام و نام خانوادگی')
    email = forms.EmailField(label='ایمیل شما')
    to = forms.EmailField(label='ارسال به')
    comments = forms.CharField(widget=forms.Textarea,label='متن')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','comment']

    
class SearchForm(forms.Form):
    query = forms.CharField(label='جستجو',max_length=100,widget=forms.TextInput(attrs={'class':'form-control rounded-0'}))