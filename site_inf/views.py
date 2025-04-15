from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, PostBlog, Projeto

def index(request):
    from .models import Projeto
    projetos = Projeto.objects.all().order_by('-criado_em')[:3]
    return render(request, 'site_inf/pages/index.html', {'projetos': projetos})


def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'site_inf/pages/eventos.html', {'eventos': eventos})

def blog(request):
    posts = PostBlog.objects.all()
    return render(request, 'site_inf/pages/blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(PostBlog, id=post_id)
    return render(request, 'site_inf/pages/post_detail.html', {'post': post})

def sistemas_info(request):
    return render(request, 'site_inf/pages/curso_sistemas_info.html')

def ciencia_computacao(request):
    return render(request, 'site_inf/pages/curso_ciencia_computacao.html')

def projetos(request):
    projetos = Projeto.objects.all().order_by('-criado_em')
    return render(request, 'site_inf/pages/projetos.html', {'projetos': projetos})

def projeto_detail(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    return render(request, 'site_inf/pages/projeto_detail.html', {'projeto': projeto})
