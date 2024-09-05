from django.core.mail import EmailMessage

"""
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'butvlad55@yandex.ru'
EMAIL_HOST_PASSWORD = 'ButSvet2501'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'butvlad55@yandex.ru'"""

em = EmailMessage(subject='Test', body='TEKST', to=['vlaver@mail.ru'])
em.send()

