from django.shortcuts import render, redirect
from papp.forms import TaskForm
from papp.models import TaskAddModel
# Create your views here.
def home(request):
    return render(request, 'home.html')




def addtask(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('Show')
    else:
        task = TaskForm()
    return render(request, 'add_task.html', {'form': task})



from django.shortcuts import render
from .models import TaskAddModel




def showtask(request):
    task = TaskAddModel.objects.exclude(is_completed = True)
    print(task)
    return render(request, 'show_task.html',{'data':task})




def deletetask(request, id):
    task = TaskAddModel.objects.get(pk = id).delete()
    return redirect('Show')

 

 
    
def edittask(request, id):
    task = TaskAddModel.objects.get(pk = id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Show')  
    return render(request, 'add_task.html', {'form':form})




def completetask(request, id): 
    completed_task = TaskAddModel.objects.get(pk=id)
    completed_task.is_completed = True
    completed_task.save()
    #completed_task.is_completed = completed_task.status
    status = completed_task.status
    all_completed_tasks = TaskAddModel.objects.filter(is_completed=True)
    return render(request, 'complete_task.html', {'data': all_completed_tasks, 'status':status})






