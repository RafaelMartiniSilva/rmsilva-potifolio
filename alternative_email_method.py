import smtplib
import email.message
from dotenv import load_dotenv
import os
import datetime


load_dotenv()


def main():

    time_str = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    corpo_email = """
    <p>Parágrafo 1</p>
    <p>Parágrafo 2</p>
    """
    msg = email.message.Message()
    msg['Subject'] = f"Teste - {time_str}"
    msg['From'] = os.getenv("EMAIL")
    msg['To'] = os.getenv("EMAIL")
    password = os.getenv("SENHA")
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com: 587')

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(msg['From'], password)

    # sending the mail
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('UTF-8'))

    # Success message
    print('E-mail enviado')

    # terminating the session
    s.quit()

    # Success message
    print('E-mail enviado')




def mail_1():
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login("rafaelmartinisilva@gmail.com", "Ratazana01*1992")
    
    # message to be sent
    message = "Message_you_need_to_send"
    
    # sending the mail
    s.sendmail("rafaelmartinisilva@gmail.com", "rafaelmartinisilva@hotmail.com", message)
    
    # terminating the session
    s.quit()


if __name__ == '__main__':
    main()