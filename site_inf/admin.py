from django.contrib import admin
from .models import Evento, PostBlog, Projeto, ExAluno, Professor
from .models import Publicacao, EmpresaParceira, Vaga, TCC
from import_export.admin import ImportExportModelAdmin

admin.site.register(Evento)
admin.site.register(PostBlog)
admin.site.register(Projeto)
admin.site.register(TCC)

@admin.register(ExAluno)
class ExAlunoAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'curso', 'ano_conclusao', 'empresa_atual', 'latitude', 'longitude', 'linkedin')
    search_fields = ('nome', 'empresa_atual')
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

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'evento_ou_revista', 'autores_resumidos')
    list_filter = ('ano', 'evento_ou_revista')
    search_fields = ('titulo', 'autores', 'evento_ou_revista')
    ordering = ('-ano', 'titulo')

    def autores_resumidos(self, obj):
        if len(obj.autores) > 80:
            return obj.autores[:77] + "..."
        return obj.autores
    autores_resumidos.short_description = 'Autores'
    
