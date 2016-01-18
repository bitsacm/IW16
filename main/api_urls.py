from django.conf.urls import url
from main import api_views

urlpatterns = [
	url(r'^get-question/(?P<qno>\d+)/$', api_views.get_question, name='get_question'),
	url(r'^login/$', api_views.login_view, name='login'),
	url(r'^logout/$', api_views.logout_view, name='logout'),
	url(r'^submit/(?P<qno>\d+)/$', api_views.submit, name='submit'),
	url(r'^game-info/$', api_views.game_info, name='game_info'),
	url(r'^user-info/$', api_views.user_info, name='user_info'),
]
