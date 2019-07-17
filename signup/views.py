from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import SignUpData




class Base(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup/base.html'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/signup.html'

class SignIn(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup/signin.html'

def savedata(request):
	my_model = SignUpData()
	string = request.POST['email']
	my_model.email_text = string
	my_model.password_text = request.POST['pass']
	my_model.name_text = request.POST['u_name']	
	my_model.save()
	return render(request, 'signup/succesfull_signup.html')



def check_data(request):
	#my_model = SignUpData()
	string = request.POST['email']
	password = request.POST['pass']
	try:
		o = SignUpData.objects.get(email_text=string, password_text=password)
		#o = SignUpData.objects.get(name_text="Hamza Talat")
		o.user_set.all()
		o.user_set.create(u_name = o.id)
		o.save()
		
		return render(request, 'user/base.html')	
	except SignUpData.DoesNotExist:
		
		return render(request, 'signup/error.html')
		
	my_model.save()
