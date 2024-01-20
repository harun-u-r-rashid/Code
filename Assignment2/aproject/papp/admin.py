from django.contrib import admin
from papp.models import TaskAddModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
  
admin.site.register(TaskAddModel, TaskModelAdmin)



