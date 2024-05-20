from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.


class Auths(View):
    template_name = "validation/SignupForm.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")

        print(request.POST)
        # print(username, )
        if username and email and password and confirmpassword:
            print(username, email, password, confirmpassword,"credintials")
            if password == confirmpassword:
                User.objects.create_user(username, email, password)
                return JsonResponse({
                    "msg": "user created Succesfully"
                }, status = 200)
            else:
                return JsonResponse({
                    "msg" : "Password Do not match"
                }, status = 500)
        else:
            return JsonResponse({
                "msg" : "Some field is missing "
            }, status = 500)
class Login(View):
    template_name = "validation/Loginform.html"

    def get(self, request):
        return render(request, self.template_name)