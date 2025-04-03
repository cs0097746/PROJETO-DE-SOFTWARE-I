from django.shortcuts import render, redirect
from .models import Curso, Evento, PostBlog
from .forms import ContatoForm
from .utils_email import enviar_email

def index(request):
    return render(request, 'site_inf/pages/index.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'site_inf/pages/cursos.html', {'cursos': cursos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'site_inf/pages/eventos.html', {'eventos': eventos})

def blog(request):
    posts = PostBlog.objects.all()
    return render(request, 'site_inf/pages/blog.html', {'posts': posts})

def projetos(request):
    # Por enquanto, podemos renderizar um template simples para projetos.
    return render(request, 'site_inf/pages/projetos.html')


from django.shortcuts import redirect
from .forms import ContatoForm
from .utils_email import enviar_email  # Importe a função criada

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            mensagem_obj = form.save()  # Salva a mensagem no banco de dados, se desejar

            # Envia o e-mail utilizando os dados do formulário
            enviar_email(
                nome=mensagem_obj.nome,
                assunto="Nova mensagem de contato enviada pelo site",
                mensagem=mensagem_obj.mensagem,
                destinatario='destinatario@exemplo.com'  # ou use uma variável/configuração
            )
            return redirect('site_inf:contato')  # Redireciona ou exibe uma página de sucesso
    else:
        form = ContatoForm()
    
    return render(request, 'site_inf/pages/contato.html', {'form': form})