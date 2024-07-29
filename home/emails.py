# from django.conf import settings
# from home.models import send_email_token
# from django.core.mail import send_mail
# import imp


# def send_account_activation_email(email , email_token):
    
#     subject = 'Your account needs to be verified'
#     email_from = settings.EMAIL_HOST_USER
#     message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
#     send_email_token(subject , message , email_from,[email])