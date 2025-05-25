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
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class ExAluno(models.Model):
    CURSOS = (
        ('SI', 'Sistemas de Informação'),
        ('CC', 'Ciência da Computação'),
    )
    nome = models.CharField(max_length=200)
    curso = models.CharField(max_length=2, choices=CURSOS)
    ano_conclusao = models.PositiveIntegerField()


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
    ano = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)  # opcional: link para o PDF ou repositório

    def __str__(self):
        return self.titulo