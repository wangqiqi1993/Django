from datetime import date
from haystack.generic_views import SearchView
from models import *
class MySearchView(SearchView):
	def get_context_data(self,*args,**kwargs):
		context = super(MySearchView,self).get_context_data(*args,**kwargs)
		context['username'] = self.request.session.get('username',default = '')
		sessionUserId = self.request.session.get('userId',default = '')
		cartList = UserInfo.objects.get(pk = sessionUserId).cartinfo_set.all()
		cartCount = 0
		for cartInfo in cartList:
			cartCount += cartInfo.qty
			context['cartCount'] = cartCount
			return context
