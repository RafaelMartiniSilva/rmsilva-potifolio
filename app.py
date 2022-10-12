from time import time
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import datetime


load_dotenv()


app = Flask(__name__)
app.secret_key = 'secret#9137*'

mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USE_TLS": False,
    # "MAIL_NAME": name,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA"),
}
app.config.update(mail_settings)

mail = Mail(app)

class Contatos:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send', methods=['GET', 'POST'])
def send():
    print(f'{request.method} method requested')
    if request.method == 'POST':
        form_contato = Contatos(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        time_str = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        msg = Message(
            subject=f'{form_contato.nome} te enviou uma mensagem no portifólio às {time_str}',
            sender=app.config.get('MAIL_USERNAME'),
            recipients=['rafaelmartinisilva@hotmail.com', app.config.get('MAIL_USERNAME')],
            body=f"""
            {form_contato.nome} te enviou a seguinte mensagem:
            {form_contato.mensagem}
            """
        )
        #msg.body = f"""
        #{form_contato.nome} te enviou a seguinte mensagem:
        #{form_contato.mensagem}
        #"""
        #msg.html = f"<b>testing</b><p>{form_contato.nome}</p>"
        mail.send(msg)
        flash("Mensagem enviada com sucesso!")
        return redirect('/')


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5500,
        debug=True
    )
