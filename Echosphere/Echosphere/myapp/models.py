from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=30)
    def __str__(self):
        return self.user_type

    
class Register(models.Model):
    loginid = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, default="pending")
   
    
class Badge(models.Model):
    badge=models.CharField(max_length=100)
    
class Request(models.Model):
    registerId = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    request=models.CharField(max_length=100)
    
    
    
class Post(models.Model):
    registerId = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="file", null= True)
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100,null=True)
    like_count = models.IntegerField(default=0)
    comment = models.IntegerField(default=0,null=True)
    report_count = models.IntegerField(default=0,null=True)
    

class Report(models.Model):
    liker = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

class Like(models.Model):
    liker = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


class Comments_on_Posts(models.Model):
    uid = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

class AssignBadge(models.Model):
    userId = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    badgeId = models.ForeignKey(Badge, on_delete=models.CASCADE, null=True)


class Donation(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    userId = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True, default="pending")
