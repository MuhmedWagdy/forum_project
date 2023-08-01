from django.contrib import admin

# Register your models here.


from .models import Question,Answers

admin.site.register(Question)
admin.site.register(Answers)
