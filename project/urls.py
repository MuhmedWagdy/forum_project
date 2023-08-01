"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from forum.views import list_question,list_answer,ques_detail,answer_detail,new_quest,new_answer,edit_quest,edit_answer,delete_ques,delete_answer,QuestionList,ListAnswer,DetailQuest,DetailAnswer,QuestionCreate,AnswerCreate,UpdateQuest,AnswerUpdate,DeleteQuest,DeleteAnswer


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('quest/',list_question),
    # path('quest/<int:que_id>',ques_detail),
    # path('answer/<int:ansr_id>',answer_detail),
    # path('answer/',list_answer),

    # path('answer/new',new_answer),
    # path('quest/new',new_quest),
    # path('quest/<int:que_id>/edit',edit_quest),
    # path('answer/<int:ansr_id>/edit',edit_answer),

    # path('quest/<int:que_id>/delete',delete_ques),
    # path('answer/<int:que_id>/delete',delete_answer),
    path('quest/',QuestionList.as_view()),
    path('answer/',ListAnswer.as_view()),

    path('quest/<int:pk>',DetailQuest.as_view()),
    path('answer/<int:pk>',DetailAnswer.as_view()),
    path('quest/new',QuestionCreate.as_view()),
    path('answer/new',AnswerCreate.as_view()),

    path('quest/<int:pk>/edit',UpdateQuest.as_view()),
    path('answer/<int:pk>/edit',AnswerUpdate.as_view()),
    path('quest/<int:pk>/delete',DeleteQuest.as_view()),
    path('answer/<int:pk>/delete',DeleteAnswer.as_view()),

  
  
]


  
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

