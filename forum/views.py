from django.shortcuts import render,redirect
# Create your views here.
from .models import Question,Answers
from .forms import QuestionForm,AnswersForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView



def list_question(request):
    data = Question.objects.all()
    return render(request,'list_question.html',{'question':data})

class QuestionList(ListView):
   model = Question

# ----------------------------------------------------------------------------------------------------------------------------------

def list_answer(request):
    data = Answers.objects.all()
    return render(request,'list_answer.html',{'answer':data})


class ListAnswer(ListView):
   model = Answers

# -----------------------------------------------------------------------------------------------------------------------------------------------
# fbv   ----- cbv
def ques_detail(request,que_id):
    data = Question.objects.get(id=que_id)
    return render(request,'quest_detail.html',{'question':data})


class DetailQuest(DetailView):
   model = Question

# ---------------------------------------------------------------------------------------------------------------------------------------------
def answer_detail(request,ansr_id):
    data = Answers.objects.get(id=ansr_id)
    return render(request,'answer_detail.html',{'answer':data})


class DetailAnswer(DetailView):
   model = Answers
# --------------------------------------------------------------------------------------------------------------------------------------------

def new_quest(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
           
           myform = form.save(commit=False)
           myform.Author = request.user
           myform.save()
           return redirect('/quest')

    else:
      form = QuestionForm()
    return render(request,'new_quest.html',{'form':form})

class QuestionCreate(CreateView):
   
   model = Question
   fields =  ['Author','question','tags','created_at','Content']
   success_url=('/quest')

# -----------------------------------------------------------------------------------------------------------------------------------------------------

def edit_quest(request,que_id):
    data = Question.objects.get(id=que_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
           
           myform = form.save(commit=False)
           myform.Author = request.user
           myform.save()
           return redirect('/quest')

    else:
      form = QuestionForm(instance=data)
    return render(request,'edit_quest.html',{'form':form})


class UpdateQuest(UpdateView):
   model = Question
   fields =  ['Author','question','tags','created_at','Content']
   success_url=('/quest')
   template_name = 'forum/edit_quest.html'

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_ques(request,que_id):
    data = Question.objects.get(id=que_id)
    data.delete()
    return redirect('/quest')

class DeleteQuest(DeleteView):
   model = Question
   success_url=('/quest')


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def new_answer(request):

    if request.method == 'POST':
        form = AnswersForm(request.POST,request.FILES)
        if form.is_valid():
           
           myform = form.save(commit=False)
           myform.Author = request.user
           myform.save()
           return redirect('/answer')

    else:
      form = QuestionForm()
    return render(request,'new_answer.html',{'form':form})


class AnswerCreate(CreateView):
   model = Answers
   fields =  ['Author','Answer','question','created_at']

   success_url=('/answer')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
def edit_answer(request,ansr_id):
    data = Answers.objects.get(id=ansr_id)
    if request.method == 'POST':
        form = AnswersForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
           
           myform = form.save(commit=False)
           myform.Author = request.user
           myform.save()
           return redirect('/answer')

    else:
      form = AnswersForm(instance=data)
    return render(request,'edit_answer.html',{'form':form})


class AnswerUpdate(UpdateView):
   model = Answers
   fields =  ['Author','Answer','question','created_at']

   success_url=('/answer')
   template_name = 'forum/edit_answer.html'



    
def delete_answer(request,ansr_id):
    data = Answers.objects.get(id=ansr_id)
    data.delete()
    return redirect('/answer')


class DeleteAnswer(DeleteView):
   model = Answers
   success_url=('/answer')
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------










    






