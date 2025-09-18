from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from FakeNewsDetectionApp.models import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = LoginTable.objects.get(Username=username, Password=password)
            request.session['user_id'] = obj.id
            if obj.Type == 'admin':
                return HttpResponse("<script>alert('Login successful');window.location='/adminhome'</script>")
        except LoginTable.DoesNotExist:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/login'</script>")


class ViewUser(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request,'viewuser.html', {'val': obj})    

class AcceptUser(View):
    def get(self,request, id):
        obj = LoginTable.objects.get(id=id)
        obj.Type="user"
        obj.save()
        return redirect('ViewUser')
    
class RejectUser(View):
    def get(self,request, id):
        obj = LoginTable.objects.get(id=id)
        obj.Type="rejected"
        obj.save()
        return redirect('ViewUser')

class Complaint(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request,'complaint&reply.html',{'val': obj})
    
class Reply(View):
    def get(self,request):
        return render(request,'reply.html')
    
class Feedback(View):
    def get(self,request):
        obj = FeedbackTable.objects.all()
        return render(request,'feedback.html',{'val': obj})
    
class AdminHome(View):
    def get(self,request):
        return render(request,'home.html')
