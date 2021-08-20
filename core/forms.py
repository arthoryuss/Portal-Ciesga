from django import forms
from django.core.mail import send_mail
from django.conf import settings

from .mail import send_mail_template


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_mail(self, course):
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'core/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )
