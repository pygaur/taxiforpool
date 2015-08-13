from django.contrib import admin

from .models import EmailSetting, EmailTriggerName, EmailTrigger, \
    Newsletter
from .forms import EmailTriggerForm

class EmailSettingAdmin(admin.ModelAdmin):
    """ """
    list_display = ('subject', 'body',  'status')
    list_editable = ('status',)

    def body(self, obj):
        from django.template import Context, Template
        t = Template(obj.message)
        c = Context({})
        return t.render(c)
    body.allow_tags = True
    body.short_description = 'Body'

    class Media:
        """ """
        js = ("/static/js/tiny_mce/tiny_mce.js", '/static/js/textareas.js')

admin.site.register(EmailSetting, EmailSettingAdmin)


class EmailTriggerAdmin(admin.ModelAdmin):
    """ """
    form = EmailTriggerForm
    list_display = ('trigger_name', 'email_setting_message')

    def email_setting_message(self, obj):
        from django.template import Context, Template
        t = Template(obj.email_setting.message)
        c = Context({})
        return t.render(c)
    email_setting_message.allow_tags = True
    email_setting_message.short_description = 'Body'

admin.site.register(EmailTrigger, EmailTriggerAdmin)
admin.site.register(Newsletter)
admin.site.register(EmailTriggerName)
