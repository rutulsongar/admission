from django.db import models

class stu(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
 
class memebers(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.TextField()
    Addhar_no = models.TextField()
    phone_no = models.TextField()
    email = models.TextField()
    religion = models.TextField()
    Address = models.TextField()

    Gender = models.TextField(null=True)
    dob = models.DateField(null=True)
    blood = models.TextField(null=True)
    entry = models.TextField(null=True)
    cource = models.TextField(null=True)
    approval = models.BooleanField(default=False,null=True)
    photo = models.ImageField(upload_to='static',null=True)
    marksheet = models.ImageField(upload_to='static',null=True)
    class Meta:
        db_table = ("admission_tbl")
