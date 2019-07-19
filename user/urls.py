from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
	path('' , views.Base.as_view() , name='base'),
	#path('Write_tweet', views.Write_tweet.as_view(), name='write_tweet'),
	path('savetweet', views.savetweet, name='savetweet'),
	path('signout', views.signout, name='signout'),
	path('writetweet', views.writetweet, name='writetweet'),
	path('search_user', views.search_user, name='search_user'),
	path('find_user', views.find_user, name='find_user'),
	path('show_tweets', views.show_tweets, name='show_tweets'),
	path('like_tweet/<str:ids>', views.like_tweet, name='like_tweet'),
	path('comment_tweet', views.comment_tweet, name='comment_tweet'),
	path('coment/<str:ids>', views.coment, name='coment'),
]
