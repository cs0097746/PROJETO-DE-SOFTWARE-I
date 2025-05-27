from site_inf.views import index, blog, projetos, eventos, post_detail, projeto_detail, forum, extensao, extensao_inscricoes, extensao_projetos, tcc_computacao, mapa_ex_alunos
from site_inf.views import sistemas_info ,ciencia_computacao, adicionar_exalunos_em_lote, listar_exalunos
from site_inf.views import listar_professores, empresas_parceiras, listar_vagas
from django.urls import path


app_name = 'site_inf'


urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    #path('contato/', contato, name='contato'),
    path('eventos/', eventos, name='eventos'),
    path('projetos/', projetos, name='projetos'),
    path('sistemas-informacao/', sistemas_info, name='sistemas_info'),
    path('ciencia-computacao/', ciencia_computacao, name='ciencia_computacao'),
    path('projetos/', projetos, name='projetos'),
    path('projetos/<int:projeto_id>/', projeto_detail, name='projeto_detail'),
    path('forum/', forum, name='forum'),
    path('extensao/', extensao, name='extensao'),
    path('extensao/projetos/', extensao_projetos, name='extensao_projetos'),
    path('extensao/inscricoes/', extensao_inscricoes, name='extensao_inscricoes'),
    path('exalunos/adicionar-lote/', adicionar_exalunos_em_lote, name='adicionar_exalunos_lote'),
    path('exalunos/', mapa_ex_alunos, name='mapa_ex_alunos'),
    path('professores/', listar_professores, name='listar_professores'),
    path('empresas-parceiras/', empresas_parceiras, name='empresas_parceiras'),
    path('vagas/', listar_vagas, name='listar_vagas'),
    path('tccs-computacao/', tcc_computacao, name='tcc_computacao'),
]
