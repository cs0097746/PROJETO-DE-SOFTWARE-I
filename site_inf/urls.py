from site_inf.views import index, cursos, blog, projetos, eventos, post_detail
from django.urls import path


app_name = 'site_inf'


urlpatterns = [
    path('', index, name='index'),
    path('cursos/', cursos, name='cursos'),
    path('blog/', blog, name='blog'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),
    #path('contato/', contato, name='contato'),
    path('eventos/', eventos, name='eventos'),
    path('projetos/', projetos, name='projetos'),
]
