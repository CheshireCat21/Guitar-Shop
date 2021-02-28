from django.db import models


class User(models.Model):

    name = models.CharField('name', max_length=250)
    nick_name = models.CharField('nick name', max_length=250)
    email = models.CharField('email', max_length=250)
    password = models.CharField('password', max_length=250)
    repeat_password = models.CharField('repeat password', max_length=250)

    class Meta:

        verbose_name = "User"
        verbose_name_plural = "Users"