from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.

class Index(generic.View):
    template_name = 'home/index.html'
    context = {}

    def get(self, request):
        self.context={
            "users":User.objects.all() #Es igual a un select * from auth_user;
        }
        
        return render(request, self.template_name, self.context)