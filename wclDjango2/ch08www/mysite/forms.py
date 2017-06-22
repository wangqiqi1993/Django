#-*- encoding:utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from mysite import models
class ContactForm(forms.Form):
	CITY = [

			['江苏','南京'],
			['山东','济南'],
			['山东','青岛'],
			['山东','淄博'],
			['天津','天津'],
			['北京','北京'],
		]
	user_name = forms.CharField(label = '您的姓名',max_length = 50,initial = 'wcl')
	user_city = forms.ChoiceField(label = '居住城市',choices = CITY )
	user_school = forms.BooleanField(label = '是否在学',required = False)
	user_email = forms.EmailField(label = '电子邮件')
	user_message = forms.CharField(label = '您的意见',widget = forms.Textarea)
class PostForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = models.Post
		fields = ['mood','nickname','message','del_pass']
	def __init__(self,*args,**kwargs):	
		super(PostForm,self).__init__(*args,**kwargs)		
		self.fields['mood'].label = '现在的心情'
		self.fields['nickname'].label = '您的昵称'
		self.fields['message'].label = '心情留言'
		self.fields['del_pass'].label = '设置密码'
		self.fields['captcha'].label = '确定您不是机器人'
