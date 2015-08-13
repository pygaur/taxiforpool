""" sending emails"""

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.template import Context, Template


class SendEmail(object):
    
    def __init__(self, *args, **kwargs):
        self.message = kwargs.get('trigger_name')
        self.model = kwargs.get('model')

    def signup_success(self, *args, **kwargs):
        """ send email after register"""
        try:
            email_setting = self.model.objects.get(trigger_name__trigger_name=self.message).email_setting
        except:
            raise ObjectDoesNotExist 
        customer_object = kwargs.get('entry')
        password = kwargs.get('password')
        if email_setting.status:
            subject = email_setting.subject
            message = email_setting.message
            t = Template(message)
            c = Context(locals())
            final_message = t.render(c)
            msg = EmailMessage(subject, final_message,
                               """Cabforpool <support@cabforpool.com>""",
                               [customer_object.email])
            msg.content_subtype = "html"
            msg.send()

    def trip_submit(self, *args, **kwargs):
        """send email when trip is submitted"""
        try:
            email_setting = self.model.objects.get(trigger_name__trigger_name=self.message).email_setting
        except:
            raise ObjectDoesNotExist 
        entry = kwargs.get('entry')
        if email_setting.status:
            subject = email_setting.subject
            message = email_setting.message
            t = Template(message)
            c = Context(locals())
            final_message = t.render(c)
            msg = EmailMessage(subject, final_message, """Cabforpool <support@cabforpool.com>""", [entry.email])
            msg.content_subtype = "html"
            msg.send()

    def trip_interest(self, *args, **kwargs):
        """"""
        try:
            email_setting = self.model.objects.get(trigger_name__trigger_name=self.message).email_setting
        except:
            raise ObjectDoesNotExist 
        trip = kwargs.get('trip_object')
        customer = kwargs.get('customer_object')
        email = kwargs.get('email')
        if email_setting.status:
            subject = email_setting.subject
            message = email_setting.message
            t = Template(message)
            c = Context(locals())
            final_message = t.render(c)
            msg = EmailMessage(subject, final_message, """ CabForPool <support@cabforpool.com>""", [email])
            msg.content_subtype = "html"
            msg.send()
