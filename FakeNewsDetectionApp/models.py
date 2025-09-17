from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)
    Type = models.CharField(max_length=30, null=True, blank=True)
    
class UserTable(models.Model):
    loginid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name = models.CharField(max_length=30, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=30, null=True, blank=True)
    Address = models.CharField(max_length=30, null=True, blank=True)
    Phone = models.BigIntegerField(null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)

class ComplaintTable(models.Model):
    userid=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Complaint = models.CharField(max_length=1000, null=True, blank=True)
    Reply = models.CharField(max_length=1000, null=True, blank=True)
    Date = models.DateField(auto_now_add=True,null=True,blank=True)

class FeedbackTable(models.Model):
    userid=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Feedback = models.CharField(max_length=1000, null=True, blank=True)
    Date = models.DateField(auto_now_add=True,null=True,blank=True)
