from django.shortcuts import render,redirect
from .models import Todolist
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_items=Todolist.objects.order_by('id')
    context={'todo_items':todo_items}
    return render(request,"dolist/index.html",context)


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Todolist.objects.create(text=text, completed=False)
            return redirect('index')  
    else:
        form = TodoForm()
    
    return render(request, 'dolist/index.html', {'form': form})



def delete_all(request):
    # Delete all to-do items from the database
    Todolist.objects.all().delete()
    return redirect('index')  


def delete_completed(request):
    # Delete all completed to-do items from the database
    Todolist.objects.filter(completed=True).delete()
    return redirect('index')  