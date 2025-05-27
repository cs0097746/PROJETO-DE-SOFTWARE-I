from django.contrib import admin
from .models import Evento, PostBlog, Projeto, ExAluno, Professor, EmpresaParceira, Vaga, TCC
from import_export.admin import ImportExportModelAdmin

admin.site.register(Evento)
admin.site.register(PostBlog)
admin.site.register(Projeto)
admin.site.register(TCC)

@admin.register(ExAluno)
class ExAlunoAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'curso', 'ano_conclusao', 'empresa_atual', 'cidade_atual', 'latitude', 'longitude')
    search_fields = ('nome', 'empresa_atual', 'cidade_atual')
    list_filter = ('curso', 'ano_conclusao')

@admin.register(Professor)
class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'email', 'area_atuacao')
    search_fields = ('nome', 'email', 'area_atuacao')

@admin.register(EmpresaParceira)
class EmpresaParceiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'destaque')
    search_fields = ('nome',)

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'tipo', 'data_publicacao', 'data_expiracao')
    search_fields = ('titulo', 'empresa__nome')
    list_filter = ('tipo', 'empresa')
    
