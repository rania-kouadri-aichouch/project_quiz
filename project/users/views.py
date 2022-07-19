from django.shortcuts import render
from quiz.models import Result

# Create your views here.
def users(request):    
    if request.user.is_superuser:
        results=Result.objects.all()
        context = {
            'results':results
        }
        
        return render(request,'users.html',context)
    else: 
        return redirect('home') 