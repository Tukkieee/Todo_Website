from django.contrib import admin
from .models import todo
# Register your models here.

class TodoAdmin (admin.ModelAdmin):
    list_display = ("user", "todo_name", "status")

admin.site.register(todo,TodoAdmin)