from django.contrib import admin
from user.models import User , Tweets , comments


admin.site.register(User)
admin.site.register(Tweets)
admin.site.register(comments)
# Register your models here.
