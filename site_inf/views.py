from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, PostBlog

def index(request):
    return render(request, 'site_inf/pages/index.html')

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'site_inf/pages/eventos.html', {'eventos': eventos})

def blog(request):
    posts = PostBlog.objects.all()
    return render(request, 'site_inf/pages/blog.html', {'posts': posts})

def projetos(request):
    # Por enquanto, podemos renderizar um template simples para projetos.
    return render(request, 'site_inf/pages/projetos.html')

def post_detail(request, post_id):
    post = get_object_or_404(PostBlog, id=post_id)
    return render(request, 'site_inf/pages/post_detail.html', {'post': post})

def sistemas_info(request):
    return render(request, 'site_inf/pages/curso_sistemas_info.html')

def ciencia_computacao(request):
    return render(request, 'site_inf/pages/curso_ciencia_computacao.html')
