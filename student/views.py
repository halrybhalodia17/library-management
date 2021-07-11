from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentDb
from .forms import Studform

# Create your views here.
def login(request):
    if request.method == 'POST':
        userform = Studform(request.POST)
        ip_email = userform.data['email']
        ip_password = userform.data['password']
        try:
            stud = StudentDb.objects.get(email=ip_email)
            if stud.password == ip_password:
                info={
                    'enroll_no': stud.enroll_no,
                    'name': stud.name,
                    'email': stud.email,
                    'branch': stud.branch,
                    'phone_no': stud.phone_no,
                    'roll_no': stud.roll_no,
                    'shift': stud.shift
                }
                return render(request,'student.html', info)
            else:
                return render(request,'error.html')
        except:
            return render(request,'error.html')

    else:
        myform = Studform()
        return render(request, 'Student_login.html', {'form': myform})

def dashboard(request):
    return render(request,'Student.html')
