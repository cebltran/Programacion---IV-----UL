import  ssl, smtplib

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


def eviocorreo ( destino, texto):
    context = ssl.create_default_context()
    usuario = 'parcialmodulo8@gmail.com'
    contras = 'modulo2021'
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(usuario, contras)
        server.sendmail(usuario,  destino, str(texto))


