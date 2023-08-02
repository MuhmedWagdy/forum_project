

from django import forms

from .models import Question,Answers





class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # fields ='__all__'
        exclude =('Author',)




class AnswersForm(forms.ModelForm):

    class Meta:
        model = Answers
        # fields ='__all__'
        exclude =('Author',)






