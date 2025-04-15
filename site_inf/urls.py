from site_inf.views import index, blog, projetos, eventos, post_detail, projeto_detail
from site_inf.views import sistemas_info ,ciencia_computacao
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

]
