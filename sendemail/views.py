# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm

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

