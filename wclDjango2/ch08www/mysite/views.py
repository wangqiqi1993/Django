#-*- encoding:utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse
from mysite import models
from mysite import forms
from django.template import RequestContext#因为method = 'POST',网页的显示方法改变
from django.core.mail import EmailMessage
             
def listing(request,pid = None,del_password = None):
	template = get_template('listing.html')
	posts = models.Post.objects.filter(enabled = True).order_by('-pub_time')[:150]
	moods = models.Mood.objects.all()
	if pid and del_password:
		try:
			post = models.Post.objects.get(id = pid)
		except:
			post = None
		if post:
			if post.del_pass == del_password:
				post.delete()
				message = "数据删除成功"
			else:
				message = "删除密码和张贴密码应一致！"
	html = template.render(locals())
	return HttpResponse(html)
def contact(request):
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			message = '感谢您的来信'
			user_name = form.cleaned_data['user_name']
			user_city = form.cleaned_data['user_city']
			user_school = form.cleaned_data['user_school']
			user_email = form.cleaned_data['user_email']
			user_message = form.cleaned_data['user_message']
			mail_body = u'''网友的姓名:{}
					居住城市:{}
					是否在学:{}
					反映意见:{}'''.format(user_name,user_city,user_school,user_message)
			email = EmailMessage('来自[吐槽大会]网站的意见',mail_body,user_email,['clwang1102@163.com'])
			email.send()
		else:
			message = '请检查您输入的信息是否正确'
	else:
		form = forms.ContactForm()
	template = get_template('contact.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)
def post2db(request):
	if request.method == 'POST':
		post_form = forms.PostForm(request.POST)
		if post_form.is_valid():
			message = '您的信息已存储，要等管理员启用后才可看得到'
			post_form.save()
		else:
			message = '如果要张贴信息，那么每个字段都要填写完整'
	else:
		post_form = forms.PostForm()
		message = '如果要张贴信息，那么每个字段都要填写完整'
	template = get_template('post2db.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)

