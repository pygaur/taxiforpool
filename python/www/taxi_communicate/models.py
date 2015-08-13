from django.db import models


class EmailTriggerName(models.Model):
    """ """
    trigger_name = models.CharField(max_length=35, unique=True)
    
    def __unicode__(self):
        return self.trigger_name


class EmailSetting(models.Model):
    """ """
    subject = models.CharField(max_length=450)
    message = models.TextField()
    status = models.BooleanField()

    def __unicode__(self):
        """ """
        return self.subject

    class Meta:
        """"""
        app_label = "taxi_communicate"
        verbose_name = "Email setting trigger"
        verbose_name_plural = "Email Setting triggers"


class EmailTrigger(models.Model):
    """ """
    trigger_name = models.ForeignKey(EmailTriggerName)
    email_setting = models.ForeignKey(EmailSetting)

    def __unicode__(self):
        return self.trigger_name.trigger_name

    class Meta:
        """ """
        app_label = "taxi_communicate"
        verbose_name = "Email Trigger"
        verbose_name_plural = "Email Triggers"


class Newsletter(models.Model):
    """ """
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email

    class Meta:
        """ """
        app_label = "taxi_communicate"
