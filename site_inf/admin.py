from django.contrib import admin
from .models import Evento, PostBlog, Projeto, ExAluno, Professor
from import_export.admin import ImportExportModelAdmin

admin.site.register(Evento)
admin.site.register(PostBlog)
admin.site.register(Projeto)

@admin.register(ExAluno)
class ExAlunoAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'curso', 'ano_conclusao')
    search_fields = ('nome',)
    list_filter = ('curso', 'ano_conclusao')

@admin.register(Professor)
class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'email', 'area_atuacao')
    search_fields = ('nome', 'email', 'area_atuacao')