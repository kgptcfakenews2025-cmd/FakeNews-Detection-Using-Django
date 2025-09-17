from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from FakeNewsDetection.FakeNewsDetectionApp.models import LoginTable

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = LoginTable.objects.get(username=username, password=password)
            request.session['user_id'] = obj.id
            if obj.user_type == 'admin':
                return HttpResponse("<script>alert('Login successful');window.location='/admin_dash'</script>")
            elif obj.user_type == 'teacher':
                return HttpResponse("<script>alert('Login successful');window.location='/teacher_home'</script>")
            elif obj.user_type == 'student':
                return HttpResponse("<script>alert('Login successful');window.location='/student_home'</script>")
        except LoginTable.DoesNotExist:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/login'</script>")



class ViewUser(View):
    def get(self,request):
        return render(request,'viewuser.html')    

class Complaint(View):
    def get(self,request):
        return render(request,'complaint&reply.html')
    
class Reply(View):
    def get(self,request):
        return render(request,'reply.html')
    
class Feedback(View):
    def get(self,request):
        return render(request,'feedback.html')
    
