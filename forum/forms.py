

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Question,Answers






class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # fields ='__all__'
        exclude =('Author',)
        widgets = {
            'content': SummernoteWidget(),
          
        }




class AnswersForm(forms.ModelForm):

    class Meta:
        model = Answers
        # fields ='__all__'
        exclude =('Author',)






