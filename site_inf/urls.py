from django.urls import path
from site_inf import views

app_name = 'site_inf'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),
    path('eventos/', views.eventos, name='eventos'),
    path('projetos/', views.projetos, name='projetos'),
    path('sistemas-informacao/', views.sistemas_info, name='sistemas_info'),
    path('ciencia-computacao/', views.ciencia_computacao, name='ciencia_computacao'),
    path('projetos/', views.projetos, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto_detail, name='projeto_detail'),
    path('forum/', views.forum, name='forum'),
    path('extensao/', views.extensao, name='extensao'),
    path('extensao/projetos/', views.extensao_projetos, name='extensao_projetos'),
    path('extensao/inscricoes/', views.extensao_inscricoes, name='extensao_inscricoes'),
    path('exalunos/adicionar-lote/', views.adicionar_exalunos_em_lote, name='adicionar_exalunos_lote'),
    path('exalunos/', views.mapa_ex_alunos, name='mapa_ex_alunos'),
    path('professores/', views.listar_professores, name='listar_professores'),
    path('empresas-parceiras/', views.empresas_parceiras, name='empresas_parceiras'),
    path('vagas/', views.listar_vagas, name='listar_vagas'),
    path('tccs-computacao/', views.tcc_computacao, name='tcc_computacao'),
    path('publicacoes/', views.pagina_publicacoes, name='publicacoes'),
    path('api/cadastrar-ex-aluno/', views.cadastrar_ex_aluno, name='api_cadastrar_ex_aluno'),
]
