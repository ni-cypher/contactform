# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from bs4 import BeautifulSoup
import urllib.request
from .project import Project

def emailView(request):
 if request.method == 'GET':
  form = ContactForm()
 else:
  form = ContactForm(request.POST)
  if form.is_valid():
     quilcheck_box = form.cleaned_data['quilcheck_box']
     work_period_sele = form.cleaned_data['work_period_sele']
     employ_type_box = form.cleaned_data['employ_type_box']
     wanted_place_sele01 = form.cleaned_data['wanted_place_sele01']
     wanted_place_sele02 = form.cleaned_data['wanted_place_sele02']
     wanted_industry_box = form.cleaned_data['wanted_industry_box']
     name = form.cleaned_data['name']
     kana = form.cleaned_data['kana']
     birth_yearsele = form.cleaned_data['birth_yearsele']
     birth_monthsele = form.cleaned_data['birth_monthsele']
     birth_daysele = form.cleaned_data['birth_daysele']
     address01_sele = form.cleaned_data['address01_sele']
     address02 = form.cleaned_data['address02']
     tel = form.cleaned_data['tel']
     from_email = form.cleaned_data['from_email']
     message = form.cleaned_data['message']


     request.session['quilcheck_box'] = quilcheck_box
     request.session['work_period_sele']= work_period_sele
     request.session['employ_type_box']= employ_type_box
     request.session['wanted_place_sele01'] = wanted_place_sele01
     request.session['wanted_place_sele02'] = wanted_place_sele02
     request.session['wanted_industry_box'] = wanted_industry_box
     request.session['name'] = name
     request.session['kana'] = kana
     request.session['birth_yearsele'] = birth_yearsele
     request.session['birth_monthsele'] = birth_monthsele
     request.session['birth_daysele'] = birth_daysele
     request.session['address01_sele'] = address01_sele
     request.session['address02'] = address02
     request.session['tel'] = tel
     request.session['from_email'] = from_email
     request.session['message'] = message
     request.session['confrim'] = 1
   
     form_content=request.POST.get('content','')
     template=get_template('contact_template.txt')
     context={
     	'quilcheck_box': quilcheck_box,
     	'work_period_sele':work_period_sele,
      'employ_type_box': employ_type_box,
      'wanted_place_sele01':wanted_place_sele01,
      'wanted_place_sele02': wanted_place_sele02,
      'wanted_industry_box':wanted_industry_box,
      'name': name,
      'kana':kana,
      'birth_yearsele': birth_yearsele,
      'birth_monthsele':birth_monthsele,
      'birth_daysele': birth_daysele,
      'address01_sele':address01_sele,
      'address02': address02,
      'tel':tel,
      'from_email': from_email,
      'message':message,
     	}
     content=template.render(context);
     #try:
      # send_mail(subject, content, from_email, ['nwe.n@cypher-point.co.jp'])
      # send_mail(subject, content, 'nwe.n@cypher-point.co.jp', [from_email])
     #except BadHeaderError:
      #return HttpResponse('Invalid header found.')
     return redirect('success')
 return render(request, "email.html", {'form': form})

def successView(request):

 form = ContactForm(request.POST)
 quilcheck_box = request.session['quilcheck_box']
 work_period_sele = request.session['work_period_sele']
 employ_type_box = request.session['employ_type_box']
 wanted_place_sele01 = request.session['wanted_place_sele01']
 wanted_place_sele02 = request.session['wanted_place_sele02']
 wanted_industry_box = request.session['wanted_industry_box']
 name = request.session['name']
 kana = request.session['kana']
 birth_yearsele = request.session['birth_yearsele']
 birth_monthsele = request.session['birth_monthsele']
 birth_daysele = request.session['birth_daysele']
 address01_sele = request.session['address01_sele']
 address02 = request.session['address02']

 tel = request.session['tel']
 from_email = request.session['from_email']
 message = request.session['message']
 confrim = request.session['confrim']
 print(confrim)
 #form confirm page 
 if(confrim==1):
  request.session['confrim']=0
  return render(request, "success.html", {'quilcheck_box': quilcheck_box,'work_period_sele': work_period_sele,'employ_type_box': employ_type_box,'wanted_place_sele01': wanted_place_sele01,'wanted_place_sele02': wanted_place_sele02,'wanted_industry_box': wanted_industry_box,'name': name,'kana': kana,'birth_yearsele': birth_yearsele,'birth_monthsele': birth_monthsele,'birth_daysele': birth_daysele,'address01_sele': address01_sele,'address02': address02,'tel': tel,'from_email': from_email,'message': message})
   # return redirect('thanks')
 #form complete page
 else:
  form_content=request.POST.get('content','')
  template=get_template('contact_template.txt')
  template_user=get_template('contact_template_user.txt')
  context={
   'quilcheck_box': quilcheck_box,
   'work_period_sele':work_period_sele,
   'employ_type_box': employ_type_box,
   'wanted_place_sele01':wanted_place_sele01,
   'wanted_place_sele02': wanted_place_sele02,
   'wanted_industry_box':wanted_industry_box,
   'name': name,
   'kana':kana,
   'birth_yearsele': birth_yearsele,
   'birth_monthsele':birth_monthsele,
   'birth_daysele': birth_daysele,
   'address01_sele':address01_sele,
   'address02': address02,
   'tel':tel,
   'from_email': from_email,
   'message':message,
   }
  content=template.render(context);
  content_user=template_user.render(context);
  subject="python"
  try:
   send_mail(subject, content, from_email, ['nwe.n@cypher-point.co.jp'])
   send_mail(subject, content_user, 'nwe.n@cypher-point.co.jp', [from_email])
  except BadHeaderError:
   return HttpResponse('Invalid header found.')
  return redirect('thanks')

def thanksView(request):

 return render(request, "thanks.html",)

def projectView(request):
 project_list=[]
 project_list2=[]
 #project_list.append(Project("0","0","0","0"))
 #project_list.append(Project("1","1","1","1"))
 
 #print(project_list)
  
 html_doc=urllib.request.urlopen("https://www.doctor-vision.com/search_full/all/")
 soup = BeautifulSoup(html_doc, 'html.parser')
 html_doc2=urllib.request.urlopen("https://rikunabi-yakuzaishi.jp/search/?page=&from=&pref=13&x=71&y=20&srchld=full_n_13_n_n_n_n")
 soup2 = BeautifulSoup(html_doc2, 'html.parser')





 #<a><a/>
 #pg_alla=soup.find_all('h3',class_="pg_settl")
 for link in soup.find_all('h3',class_="pg_settl"):
    project_list.append(Project(link.text,"0","0","0"))
 #for project_lists in project_list:
    #print(project_lists.prjName)
 for link in soup2.find_all('p',class_="catch"):
    project_list2.append(Project(link.text,"0","0","0"))


 return render(request,"project_list.html",{'soup': project_list,'soup2': project_list2})

