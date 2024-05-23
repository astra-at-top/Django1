from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
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
                # User.objects.create_user(username, email, password)
                return redirect("http://127.0.0.1:8000/auth/login",permanent=True)
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
    
    def post(self, request):
        action = request.POST.get("action")

        if action:
            if action == "login":
                username = request.POST.get("username")
                password = request.POST.get("password")
                if username and password:
                    user = authenticate(request, username=username,password=password)
                    print(user,"user")
                    if user is not None:
                        login(request, user)
                        return JsonResponse({
                            "msg" : "User successfully login"
                        })
                    else:
                        return JsonResponse({
                            "msg" : "Fail to login "
                        })
                else :
                    return JsonResponse({
                        "msg" : "Incomplete values"
                    })
            else :
                logout(request)
                return JsonResponse({
                    "msg" : "User logout successfully"
                })
        else :
            return JsonResponse({
                "msg" : "No action found"
            })