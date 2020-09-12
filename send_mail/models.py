from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    email = models.CharField(max_length=100, blank=False, null=False, verbose_name='email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
