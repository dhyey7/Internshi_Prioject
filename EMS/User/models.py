from django.db import models

# Create your models here.

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(blank=True, null=True, max_length=50)
    
    class Meta:
        db_table = 'Role'
    
class User(models.Model):
    userid = models.CharField(primary_key=True)
    firstname =models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    roleid = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'User'