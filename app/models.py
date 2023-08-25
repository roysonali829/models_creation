from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    loc = models.CharField(max_length=100,default='banglore')

    def __str__(self):
        return self.name

class Emp(models.Model):
    deptno = models.ForeignKey(Dept,on_delete = models.CASCADE)
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    sal = models.IntegerField()
    comm = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.empname
