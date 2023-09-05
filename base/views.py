from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.
# this is function based view
# def taskList(request):
#   return HttpResponse('To do list')

# This view by default looks for a template named <model>_list.html
# We can override this by using the variable template_name.
# By default this views sends object_list as the query set to the template. We can override this by setting 'context_object_name' as we are doing here.
class TaskList(ListView):
  model = Task
  context_object_name = 'tasks'

# This view by default looks for a template named <model>_detail.html.
# We can override this by using the variable template_name.
class TaskDetail(DetailView):
  model = Task
  context_object_name = 'task'
  template_name = 'base/task.html'

# This view by default looks for a template named <model>_form.html.
class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = reverse_lazy('tasks')

# This view by default looks for a template named <model>_form.html.
class TaskUpdate(UpdateView):
  model = Task
  fields = "__all__"
  success_url = reverse_lazy('tasks')

# This view by default looks for a template named <model>_confirm_delete.html.
class TaskDelete(DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')
