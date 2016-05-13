from django.db import models


class User(models.Model):
    name = models.CharField('User Name', max_length=200, unique=True)
    friends = models.ManyToManyField('User')
    password = models.CharField('User Password', max_length=200)
    register_time = models.DateTimeField('Register Time', auto_now_add=True)
    email = models.EmailField('User Email', null=True)

    def __str__(self):
        return self.name


class OnlineUser(models.Model):
    user = models.OneToOneField(User)
    login_time = models.DateTimeField('Login Time', auto_now_add=True)
    token = models.CharField('User Token', max_length=200, unique=True)

    def __str__(self):
        return self.user.name






