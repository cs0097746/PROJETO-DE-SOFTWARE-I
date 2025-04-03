import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

def enviar_email(nome, assunto, destinatario=None):
    # Caminho para o template de e-mail
    CAMINHO_HTML = pathlib.Path(__file__).parent / 'email_templates' / 'email_template.html'
    
    # Dados do remetente e destinatário
    remetente = os.getenv('FROM_EMAIL', '')
    if not destinatario:
        destinatario = remetente  # ou configure para outro e-mail de destino
    
    # Configurações SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('FROM_EMAIL', '')
    smtp_password = os.getenv('EMAIL_PASSWORD', '')
    
    # Carrega o template HTML e substitui a variável ${nome}
    with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
        texto_arquivo = arquivo.read()
        template = Template(texto_arquivo)
        texto_email = template.substitute(nome=nome)
    
    # Monta a mensagem MIME
    mime_multipart = MIMEMultipart()
    mime_multipart['From'] = remetente
    mime_multipart['To'] = destinatario
    mime_multipart['Subject'] = assunto
    
    corpo_email = MIMEText(texto_email, 'html', 'utf-8')
    mime_multipart.attach(corpo_email)
    
    # Envia o e-mail via SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multipart)
        print('E-mail enviado com sucesso!')

# Exemplo de uso:
# enviar_email(nome="Helena", assunto="Teste de E-mail", destinatario="destinatario@example.com")
