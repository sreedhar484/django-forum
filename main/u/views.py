from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import ProfileForm,ExtendedForm,ExtendedUpdateForm,ProfileUpdateForm,QueansForm,ArticleForm,ArticleUpdateForm,QuestionForm
from . models import Question,Queans,Article,Posts,Slide,Quiz,Quizres,java,javascript,c,html,python,Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter,SearchFilter
from . serializers import ArticlePostView
import random

# Create your views here.
def home(request):
    post = Posts.objects.all()
    slide = Slide.objects.all()
    return render(request,'home.html',{'posts':post,'slide':slide})

def stuhome(request,id):
    return redirect('log')
def register(request):
    if request.method =='POST':
        email = request.POST['email']
        form = ExtendedForm(request.POST)
        user_profile = ProfileForm(request.POST,request.FILES)
        if form.is_valid() and user_profile.is_valid():
            try:
                send_mail('thanks for register','your registration has been successfully complted','sreedharr484@gmail.com',[email])
                user = form.save()
                profile = user_profile.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('/')
            except:
                messages.info(request,'invalid mail')
                return redirect('signup')
        else:
            messages.info(request,'invalid details')
            return redirect('signup')
    else:
        form = ExtendedForm()
        user_profile = ProfileForm()
        return render(request,'register.html',{'form':form,'form1':user_profile})

def log(request):
    return render(request,'profile.html')
def profile(request):
    if request.method=='POST':
        form = ExtendedUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('log')
        else:
            return redirect('profile')
    else:
        form = ExtendedUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request,'profile_update.html',{'form':form,'form1':profile_form})

def asq(request):
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username=request.user
            instance.save()
            number_of_que = request.user.profile.noque
            number_of_que+=1
            profile = Profile.objects.get(user=request.user.id)
            profile.noque=number_of_que
            profile.save()
            return redirect('log')
        else:
            return redirect('asq')
    else:
        form = QuestionForm()
        return render(request,'asq.html',{'form':form})

def myq(request):
    que = Question.objects.all()
    ans = Queans.objects.all()
    name = User.objects.all()
    que = [i for i in que]
    que = sorted(que,key=lambda x:x.id,reverse=True)
    return render(request,'myquestion.html',{'que':que,'ans':ans,'name':name})

def seeque(request):
    if request.method=='POST':
        question = request.POST['srh']
        name = User.objects.all()
        count = Question.objects.count()
        allquestion = Question.objects.all()
        key_words=[i for i in word_tokenize(question) if not i in stopwords.words('english')]
        l2 = list(allquestion)
        l1 =[i.question for i in allquestion]
        l=[word_tokenize(j) for j in l1]
        key_words_in_list=[[j for j in i if not j in stopwords.words('english')] for i in l]
        c=0
        d=[]
        for i in range(len(key_words_in_list)):
            for j in key_words:
                if j in key_words_in_list[i]:
                    c+=1
            d1=[l2[i],c]
            d.append(d1)
            c=0
        finallist =[i[0] for i in sorted(d,key=lambda x:x[1],reverse=True) if i[1]>0]
        str1 = 'showing results for "{}"'.format(question)
        return render(request,'seeque.html',{'data':finallist,'image':name,'str1':str1,'count':count,'question':question})
    else:
        que = Question.objects.all()
        image = User.objects.all()
        count = Question.objects.count()
        que = [i for i in que]
        que = sorted(que,key=lambda x:x.id,reverse=True)
        return render(request,'seeque.html',{'data':que,'image':image,'count':count})

def postans(request,id):
    if request.method=='POST':
        form = QueansForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            que = Question.objects.get(id=id)
            instance.question = que
            instance.save()
            number_of_answers = request.user.profile.noans
            number_of_answers+=1
            profile = Profile.objects.get(user=request.user.id)
            profile.noans=number_of_answers
            profile.save()
            answer = request.POST['answer']
            email1 = User.objects.get(id=que.username_id)
            email = email1.email
            msg = que.question+' has another answer by '+request.user.username+' and the answer is '+answer
            send_mail('one answer is posted to your question',msg,'sreedharr484@gmail.com',[email])
            return redirect('log')
        else:
            return redirect('postans')
    else:
        que = Question.objects.get(id=id)
        form = QueansForm()
        return render(request,'postans.html',{'form':form,'que':que})

def allq(request):
    if request.method=='POST':
        question = request.POST['srh']
        name = User.objects.all()
        count = Question.objects.count()
        allquestion = Question.objects.all()
        key_words=[i for i in word_tokenize(question) if not i in stopwords.words('english')]
        l2 = list(allquestion)
        l1 =[i.question for i in allquestion]
        l=[word_tokenize(j) for j in l1]
        key_words_in_list=[[j for j in i if not j in stopwords.words('english')] for i in l]
        c=0
        d=[]
        for i in range(len(key_words_in_list)):
            for j in key_words:
                if j in key_words_in_list[i]:
                    c+=1
            d1=[l2[i],c]
            d.append(d1)
            c=0
        finallist =[i[0] for i in sorted(d,key=lambda x:x[1],reverse=True) if i[1]>0]
        str1 = 'showing results for "{}"'.format(question)
        return render(request,'allq.html',{'que':finallist,'name':name,'str1':str1,'count':count,'question':question})
    else:
        que = Question.objects.all()
        count = Question.objects.count()
        name = User.objects.all()
        que = [i for i in que]
        que = sorted(que,key=lambda x:x.id,reverse=True)
        return render(request,'allq.html',{'que':que,'name':name,'count':count})

def seeprofile(request,id):
    profile = User.objects.get(username=id)
    return render(request,'seeprofile.html',{'pro':profile})

def postar(request):
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username=request.user
            instance.save()
            messages.info(request,'your article has been successfully posted')
            number_of_posts = request.user.profile.noposts
            number_of_posts+=1
            profile = Profile.objects.get(user=request.user.id)
            profile.noposts=number_of_posts
            profile.save()
            return redirect('postar')
        else:
            messages.info(request,'your article has been failed to submit')
            return redirect('postar')
    else:
        form = ArticleForm()
        return render(request,'postarticle.html',{'form':form})
def article(request):
    if request.method=='POST':
        question = request.POST['srh']
        name = User.objects.all()
        count = Article.objects.count()
        allquestion = Article.objects.all()
        key_words=[i for i in word_tokenize(question) if not i in stopwords.words('english')]
        l2 = list(allquestion)
        l1 =[i.discription for i in allquestion]
        l=[word_tokenize(j) for j in l1]
        key_words_in_list=[[j for j in i if not j in stopwords.words('english')] for i in l]
        c=0
        d=[]
        for i in range(len(key_words_in_list)):
            for j in key_words:
                if j in key_words_in_list[i]:
                    c+=1
            d1=[l2[i],c]
            d.append(d1)
            c=0
        finallist =[i[0] for i in sorted(d,key=lambda x:x[1],reverse=True) if i[1]>0]
        str1 = 'showing results for "{}"'.format(question)
        return render(request,'article.html',{'name':finallist,'data':name,'count':count,'str1':str1,'question':question}) 
    else:
        name = Article.objects.all()
        count = Article.objects.count()
        data = User.objects.all()
        name = [i for i in name]
        name = sorted(name,key=lambda x:x.id,reverse=True)
        return render(request,'article.html',{'name':name,'data':data,'count':count})
def myar(request):
    name = Article.objects.all()
    data = User.objects.all()
    name = [i for i in name]
    name = sorted(name,key=lambda x:x.id,reverse=True)
    return render(request, 'myartcle.html', {'name': name, 'data': data})

def articleupdate(request,id):
    title = Article.objects.get(id=id)
    if request.method=='POST':
        form = ArticleUpdateForm(request.POST,request.FILES,instance=title)
        if form.is_valid():
            form.save()
            return redirect('myar')
        else:
            return redirect(id)
    else:
        form = ArticleUpdateForm(instance=title)
        return render(request,'article_update.html',{'form':form})

def articledelete(request,id):
    instance = Article.objects.get(id=id)
    instance.delete()
    return redirect('myar')

def articleview(request,id):
    name = Article.objects.get(id=id)
    art = Article.objects.all()
    return render(request,'articleview.html',{'data':art,'name':name})

def allarticleview(request,id):
    name = Article.objects.get(id=id)
    number_of_view = name.view
    number_of_view+=1
    name.view = number_of_view
    name.save()
    name = Article.objects.get(id=id)
    art = Article.objects.all()
    return render(request,'allarticleview.html',{'data':art,'name':name})

def viewanswer(request,id):
    que = Question.objects.get(id=id)
    ans = Queans.objects.all()
    name = User.objects.all()
    return render(request,'viewanswer.html',{'que':que,'ans':ans,'name':name})

def viewmyanswer(request,id):
    que = Question.objects.get(id=id)
    ans = Queans.objects.all()
    name = User.objects.all()
    return render(request,'myq.html',{'que':que,'ans':ans,'name':name})

def questiondelete(request,id):
    instance = Question.objects.get(id=id)
    instance.delete()
    return redirect('myq')

def search(request):
    word = request.POST['srh']
    try:
        instance = User.objects.get(username=word)
        return render(request,'seeprofile.html',{'pro':instance})
    except:
        messages.info(request,'invalid username')
        return redirect('log')

def quiz(request):
    quiz = Quiz.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'general'
    count = Quiz.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def pythonquiz(request):
    quiz = python.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'python'
    count = python.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def javaquiz(request):
    quiz = java.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'java'
    count = java.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def cquiz(request):
    quiz = c.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'c programming'
    count = c.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def htmlquiz(request):
    quiz = html.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'html'
    count = html.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def javascriptquiz(request):
    quiz = javascript.objects.all()
    quiz = [i for i in quiz]
    random.shuffle(quiz)
    subject = 'javascript'
    count = javascript.objects.count()
    return render(request,'quiz.html',{'quiz':quiz,'sub':subject,'count':count})

def quizform(request):
    score = request.POST['score']
    subject = request.POST['subject']
    count = request.POST['count']
    form = Quizres(username=request.user,score=score,subject=subject,total=count)
    form.save()
    return redirect('quizprogress')

def quizprogress(request):
    name = request.user.id
    res=Quizres.objects.all()
    l=[0,0,0,0,0,0]
    l2=[0,0,0,0,0,0]
    l1=['general','python','java','c programming','html','javascript']
    for i in range(6):
        for j in res:
            if j.username_id==name:
                if l1[i]==j.subject:
                    l[i]=int(j.score)
    for i in range(6):
        for j in res:
            if j.username_id==name:
                if l1[i]==j.subject and l2[i]<int(j.score):
                    l2[i]=int(j.score)
    return render(request,'quiz_progress.html',{'res':res,'data':l,'data1':l2})

def searchquestion(request):
    question = request.POST['srh']
    name = User.objects.all()
    allquestion = Question.objects.all()
    key_words=[i for i in word_tokenize(question) if not i in stopwords.words('english')]
    l2 = list(allquestion)
    l1 =[i.question for i in allquestion]
    l=[word_tokenize(j) for j in l1]
    key_words_in_list=[[j for j in i if not j in stopwords.words('english')] for i in l]
    c=0
    d=[]
    for i in range(len(key_words_in_list)):
        for j in key_words:
            if j in key_words_in_list[i]:
                c+=1
        d1=[l2[i],c]
        d.append(d1)
        c=0
    finallist =[i[0] for i in sorted(d,key=lambda x:x[1],reverse=True) if i[1]>0]
    return render(request,'searchresult.html',{'data':finallist,'name':name})


class ArticleBlogView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlePostView
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','discription','username__username')

    
        

