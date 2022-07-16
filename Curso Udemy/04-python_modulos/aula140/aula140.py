from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email = ''
senha = ''

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome = 'Andre', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Andre P'
msg['to'] = email
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('foto.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, senha)
    smtp.send_message(msg)
    print('Email enviado com sucesso.')
