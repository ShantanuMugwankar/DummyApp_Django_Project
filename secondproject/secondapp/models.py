from django.db import models

# Create your models here.
class Question(models.Model):
    qno=models. IntegerField(primary_key=True)
    qtext=models.CharField(max_length=100)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def _str_(self) -> str:
        return f"(self.qno, self.qtext, self.answer, self.opl, self.op2)"

    class Meta:
        db_table="question"

class UserData(models.Model):
    email = models.EmailField(max_length=100, unique=True, primary_key=True) 
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return f"username: {self.username}, email: {self.email}, password: {self.password}"

    class Meta:
        db_table = "userdata"

class AdminData(models.Model):
    username=models.CharField(max_length=40,primary_key=True)
    email = models.EmailField(max_length=100, unique=True) 
    password=models.CharField(max_length=20)

    class Meta:
        db_table='admindata'


class Result(models.Model):
    srno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40)
    subject=models.CharField(max_length=20)
    score=models.IntegerField()

    class Meta:
        db_table='result'