from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def addQuestion(request):    
    if request.user.is_superuser:
        form=Questionform()
        if(request.method=='POST'):
            form=Questionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addqst.html',context)
    else: 
        return redirect('home') 



def quiz(request):
    if request.method == 'POST':
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        all_questions =[]
        all_ans=[]
        
        
        for q in questions:
            total+=1
            all_questions.append(q.question)
            all_ans.append(q.answer)

            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1

        qst=all_questions
        ans=all_ans        
        context = {
            'score':score,
            'qst':qst,
            'ans':ans,
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        result = Result(user=request.user, score=score,correct=correct, wrong=wrong, total=total)
        result.save()
        return render(request,'results.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz.html',context)



def edit(request, id):  
    question = Question.objects.get(id=id)   
    return render(request,'edit.html', {'question': question}) 

def update(request, id):  
    question = Question.objects.get(id=id)  
    form = Questionform(request.POST, instance = question)  
    if form.is_valid():  
        form.save()  
        return redirect("/quiz/quiz/")  
    return render(request, 'edit.html', {'question': question})  

  
def destroy(request, id):  
    question = Question.objects.get(id=id)  
    question.delete()  
    return redirect("/quiz/quiz/")  