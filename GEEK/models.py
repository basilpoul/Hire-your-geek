from django.db import models

# Create your models here.
class URegistration(models.Model):
    name=models.CharField(max_length=30)
    
    email=models.EmailField(max_length=50)
    contact=models.BigIntegerField()
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)

class Coders(models.Model):
    name=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    qualification=models.ImageField()
    psw=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=50,null=True)
    lang=models.CharField(max_length=20,null=True)
    skills=models.CharField(max_length=20,null=True)
    profile=models.ImageField(null=True)
    alert=models.CharField(max_length=10,null=True)


    # rfile=models.ImageField(null=True)


class Request(models.Model):
     buid=models.ForeignKey(URegistration,on_delete=models.CASCADE,null=True)
     title=models.CharField(max_length=20)
     desc=models.CharField(max_length=20)
     duedate=models.DateField()
     rfile=models.ImageField()
     status=models.CharField(max_length=20)  
        
     


class Bid(models.Model):
    rid=models.ForeignKey(Request,on_delete=models.CASCADE)
    cid=models.ForeignKey(Coders,on_delete=models.CASCADE)
    buid=models.ForeignKey(URegistration,on_delete=models.CASCADE,null=True)
    duedate=models.DateField()
    amt=models.BigIntegerField()
    status=models.CharField(max_length=20)

class Work(models.Model):
    title=models.CharField(max_length=20)
    tforw=models.DateField()
    status=models.CharField(max_length=10)
    amount=models.BigIntegerField(null=True)
    cid=models.ForeignKey(Coders, on_delete=models.CASCADE)
    userid=models.ForeignKey(URegistration, on_delete=models.CASCADE)
    bidid=models.ForeignKey(Bid, on_delete=models.CASCADE)

class Payment(models.Model):
    wid=models.ForeignKey(Work,on_delete=models.CASCADE,null=True)
    cid=models.ForeignKey(Coders,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    amt=models.BigIntegerField()
    buid=models.ForeignKey(URegistration,on_delete=models.CASCADE,null=True)

class Chat(models.Model):
    sender=models.CharField(max_length=20)
    receiver=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    message=models.CharField(max_length=400)


class Feedback(models.Model):
    con=models.CharField(max_length=100)
    sender=models.CharField(max_length=20)
    receiver=models.EmailField()
    date=models.DateField()


class Warning(models.Model):
    msg=models.CharField(max_length=20)
    cid=models.ForeignKey(Coders,on_delete=models.CASCADE)