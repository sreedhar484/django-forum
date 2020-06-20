from django.urls import path,include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . views import ArticleBlogView

urlpatterns = [
    path('',views.home,name='home'),
    path('profile',views.profile,name="profile"),
    path('asq',views.asq,name='asq'),
    path('myq',views.myq,name='myq'),
    path('log',views.log,name='log'),
    path('<id>/stuhome',views.stuhome,name='stuhome'),
    path('seeque',views.seeque,name='seeque'),
    path('signup',views.register,name='signup'),
    path('acconts/',include('django.contrib.auth.urls')),
    path('acconts/logout',include('django.contrib.auth.urls')),
    path('allq',views.allq,name='allq'),
    path('quizform',views.quizform,name='quizform'),
    path('postar',views.postar,name='postar'),
    path('article',views.article,name='article'),
    path('myar',views.myar,name='myar'),
    path('search',views.search,name='search'),
    path('quiz',views.quiz,name='quiz'),
    path('python',views.pythonquiz,name='python'),
    path('java',views.javaquiz,name='java'),
    path('c',views.cquiz,name='c'),
    path('html',views.htmlquiz,name='html'),
    path('javascript',views.javascriptquiz,name='javascript'),
    path('quizprogress',views.quizprogress,name='quizprogress'),
    path('searchquestion',views.searchquestion,name='searchquestion'),
    #path('searchquestion',ArticleBlogView.as_view(),name='searchquestion'),
    path('viewanswer/<id>',views.viewanswer,name='viewanswer'),
    path('viewmyanswer/<id>',views.viewmyanswer,name='viewmyanswer'),
    path('articleview/<id>',views.articleview,name='articleview'),
    path('allarticleview/<id>',views.allarticleview,name='allarticleview'),
    path('seeprofile/<id>',views.seeprofile,name='seeprofile'),
    path('edit/<id>',views.articleupdate,name="articleupdate"),
    path('delete/<id>',views.articledelete,name="articledelete"),
    path('deleteq/<id>',views.questiondelete,name="questiondelete"),
    path('acconts/logoutlogin/password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    url(r'^(?P<id>\d+)/$',views.postans,name="postans")
]