from decimal import Context
from django.contrib.auth import  login, authenticate,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm,SigninForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            contact_no = form.cleaned_data.get('contact_no')
            city = form.cleaned_data.get('city')
            country = form.cleaned_data.get('country')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            tempvar=form.cleaned_data.get('checkbx')
            if tempvar is True:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                Profile(user=User.objects.filter(username=username).first(),gender=gender,contact_no=contact_no,city=city,country=country).save()
                user.is_active = False
                current_site = get_current_site(request)
                mail_subject = 'Activate your MCQhero account.'
                message = render_to_string('account/acc_active_email.html', {
                    'user': user,
                    'domain': "127.0.0.1:8000",
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                email1=form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[email1]
                )
                email.send()
                return render(request,'account/confirmemail.html',)
    else:
        form = RegisterForm()

    return render(request, 'account/signup.html',{"form":form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('/')

    else:
        return HttpResponse('Activation link is invalid!')
        
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user=authenticate(username=User.objects.get(email=username),password=password)
            except:
                user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Congratulation,Logged in successfully !!')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                 return redirect("/") 

    else:
        form = SigninForm()
   
    return render(request,'account/signin.html',{"form":form})




def signout(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/signin/')
def profileview(request):
   
    return render(request,'account/profileview.html')

@login_required(login_url='/signin/')
def editprofile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("/profile")
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'account/editprofile.html',context)



    