from site_inf.views import index, cursos, blog, contato, projetos, eventos
from django.urls import path

app_name = 'site_inf'

urlpatterns = [
    path('', index, name='index'),
    path('cursos/', cursos, name='cursos'),
    path('blog/', blog, name='blog'),
    path('contato/', contato, name='contato'),
    path('eventos/', eventos, name='eventos'),
    path('projetos/', projetos, name='projetos'),
]