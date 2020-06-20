from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile,Queans,Article,Question

class ExtendedForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('photo','bio','acc_type')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','discription')

class ExtendedUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','bio')

class QueansForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    pdf = forms.FileField(required=False)
    class Meta:
        model = Queans
        fields = ('answer','photo','video','pdf')

class ArticleForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    pdf = forms.FileField(required=False)
    class Meta:
        model = Article
        fields = ('title','discription','photo','video','pdf')

class ArticleUpdateForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    pdf = forms.FileField(required=False)
    class Meta:
        model = Article
        fields = ('title','discription','photo','video','pdf')



