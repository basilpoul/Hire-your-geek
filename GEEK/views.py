from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .models import URegistration,Coders,Request,Payment,Bid,Work,Chat,Feedback,Warning
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

import datetime as date

# Create your views here.


def home(request):
    return render(request,"index.html")

def login(request):
    dte=datetime.datetime.now()
    if request.POST:
        uname=request.POST["uname"]
        pwd=request.POST["psw"]
        user=authenticate(username=uname,password=pwd)
        if user is None:
            messages.info(request, 'Username or password is incorrect')
        else:
            userdata=User.objects.get(username=uname)
            if userdata.is_superuser == 1:
                return redirect("/adminhome")
            elif userdata.is_staff == 1 and userdata.is_active == 1:
                request.session["email"]=uname
                r = Coders.objects.get(email=uname)
                request.session["id"]=r.id
                request.session["name"]=r.name
                userdata.last_login=dte
                userdata.save()
                return redirect("/coderhome")
                
            else:
                request.session["email"]=uname
                r = URegistration.objects.get(email=uname)
                request.session["id"]=r.id
                request.session["name"]=r.name
                return redirect("/userhome")
    return render(request,"login.html")
    
def registration(request):
    if request.POST:
        name=request.POST["name"]
        
        phone=request.POST["contact"]
        email=request.POST["email"]
        pwd=request.POST["psw"]
        
        add=request.POST["add"]
        user=User.objects.filter(username=email).exists()
        if not user:
            try:
                r=URegistration.objects.create(name=name,email=email,contact=phone,password=pwd,address=add)
                r.save()
            except:
                messages.info(request, 'Sorry some error occured')
            else:
                try:
                    u=User.objects.create_user(username=email,password=pwd,is_superuser=0,is_active=1,is_staff=0,email=email)
                    u.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request, "Registration Succesful")
        else:
            messages.info(request, 'User already registered')

    return render(request,"registration.html")

def coderreg(request):
    if request.POST:
        name=request.POST["name"]
        qual=request.FILES["qual"]
        phone=request.POST["contact"]
        email=request.POST["email"]
        pwd=request.POST["psw"]
        skills=request.POST["skills"]
        lang=request.POST["lang"]
        image=request.FILES["prof"]
        
        add=request.POST["add"]
        user=User.objects.filter(username=email).exists()
        if not user:
            try:
                r=Coders.objects.create(name=name,email=email,contact=phone,psw=pwd,address=add,qualification=qual,lang=lang,skills=skills,status=0,profile=image)
                r.save()
            except:
                messages.info(request, 'Sorry some error occured')
            else:
                try:
                    u=User.objects.create_user(username=email,password=pwd,is_superuser=0,is_active=0,is_staff=1,email=email)
                    u.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request, "Registration Succesful")
        else:
            messages.info(request, 'Coder already registered')

    return render(request,"coderreg.html")



def userhome(request):
    return render(request,"userhome.html")


def coderhome(request):

    dte=datetime.date.today()
    cid=request.session["id"]
    coder=Coders.objects.get(id=cid)
    datas=Work.objects.filter(cid=cid, bidid__duedate__lt=dte)

    data=Warning.objects.filter(cid=cid)
    return render(request,"coderhome.html",{"data":data,"datas":datas})

def noted(request):
    coid=request.session["id"]
    coder=Coders.objects.get(id=coid)
    coder.alert="not send"
    coder.save()
    waid=request.GET.get("id")
    print(waid)
    warn=Warning.objects.get(id=waid).delete()
    

    return render(request,"coderhome.html")


def adminhome(request):
    return render(request,"adminhome.html")


def admincoder(request):
    data=Coders.objects.all()
    return render(request, "admincoder.html",{"data":data})



def adminapprove(request):
    cid=request.GET.get("id")
    d=Coders.objects.get(id=cid)

    demail=d.email
    # print(demail)
    try:
        s=User.objects.get(email=demail)
        print(s.id)
        s.is_active=1
        s.save()
        ct=Coders.objects.get(email=demail)
        ct.status=1
        ct.save()
    except:
        print("Error occured")


    return redirect("/admincoder")



def removecoder(request):
    cid=request.GET.get("id")
    d=Coders.objects.get(id=cid)
    demail=d.email
    print(demail)
    s=User.objects.get(email=demail).delete()
    ct=Coders.objects.get(email=demail).delete()
    return redirect("/admincoder")
    

def coderupdateprof(request):
    uname=request.session["email"]
    if request.POST :
        name=request.POST["t3"]
        contact=request.POST["t4"]
        skills=request.POST["t5"]
        lang=request.POST["t6"]
        add=request.POST["t7"]
        data1=Coders.objects.get(email=uname)
        data1.name=name
        data1.contact=contact
        data1.skills=skills
        data1.lang=lang
        data1.address=add
        data1.save()

        # qry1="update expert set `name`='"+str(name)+"',`email`='"+str(email)+"',`mob`='"+str(mob)+"',`area`='"+str(exp)+"',`exp`='"+str(area)+"' where username='"+str(uname)+"'"
        # print(qry1)
        # c.execute(qry1)
        # con.commit()
    data=Coders.objects.filter(email=uname)
    # qry=f"select * from expert where username='{uname}'"
    # c.execute(qry)
    # data=c.fetchall()
    return render(request,"coderupdateprof.html",{"data":data})

 




def coderbidding(request):
    uid = request.session['id']
    data=Bid.objects.filter(cid=uid)
    

    return render(request,"coderbidding.html",{"data":data})

# def requestwork(request):
    # return render(request,"requestwork.html")

# def viewcurrentwork(request):
    # return render(request,"viewcurrentwork.html")

def coderrequest(request):
    data1=Request.objects.all()

    return render(request,"coderrequest.html",{"data":data1})

# def coderbid(request):
    # return render(request,"coderbid.html")

def coderwork(request):
    uid = request.session['id']
    data=Work.objects.filter(cid=uid)
    


    return render(request,"coderwork.html",{"data":data})

def coderpayment(request):
    uid = request.session['id']
    data=Payment.objects.filter(cid=uid)
    return render(request,"coderpayment.html",{"data":data})

def coderaddbid(request):
    cid = request.session['id']
    rid = request.GET.get("rid")
    # print(cid)
    r=Request.objects.get(id=rid)
    c=Coders.objects.get(id=cid)
    y=r.buid
    s=URegistration.objects.get(id=y.id)
    if request.POST:
        amt=request.POST['amount']
        duedate=request.POST['duedate']

        r=Bid.objects.create(rid=r,cid=c,buid=s,duedate=duedate,amt=amt,status='requested')
        r.save()
        messages.info(request,"Bid added successfully")
    return render(request,"coderaddbid.html")



def buyerreqsubmit(request):
    cid = request.session['id']
    r=URegistration.objects.get(id=cid)
    if request.POST:
        title=request.POST["title"]
        desc=request.POST["desc"]
        date=request.POST["date"]
        syn=request.FILES["syn"]

        data=Request.objects.filter(title=title).exists()
        if not data:
            try:
                r=Request.objects.create(title=title,desc=desc,duedate=date,rfile=syn,status="requested",buid=r)
                r.save()
            except:
                messages.info(request, 'Sorry some error occured')
            else:
                messages.info(request, 'Request Submitted')
        else:
            messages.info(request, 'request already exists')


    return render(request,"buyerreqsubmit.html")

def buyerviewworkstatus(request):
    cid = request.session['id']   
    data=Work.objects.filter(userid=cid)                                                                                                                                          
    return render(request,"buyerviewworkstatus.html",{"data":data})

def buyerviewbid(request):
    cid = request.session['id']
    # r=Request.objects.filter(buid=cid)
    data1=Bid.objects.filter(buid=cid)
    # d=Request.objects.get(buid=cid).delete()



    return render(request,"buyerviewbid.html",{"data":data1})

def buyerpayment(request):
    cid = request.session['id']
    # data1=Work.objects.filter(userid=cid)
    # print(data1)
    data=Payment.objects.filter(wid__userid=cid)
    return render(request,"buyerpayment.html",{"data":data})

def bidreject(request):
    cd=request.GET.get("id")
    d=Bid.objects.get(id=cd)
    d.status="Rejected"
    d.save()


    return redirect("/buyerviewbid")


def bidapprove(request):
    cd=request.GET.get("id")
    cid = request.session['id']
    # print(cd)
    d=Bid.objects.get(id=cd)

    # demail=d.email
    # print(demail)
    pil=d.rid.id
    print(pil)
    due=d.duedate
    f=Request.objects.get(id=pil)
    title=f.title
    # status=d.status
    amt=d.amt
    coid=d.cid
    user=d.buid
    rfile=f.rfile

    d.status="confirmed"
    d.save()
    status=d.status

    s=Work.objects.create(title=title,tforw=due,status=status,amount=amt,cid=coid,userid=user,bidid=d)
    s.save()
    # d=Request.objects.get(id=cd)
    f.status="confirmed"
    f.save()
    # try:
        # s=Work.objects.create(title=title,tforw=due,status=status,amount=amt,cid=coid,userid=user,rfile=rfile)
        # s.save()
        # s=User.objects.get(email=demail)
        # print(s.id)
        # s.is_active=1
        # d.status="confirmed"
        # d.save()
        # ct=Coders.objects.get(email=demail)
        # ct.status=1
        # ct.save()
    # except Exception as e:
        # messages.info(request, 'Sorry some error occured')
        # messages.info(request, e)
    # else:
   
    


    return redirect("/buyerviewbid")


def coderupdatework(request):
    bd=request.GET.get("bidid")
    # rd=request.GET.get("rid")
    status=request.GET.get("status")
    s=Work.objects.get(bidid=bd)
    s.status=status
    s.save()

    return redirect("/coderwork")

def buyermakepayment(request):
    cid = request.session['id']
    user=URegistration.objects.get(id=cid)
    rd=request.GET.get("rid")
    wd=request.GET.get("wid")
    w=Work.objects.get(id=wd)
   
    # data1=Work.objects.get(id=wd)
    # data1.status="Paid"
    data=Work.objects.filter(id=wd)
    # r=Request.objects.get(id=rd)
    work=Payment.objects.filter(id=wd).exists()
    
    if not work:
        if request.POST:
            # date=request.POST['date']
            dte=date.today()
            amt=request.POST['amount']
            p=Payment.objects.create(wid=w,cid=w.cid,date=dte,amt=amt,buid=user)
            p.save()
            messages.info(request,"Payment Successful")
            w.status="paid"
            w.save()
           
            return redirect("/buyerpayment")
        
            
            
                
            
                

    else:
        messages.info(request, 'already paid ')
            

    return render(request,"buyermakepayment.html",{"data":data})



def inchat(request):
    sender = request.session['email']
    # receiver = request.GET.get("email")
    receiver=request.GET.get("email")
    print(receiver)
    print(sender)
    dates=datetime.datetime.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
    #     msg = request.POST['msg']
    #     qry = f"INSERT INTO `chat` (`sender`,`receiver`,`message`,`date`) VALUES('{sender}','{receiver}','{msg}',(select sysdate()))"
    #     c.execute(qry)
    #     db.commit()
    # qryChat = f"SELECT * FROM chat WHERE sender='{sender}' AND receiver='{receiver}' UNION SELECT * FROM chat WHERE receiver='{sender}' AND sender='{receiver}' ORDER BY `chatid`"
    # c.execute(qryChat)
    # messages = c.fetchall()  
    r=Chat.objects.all()
    return render(request,"inchat.html",{"messages":r,"sender":sender, "receiver": receiver}  )



def sfChatPer(request):
    sender = request.session['email']
    receiver = request.GET['email']
    dates=datetime.datetime.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
    #     msg = request.POST['msg']
    #     qry = f"INSERT INTO `chat` (`sender`,`receiver`,`message`,`date`) VALUES('{sender}','{receiver}','{msg}',(select sysdate()))"
    #     c.execute(qry)
    #     db.commit()
    # qryChat = f"SELECT * FROM chat WHERE sender='{sender}' AND receiver='{receiver}' UNION SELECT * FROM chat WHERE receiver='{sender}' AND sender='{receiver}' ORDER BY `chatid`"
    # c.execute(qryChat)
    # messages = c.fetchall()
    r=Chat.objects.all()
    # for i in  r:

    return render(request, "sfChatPer.html", {"messages":r,"sender":sender, "receiver": receiver})  



def buyerfeedback(request):
    uid=request.session["id"]
    user=URegistration.objects.get(id=uid)
    cid=request.GET.get("wid")
    wid=request.GET.get("ciid")
    work=Work.objects.get(id=wid)
    coder=Coders.objects.get(id=cid)
    dte=date.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Feedback.objects.create(con=msg,receiver=coder.email,date=dte,sender=user.name)
        c.save()
        work.status="Completed"
        work.save()
        
        return redirect("/buyerviewworkstatus")
        messages.info(request,"Feedback added")


    return render(request,"buyerfeedback.html")


def adminvfeedback(request):
    
    cid=request.GET.get("id")
    
    coder=Coders.objects.get(id=cid)
    user=User.objects.get(email=coder.email)
    newdate = str(user.last_login)
    data=Feedback.objects.filter(receiver=coder.email)
    if request.POST:
        msg=request.POST["msg"]
        try:
            a=Warning.objects.create(msg=msg,cid=coder)
            a.save()
            coder.status="send"
            coder.save()
        except Exception as e:
            messages.info(request,e)
        else:
            messages.info(request,"Alert send")
    return render(request,"adminvfeedback.html",{"data":data,"user":user,"coder":coder,"ndate":newdate[:19]})