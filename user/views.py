from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Tweets
from .models import User
from .models import SignUpData

class Base(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/base.html'


#class Write_tweet(generic.CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('successfull')
#    template_name = 'user/Write_tweet.html'

def like_tweet(request,ids):
	o = Tweets.objects.get(tweet = ids)
	o.likes+=1
	o.save()

def search_user(request):
	string = request.POST.get('User_info')
	try:
		o = SignUpData.objects.get(name_text=string)
		return render(request, 'user/user_found.html' , {'o': o})	
	except SignUpData.DoesNotExist:		
		return render(request, 'user/error.html' ,{'string':string})


def show_tweets(request):
	a=User.objects.latest('id')
	var=a.u_name
	a = SignUpData.objects.get(name_text=var.name_text)
	b=a.user_set.all().first()	
	b.tweets_set.all()
	return render(request, 'user/show_tweets.html' ,{'a':b})



def savetweet(request):
	string = request.POST['tweet']
	a=User.objects.latest('id')
	var=a.u_name
	a = SignUpData.objects.get(name_text=var.name_text)
	b=a.user_set.all().first()	
	b.tweets_set.all()
	b.tweets_set.create(tweet=string , likes=0)
	b.save()
	return render(request, 'user/successfull_tweet.html')
def signout(request):
	return render(request, 'signup/signin.html')

def writetweet(request):
	return render(request,'user/Write_tweet.html')
