from django.shortcuts import render,redirect
from django.contrib import messages, auth 
from django.contrib.auth.models import User
from django.contrib.auth import logout
from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('index')
        else:
            messages.error(request,"invalid credential")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,"that username is taken!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"that email is being used!")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    user.save()
                    # auth.login(request,user)
                    messages.success(request,'you are now can register in')
                    return redirect('login')
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contacts,
    }
    return render(request,'accounts/dashboard.html',context)

def logout_view(request):
    logout(request)
    messages.success(request,"You are logged out")
    return redirect('index')