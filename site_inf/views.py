from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, PostBlog, Projeto, ExAluno, Professor, EmpresaParceira, Vaga, TCC, Publicacao
from datetime import date
from django.utils.html import escapejs
import json
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

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
    # Agora busca todas as vagas, sem filtrar por data de expiração
    vagas = Vaga.objects.all().order_by('-data_publicacao') 
    return render(request, 'site_inf/pages/listar_vagas.html', {'vagas': vagas})

def tcc_computacao(request):
    tccs = TCC.objects.all()
    return render(request, 'site_inf/pages/tcc_computacao.html', {'tccs': tccs})

def mapa_ex_alunos(request):
    todos_os_alunos = ExAluno.objects.all().order_by('-ano_conclusao', 'nome')
    
    context = {
        'ex_alunos_list': todos_os_alunos 
    }
    return render(request, 'site_inf/pages/listar_exalunos.html', context)

def pagina_publicacoes(request):
    publicacoes = Publicacao.objects.all() # A ordenação do Meta do modelo será usada
    
    # Para criar os títulos de ano como "2024", "2023", etc.
    # Pega todos os anos únicos das publicações, em ordem decrescente
    anos_unicos = sorted(list(set(p.ano for p in publicacoes)), reverse=True)
    
    context = {
        'publicacoes': publicacoes,
        'anos_unicos': anos_unicos, # Para iterar e criar seções por ano
    }
    return render(request, 'site_inf/pages/publicacoes.html', context)

@require_POST # Garante que esta view só aceita requisições POST
def cadastrar_ex_aluno(request):
    try:
        # Pega os dados enviados via JavaScript (em formato JSON)
        data = json.loads(request.body)
        
        # Cria a nova instância do ExAluno no banco de dados
        novo_aluno = ExAluno.objects.create(
            nome=data.get('nome'),
            curso=data.get('curso'),
            ano_conclusao=data.get('ano_conclusao'),
            empresa_atual=data.get('empresa_atual'),
            linkedin=data.get('linkedin'),
            # Latitude e Longitude não são coletadas no formulário, então ficam nulas
            latitude=None, 
            longitude=None,
        )

        # Prepara uma resposta de sucesso para o JavaScript
        response_data = {
            'status': 'success',
            'message': 'Ex-aluno cadastrado com sucesso!',
            'aluno': { # Envia os dados do aluno criado de volta para o frontend
                'id': novo_aluno.id,
                'nome': novo_aluno.nome,
                'ano_conclusao': novo_aluno.ano_conclusao,
                'empresa_atual': novo_aluno.empresa_atual,
                'linkedin': novo_aluno.linkedin
            }
        }
        return JsonResponse(response_data, status=201)

    except Exception as e:
        # Em caso de erro, retorna uma mensagem de falha
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)