from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, PostBlog, Projeto, ExAluno, Professor, EmpresaParceira, Vaga, TCC
from datetime import date
from django.utils.html import escapejs
import json

def index(request):
    posts = PostBlog.objects.all().order_by('-id')
    projetos = Projeto.objects.all().order_by('-criado_em')[:3]
    return render(request, 'site_inf/pages/index.html', {'projetos': projetos, 'posts': posts})


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

def forum(request):
    return render(request, 'site_inf/pages/forum.html')

def extensao(request):
    return render(request, 'site_inf/pages/extensao.html')

def extensao_projetos(request):
    return render(request, 'site_inf/pages/extensao_projetos.html')

def extensao_inscricoes(request):
    return render(request, 'site_inf/pages/extensao_inscricoes.html')

def adicionar_exalunos_em_lote(request):
    mensagem = ""
    if request.method == "POST":
        dados = request.POST.get("alunos_lote", "")
        linhas = [l.strip() for l in dados.splitlines() if l.strip()]
        adicionados = 0
        for linha in linhas:
            partes = [p.strip() for p in linha.split(",")]
            if len(partes) == 3:
                nome, curso, ano = partes
                if curso in ["SI", "CC"]:
                    ExAluno.objects.create(nome=nome, curso=curso, ano_conclusao=ano)
                    adicionados += 1
        mensagem = f"{adicionados} ex-alunos adicionados com sucesso!"
    return render(request, "site_inf/pages/adicionar_exalunos_lote.html", {"mensagem": mensagem})

def listar_exalunos(request):
    exalunos = ExAluno.objects.all().order_by('-ano_conclusao', 'nome')
    return render(request, 'site_inf/pages/listar_exalunos.html', {'exalunos': exalunos})

def listar_professores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, 'site_inf/pages/listar_professores.html', {'professores': professores})

def empresas_parceiras(request):
    empresas = EmpresaParceira.objects.all().order_by('-destaque', 'nome')
    return render(request, 'site_inf/pages/empresas_parceiras.html', {'empresas': empresas})

def listar_vagas(request):
    vagas = Vaga.objects.filter(
        data_expiracao__gte=date.today()
    ).order_by('-data_publicacao')
    return render(request, 'site_inf/pages/listar_vagas.html', {'vagas': vagas})

def tcc_computacao(request):
    tccs = TCC.objects.all()
    return render(request, 'site_inf/pages/tcc_computacao.html', {'tccs': tccs})

def mapa_ex_alunos(request):
    ex_alunos_com_coords = ExAluno.objects.filter(latitude__isnull=False, longitude__isnull=False).order_by('nome')

    # DEBUG: Imprimir o que está sendo pego pela query
    print("--- DEBUG NA VIEW: mapa_ex_alunos ---")
    print(f"QuerySet ex_alunos_com_coords: {ex_alunos_com_coords}")
    print(f"Contagem de ex_alunos_com_coords: {ex_alunos_com_coords.count()}")
    for aluno in ex_alunos_com_coords:
        print(f"Aluno na lista: ID={aluno.id}, Nome={aluno.nome}, Lat={aluno.latitude}, Lng={aluno.longitude}")
    print("--- FIM DO DEBUG NA VIEW ---")

    context = {
        'ex_alunos_list': ex_alunos_com_coords,
    }
    return render(request, 'site_inf/pages/listar_exalunos.html', context)