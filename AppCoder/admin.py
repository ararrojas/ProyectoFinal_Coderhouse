from django.contrib import admin

# Register your models here.

from .models import Curso


@admin.register(Curso) # decorador 
class CursoAdmin(admin.ModelAdmin):
    pass