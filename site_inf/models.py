from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_evento = models.DateTimeField()
    local = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class PostBlog(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    # Definindo as opções para o campo categoria
    CATEGORIA_ENSINO = 'ENSINO'
    CATEGORIA_EXTENSAO = 'EXTENSAO'
    CATEGORIA_PESQUISA = 'PESQUISA'
    
    CATEGORIA_CHOICES = [
        (CATEGORIA_ENSINO, 'Ensino'),
        (CATEGORIA_EXTENSAO, 'Extensão'),
        (CATEGORIA_PESQUISA, 'Pesquisa'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    # Novo campo para categoria
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default=CATEGORIA_PESQUISA,
        verbose_name="Categoria do Projeto"
    )

    def __str__(self):
        return self.titulo
    
class ExAluno(models.Model):
    CURSOS = (
        ('SI', 'Sistemas de Informação'),
        ('CC', 'Ciência da Computação'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    curso = models.CharField(max_length=2, choices=CURSOS)
    ano_conclusao = models.PositiveIntegerField()
    empresa_atual = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    area_atuacao = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome
    
class EmpresaParceira(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='empresas/', blank=True, null=True)
    site = models.URLField(blank=True)
    descricao = models.TextField(blank=True)
    contato = models.CharField(max_length=200)
    destaque = models.BooleanField(default=False)  # Para exibir no topo, se quiser

    def __str__(self):
        return self.nome
    
class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    empresa = models.ForeignKey(EmpresaParceira, on_delete=models.CASCADE, related_name='vagas')
    descricao = models.TextField()
    local = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=50, choices=[('Estágio', 'Estágio'), ('Emprego', 'Emprego'), ('Trainee', 'Trainee'), ('Outro', 'Outro')])
    link = models.URLField(blank=True)
    data_publicacao = models.DateField(auto_now_add=True)
    data_expiracao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.empresa.nome}"

class TCC(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    autor = models.CharField(max_length=255)
    ano = models.IntegerField(null=True, blank=True)
    palavras_chave = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    # Novo campo para upload do arquivo do TCC
    arquivo_tcc = models.FileField(upload_to='tccs/', null=True, blank=True) # O argumento upload_to define o subdiretório dentro do seu MEDIA_ROOT

    def __str__(self):
        return self.titulo
    
class Publicacao(models.Model):
    titulo = models.CharField(max_length=500, verbose_name="Título da Publicação")
    autores = models.TextField(help_text="Liste os autores. Ex: Silva, J.; Souza, A.; Pereira, L.")
    evento_ou_revista = models.CharField(max_length=500, verbose_name="Nome do Evento, Revista ou Livro")
    ano = models.IntegerField(verbose_name="Ano de Publicação")
    
    link_pdf = models.URLField(blank=True, null=True, verbose_name="Link para o PDF")
    link_bibtex = models.URLField(blank=True, null=True, verbose_name="Link para o BibTeX")
    link_doi = models.URLField(blank=True, null=True, verbose_name="Link para DOI (Digital Object Identifier)")
    link_outro = models.URLField(blank=True, null=True, verbose_name="Outro Link (Ex: App, Código, Apresentação)")

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
        ordering = ['-ano', 'titulo'] # Ordena por ano (mais recente primeiro), depois por título

    def __str__(self):
        return f"{self.titulo} ({self.ano})"