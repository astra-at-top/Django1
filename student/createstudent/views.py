from django.shortcuts import render
from django.views import View
from django.http import JsonResponse 
from .models import Student
import json
# Create your views here.
class Createstudent(View):
    template_name = "createstudent/student.html"
    
    def get(self, request):
        print(request.GET)
        studentData = list(Student.objects.all().values())
        return render(request, self.template_name, {"studentData": studentData})
    
    def post(self, request):
        try:
            if "action" in request.POST:
                action = request.POST.get("action")
                print(action,"action")
                if  action == "addStudentdata":
                    name = request.POST.get("name")
                    email = request.POST.get("email")
                    rollno = request.POST.get("rollno")
                    date = request.POST.get("date")
                    if name and email and rollno and date:
                        newStudent = Student.objects.create(
                            name=name,
                            email=email,
                            rollno=int(rollno),
                            date=date
                        )
                        return JsonResponse({
                            "msg": "Student added successfully",
                            "data": {
                                "name": newStudent.name,
                                "email": newStudent.email,
                                "rollno": newStudent.rollno,
                                "date": newStudent.date
                            }
                        })
                    else:
                        return JsonResponse({
                            "msg": "Some fields are missing"
                        }, status=400)
                    
                elif action == "fetchStudentrecord":
                    id = request.POST.get("id")
                    student = Student.objects.get(id=int(id))
                    if student:
                        return JsonResponse({
                            "msg" : "Successfully fetched",
                            "data" : {
                                "name" : student.name,
                                "email" : student.email,
                                "rollno" : student.rollno,
                                "date": student.date
                            }
                        })
                    else:
                        return JsonResponse({
                            "msg" : "No student found"
                        }, status=500)
                    
                else:
                     return JsonResponse({
                            "msg" : "No action found"
                        }, status=500)
            else:
                raise("No action found")    
        except Exception as e:
            return JsonResponse({
                "msg": "Something went wrong",
                "error": str(e)
            }, status=500)
    
    def delete(self, request):
        try:
            data = json.loads(request.body)
            student_id = data.get("id") 
            student = Student.objects.get(id=student_id)
            if student:
                student.delete()
                return JsonResponse({
                        "msg": "Student deleted successfully"
                    }, status=200)
            else :
                return JsonResponse({
                    "msg" : "No student found",
                }, status=400)
        except Exception as e:
            print(str(e))
            return JsonResponse({
                "msg" : "SomeThing went wrong",
                "errror" : str(e)
            }, status=400)
        