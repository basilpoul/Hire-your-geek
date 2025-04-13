"""HIREYOURGEEK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GEEK import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('coderreg',views.coderreg,name="coderreg"),
    path('userhome',views.userhome,name="userhome"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('coderhome',views.coderhome,name="coderhome"),
    path('admincoder',views.admincoder,name="admincoder"),
    path('adminapprove',views.adminapprove,name="adminapprove"),
    path('removecoder',views.removecoder,name="removecoder"),
    path('coderupdateprof',views.coderupdateprof,name="coderupdateprof"),
    path('coderbidding',views.coderbidding,name="coderbidding"),
    # path('requestwork',views.requestwork,name="requestwork"),
    # path('viewcurrentwork',views.viewcurrentwork,name="viewcurrentwork"),
    path('coderrequest',views.coderrequest,name="coderrequest"),
    # path('coderbid',views.coderbid,name="coderbid"),
    path('coderwork',views.coderwork,name="coderwork"),
    path('coderpayment',views.coderpayment,name="coderpayment"),
    path('coderaddbid',views.coderaddbid,name="coderaddbid"),
    path('buyerreqsubmit',views.buyerreqsubmit,name="buyerreqsubmit"), 
    path('buyerviewbid',views.buyerviewbid,name="buyerviewid"),
    path('buyerviewworkstatus',views.buyerviewworkstatus,name="buyerviewworkstatus"),
    path('buyerpayment',views.buyerpayment,name="buyerpayment"),
    path('bidapprove',views.bidapprove,name="bidapprove"),
    path('bidreject',views.bidreject),
    path('coderupdatework',views.coderupdatework,name="coderupdatework"),
    path('buyermakepayment',views.buyermakepayment,name="buyermakepayment"),
    path('inchat',views.inchat,name="inchat"),
    path('sfChatPer',views.sfChatPer,name="sfChatPer"),
    path('buyerfeedback',views.buyerfeedback),
    path('adminvfeedback',views.adminvfeedback),
    path('noted',views.noted),

      


]
