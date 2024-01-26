from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from .models import memebers

from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str


from admission_management_system import settings
from . tokens import generate_token

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is home")

def contact(request):
    return render(request, 'contect.html')
    #return HttpResponse("this is contact")

def Admission(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'Admission.html')    
    #return HttpResponse("this is Admission")

def Next(request):
    return render(request, 'Next.html')
    #return HttpResponse("this is Next")

    return HttpResponsere

def storedata(request):
    if request.method == 'POST':
        name = request.POST['name']
        Addhar_no = request.POST['addhar_card']
        phone_no = request.POST['ph_no']
        email = request.POST['email']
        religion = request.POST['religion']
        Address = request.POST['address']
        Gender = request.POST['Gender']
        date = request.POST['DOB']
        blood_grp = request.POST['blood_grp']
        entry_level = request.POST['entry_level']
        Course_Preference = request.POST['Course_Preference']
        marksheet = request.FILES['marksheet']
        photo = request.FILES['photo']

        # Create a new Subject instance

        memeber = memebers(name=name,Addhar_no=Addhar_no,phone_no=phone_no,email=email,religion=religion,Address=Address,Gender=Gender,blood=blood_grp,cource=Course_Preference,dob=date,entry=entry_level,marksheet=marksheet,photo=photo)

        subject = "Welcome to Admission Management - Login!!"
        message = "Your Admission will be send to our Admin They will Contact You.\nhttp://127.0.0.1:8000/"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)

        memeber.save()
        
        return redirect('/index')  # Redirect to the list of subjects after successful creation
    
    return render(request, 'Admission.html')

def view_subject(request):
    subject_item = memebers.objects.all()
    return render(request,'view_subject.html',{'subject_item':subject_item})

def deletedata(request):
    id = request.GET.get('id')
    AdmissionList = memebers.objects.get(id=id)
    AdmissionList.delete()
    return HttpResponseRedirect('/view_details/')

def editdata(request):
    id = request.GET.get('id')
    AdmissionList = memebers.objects.filter(id=id).all()
    return render(request,'edit_admissionForm.html',{'AdmissionList':AdmissionList})

def approval(request):
    id = request.GET.get('id')
    AdmissionList = memebers.objects.get(id=id)
    if AdmissionList.approval == False:
        id = AdmissionList.id
        email = AdmissionList.email
        AdmissionList.approval = True
        AdmissionList.save()
        subject = "Welcome to Admission Management - Login!!"
        message = "Your Icard Ready\nCheck Out Your Icard\nhttp://127.0.0.1:8000/Icard/"+str(id)+"/"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)
    else:
        AdmissionList.approval = False
        AdmissionList.save()    
    return redirect('/view_details')

def updatedata(request):
    memebers_model = memebers()
    memebers_model.id = request.POST.get('id')
    memebers_model.name = request.POST.get('change_name')
    memebers_model.Addhar_no = request.POST.get('change_addhar_card')
    memebers_model.phone_no = request.POST.get('change_phone_no')
    memebers_model.email = request.POST.get('change_email')
    memebers_model.religion = request.POST.get('change_religion')
    memebers_model.Address = request.POST.get('change_address')
    memebers_model.Gender = request.POST.get('Gender')
    memebers_model.dob = request.POST.get('DOB')
    memebers_model.blood = request.POST.get('blood_grp')
    memebers_model.entry = request.POST.get('entry_level')
    memebers_model.cource = request.POST.get('Course_Preference')
    memebers_model.save()

    messages.success(request,'Admission Form Data were Changed!!')
    return HttpResponseRedirect('/view_details/')

def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username):
            messages.error(request,"Username already exist! Please try some "
                                   "other username")
            return redirect('signup')

        if len(username)>18:
            messages.error(request,"Username must be under 18 character")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request,"Password didn't match")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!")
            return redirect('signup')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.save()

        messages.success(request,"Your Account has been successfully "
                                 "created. We have sent you a confirmation "
                                 "email, please confirm your email in order "
                                 "to activate your account.")

        #welcome Email
        subject = "Welcome to Admission Management - Login!!"
        message = "Hello"+ myuser.first_name + "!! \n" + "welcome to Admission management!! \n Thank you for visiting our website \n we have also sent you a confirmation email, please confirm your email adress in order to  active your account. \n\n  Thanking You \n Yash University"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)

        # #Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ Gravience management "
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain':current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')

    return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
       
            
        if user is not None:
            try:
                if user.is_superuser:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return redirect('/view_details/')
            except:
                pass
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged in Successfully")
            # return render(request,"index.html",{'fname':fname})
            return redirect('/')

        else:
            messages.error(request,"Please Verify your account")
            return redirect('signin')


    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('index')

def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        messages.success(request,f"{myuser.username} has been Verified!!")
        return redirect('/signin')
    else:
        return render(request,'activation_failed.html')

def Icard(request,id):
    data = memebers.objects.get(id=id)
    return render(request, 'Icard.html',{"data":data})

def mca(request):
    return render(request, 'mca.html')

def bca(request):
    return render(request, 'bca.html')

def mba(request):
    return render(request, 'mba.html')

def degree(request):
    return render(request, 'degree.html')

def sf(request):
    return render(request, 'sf.html')