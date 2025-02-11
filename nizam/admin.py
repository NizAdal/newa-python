from django.contrib import admin
from .models import Blog, About, Message, Contact,Membership,Notes,Survey,Questions,Data
# Register your models here.
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Membership)
admin.site.register(Notes)
admin.site.register(Survey)
admin.site.register(Data)
admin.site.register(Questions)