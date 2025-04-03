import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

def enviar_email(nome, assunto, mensagem, destinatario=None):
    # Caminho para o template de e-mail
    CAMINHO_HTML = pathlib.Path(__file__).parent / 'email_templates' / 'email_template.html'
    
    # Dados do remetente e destinatário
    remetente = os.getenv('FROM_EMAIL', '')
    if not destinatario:
        destinatario = remetente  # Se nenhum destinatário for informado, envia para o próprio remetente

    # Configurações SMTP (exemplo com Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('FROM_EMAIL', '')
    smtp_password = os.getenv('EMAIL_PASSWORD', '')
    
    # Lê o template HTML e substitui as variáveis ${nome} e ${mensagem}
    with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
        texto_arquivo = arquivo.read()
        template = Template(texto_arquivo)
        texto_email = template.substitute(nome=nome, mensagem=mensagem)
    
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
