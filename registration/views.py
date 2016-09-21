from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserRegister, JobSubmit, ApplicationSubmit, CompanyRegister, ProfileAdd, LogInCompany, LogInUser, \
    SearchJob
from .models import JobSeeker, JobDetails, JobProvider, JobApplication, UserDetails
from django.utils import timezone
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from django.conf import settings
from django.core.mail import send_mail


def checkuserlogin(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return HttpResponseRedirect('/registration/jobseeker/thanks/', {"username": username})
    else:
        return HttpResponseRedirect('/registration/login/user')


def checkcompanylogin(request):
    if request.session.has_key('companyname'):
        companyname = request.session['companyname']
        return HttpResponseRedirect('/registration/jobseeker/thanks/', {"username": companyname})
    else:
        return HttpResponseRedirect('/registration/login/company')


def get_user(request):
    form = UserRegister()
    if (request.session.has_key('username') or request.session.has_key('companyname')):
        x = "off"

    else:
        x = "on"
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print(form.is_valid())
        try:
            if form.is_valid():
                user_name_temp = form.cleaned_data["user_name"]
                first_name_temp = form.cleaned_data["first_name"]
                last_name_temp = form.cleaned_data["last_name"]
                email_temp = form.cleaned_data["email"]
                password_temp = form.cleaned_data["password"]
                enc_password = pbkdf2_sha256.encrypt(password_temp)
                address_temp = form.cleaned_data["address"]
                contact_temp = form.cleaned_data["contact"]
                job_obj = JobSeeker.objects.create(user_name=user_name_temp, first_name=first_name_temp,
                                                   last_name=last_name_temp,
                                                   email_id=email_temp, password=enc_password,
                                                   address=address_temp, contact_number=contact_temp)
                request.session['username'] = user_name_temp
                job_obj.save()
                try:
                    subject = "Thankyou"
                    message = "Thanks for Your Registration on Scribber"
                    from_email = settings.EMAIL_HOST_USER

                    send_mail(subject, message, from_email, [email_temp], fail_silently=False)
                except:
                    messages.error(request, 'Not Connected to internet or invalid email id provided ')
                print("hello")
                return HttpResponseRedirect('/registration/userprofile/edit/')
        except:
            messages.error(request, 'This Username already exits')

    return render(request, 'register_user.html', {'form': form, 'flag': x})


def get_comapny(request):
    form = CompanyRegister()
    if (request.session.has_key('username') or request.session.has_key('companyname')):
        x = "off"

    else:
        x = "on"
    if request.method == 'POST':
        form = CompanyRegister(request.POST)
        try:
            if form.is_valid():
                user_name_temp = form.cleaned_data["company_name"]
                first_name_temp = form.cleaned_data["first_name"]
                last_name_temp = form.cleaned_data["last_name"]
                email_temp = form.cleaned_data["email"]
                password_temp = form.cleaned_data["password"]
                enc_password = pbkdf2_sha256.encrypt(password_temp)
                address_temp = form.cleaned_data["address"]
                contact_temp = form.cleaned_data["contact"]
                request.session['companyname'] = user_name_temp
                job_obj1 = JobProvider.objects.create(company_name=user_name_temp, first_name=first_name_temp,
                                                      last_name=last_name_temp,
                                                      email_id=email_temp, password=enc_password,
                                                      address=address_temp, contact_number=contact_temp)
                job_obj1.save()
                try:
                    subject = "Thankyou"
                    message = "Thanks for Your Registration on Scribber"
                    from_email = settings.EMAIL_HOST_USER

                    send_mail(subject, message, from_email, [email_temp], fail_silently=False)
                except:
                    messages.error(request, 'Not Connected to internet or invalid email id provided ')

                return HttpResponseRedirect('/registration/companyprofile/edit/')
        except:
            messages.error(request, 'This CompanyName already exits')
    return render(request, 'register_company.html', {'form': form, 'flag': x})


def thanks(request):
    return render(request, 'loggedIn.html')


def get_job(request):
    form = JobSubmit()
    try:
        if (request.session['companyname']):
                check = "on"
    except:
        check = "off"
    if request.method == 'POST':
        form = JobSubmit(request.POST)
        print(form.is_valid())
        try:
            username = request.session['companyname']
            if form.is_valid():

                company_name = username
                genre = form.cleaned_data["genre"]
                details = form.cleaned_data["details"]
                pay = form.cleaned_data["pay"]
                dead_line = form.cleaned_data["dead_line"]
                pub_date = timezone.now()
            temp = JobDetails.objects.create(company_name=company_name, genre=genre, details=details, pay=pay,
                                             deadline=dead_line, pub_date=pub_date)
            temp.save()
            return HttpResponseRedirect('/registration/companyprofile/')
        except:
            messages.error(request, 'Looks like you are Not Logged in')
    return render(request, 'post_job.html', {'form': form,'post':check})


def get_application(request, details):
    form = ApplicationSubmit()
    try:
        if (request.session['username']):
            check = "on"
    except:
        check = "off"
    if request.method == 'POST':
        form = ApplicationSubmit(request.POST)

        if form.is_valid():
            username = request.session["username"]
            application = form.cleaned_data["application"]
            pay_expected = form.cleaned_data["pay_expected"]
            active_job = JobDetails.objects.get(details=details)
            active_user = JobSeeker.objects.get(user_name=username)
            try :
                user_check = JobApplication.objects.get(details=active_job.details,user_name=username)
                x = user_check.user_name
                print (x)
            except:
                x = 'null'

            if x == username:
                messages.error(request,'You have already submitted an application for this job')
                return HttpResponseRedirect('/registration/userprofile/')
            else :

                print(active_job.details)
                temp = JobApplication.objects.create(company_name=active_job.company_name,
                                                     email_user=active_user.email_id,
                                                     details=active_job.details, user_name=username,
                                                     application_text=application,
                                                     pay_expected=pay_expected, status=False)
                temp.save()
                messages.success(request, "Application submitted successfully")
                return HttpResponseRedirect('/registration/applicationview/')
    return render(request, 'post_application.html', {'form': form,'show':check})


def edit_profile_user(request):
    form = ProfileAdd()
    if request.method == 'POST':
        form = ProfileAdd(request.POST, request.FILES)
        print (form.is_valid())
        profile_img = form.cleaned_data['profile_img']
        website_linked = form.cleaned_data['website_linked']
        user_introduction = form.cleaned_data['user_introduction']
        username = request.session['username']
        user_temp = JobSeeker.objects.get(user_name=username)
        temp = UserDetails.objects.create(user_name=user_temp.user_name, first_name=user_temp.first_name,
                                          last_name=user_temp.last_name,
                                          email_id=user_temp.email_id, address=user_temp.address,
                                          contact_number=user_temp.contact_number, img=profile_img,
                                          website_linked=website_linked, user_introduction=user_introduction)

        temp.save()
        return HttpResponseRedirect('/registration/userprofile/')
    return render(request, 'ProfileEdit.html', {'form': form})


def edit_profile_company(request):
    form = ProfileAdd()
    try:
        if request.method == 'POST':
            form = ProfileAdd(request.POST, request.FILES)
            print (form.is_valid())
            profile_img = form.cleaned_data['profile_img']
            website_linked = form.cleaned_data['website_linked']
            user_introduction = form.cleaned_data['user_introduction']
            username_temp = request.session['companyname']
            user_temp = JobProvider.objects.get(company_name=username_temp)
            temp = UserDetails.objects.create(user_name=user_temp.company_name, first_name=user_temp.first_name,
                                              last_name=user_temp.last_name,
                                              email_id=user_temp.email_id, address=user_temp.address,
                                              contact_number=user_temp.contact_number, img=profile_img,
                                              website_linked=website_linked, user_introduction=user_introduction)

            temp.save()
            return HttpResponseRedirect('/registration/companyprofile/')
    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')

    return render(request, 'ProfileEdit.html', {'form': form})


def login_user(request):
    form = LogInUser()
    if (request.session.has_key('username') or request.session.has_key('companyname')):
        x = "off"

    else:
        x = "on"
    if request.method == 'POST':
        form = LogInUser(request.POST)
        if form.is_valid():

            username_tmp = form.cleaned_data["user_name"]
            password_tmp = form.cleaned_data["password"]
            try:
                username_check = JobSeeker.objects.get(user_name=username_tmp)
                if pbkdf2_sha256.verify(password_tmp, username_check.password):
                    request.session['username'] = username_tmp
                    return HttpResponseRedirect('/registration/userprofile/')
                else:
                    messages.error(request, "Password Incorrect")
            except ObjectDoesNotExist:
                messages.error(request, "SignUp First")

    return render(request, 'login_user.html', {'form': form, 'flag': x})


def login_Company(request):
    form = LogInCompany()
    if (request.session.has_key('username') or request.session.has_key('companyname')):
        x = "off"

    else:
        x = "on"
    if request.method == 'POST':
        form = LogInCompany(request.POST)
        if form.is_valid():
            companyname_tmp = form.cleaned_data["company_name"]
            password_tmp = form.cleaned_data["password"]
            try:
                Companyname_check = JobProvider.objects.get(company_name=companyname_tmp)
                if pbkdf2_sha256.verify(password_tmp, Companyname_check.password):
                    request.session['companyname'] = companyname_tmp
                    return HttpResponseRedirect('/registration/companyprofile/')
                else:
                    messages.error(request, "Password Incorrect")
            except ObjectDoesNotExist:
                messages.error(request, "SignUp First")

    return render(request, 'login_company.html', {'form': form, 'flag': x})


def displayjob(request):
    try:
        username = request.session['companyname']
        job_temp = JobDetails.objects.filter(company_name=username)
        return render(request, 'job_view.html', {'user': job_temp})

    except:
        return HttpResponse('unsucessful')


def displayapplication(request):
    try:
        username = request.session['username']
        app_temp = JobApplication.objects.filter(user_name=username)
        return render(request, 'application_view.html', {'user': app_temp})

    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')


def submitted_application(request):
    try:
        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"
        username = request.session['companyname']
        app_temp = JobApplication.objects.filter(company_name=username)
        return render(request, 'submitted_application.html', {'user': app_temp, 'flag': x})

    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')


def accepting_letter(request, text):
    try:
        accepted_user = JobApplication.objects.get(application_text=text)
        email_temp = accepted_user.email_user
        subject = "Confirmation Letter "
        message = "Your Job submitted for the job " + accepted_user.details + "for the company" + accepted_user.company_name + "has been accepted . Congratulations !!!!!"

        from_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, [email_temp], fail_silently=False)
        messages.success(request, "Email Sent")
        return HttpResponseRedirect('/registration/companyprofile/')
    except:
        messages.error(request, 'Not Connected to internet or invalid email id provided ')


def update_profile_user(request):
    form = ProfileAdd()
    try:
        if request.method == 'POST':
            form = ProfileAdd(request.POST, request.FILES)
            print (form.is_valid())
            profile_img = form.cleaned_data['profile_img']
            website_linked = form.cleaned_data['website_linked']
            user_introduction = form.cleaned_data['user_introduction']
            username_temp = request.session['username']
            user_temp = UserDetails.objects.get(user_name=username_temp)
            user_temp.img = profile_img
            user_temp.save()
            user_temp.website_linked = website_linked
            user_temp.user_introduction = user_introduction
            user_temp.save()
            print (user_temp.website_linked)
            return HttpResponseRedirect('/registration/userprofile/')
    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')
    return render(request, 'ProfileEdit.html', {'form': form})


def update_profile_company(request):
    form = ProfileAdd()
    try:
        if request.method == 'POST':
            form = ProfileAdd(request.POST, request.FILES)
            print (form.is_valid())
            profile_img = form.cleaned_data['profile_img']
            website_linked = form.cleaned_data['website_linked']
            user_introduction = form.cleaned_data['user_introduction']
            username_temp = request.session['companyname']
            user_temp = UserDetails.objects.get(user_name=username_temp)
            user_temp.img = profile_img
            user_temp.save()
            user_temp.website_linked = website_linked
            user_temp.user_introduction = user_introduction
            user_temp.save()
            print (user_temp.website_linked)
            return HttpResponseRedirect('/registration/companyprofile/')
    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')
    return render(request, 'ProfileEdit.html', {'form': form})


def search_job(request):
    form = SearchJob()
    try:
        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"
        if request.method == 'POST':
            form = SearchJob(request.POST)
            if form.is_valid():
                search_tmp = form.cleaned_data["search"]
                pay_tmp = form.cleaned_data["pay_Salary"]
                list_job = JobDetails.objects.filter(genre=search_tmp)
                return render(request, 'search.html', {'list': list_job , 'flag': x})

    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')
    list_job = JobDetails.objects.all()
    return render(request, 'search.html', {'form': form, 'flag': x ,'list':list_job })


def userprofile(request):

        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"

        username = request.session['username']
        username_temp = UserDetails.objects.get(user_name=username)
        return render(request, 'profile_user.html', {'user': username_temp, 'flag': x})

        return HttpResponseRedirect('/registration/jobseeker/thanks/')


def companyprofile(request):
    try:
        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"

        username = request.session['companyname']
        username_temp = UserDetails.objects.get(user_name=username)
        return render(request, 'profile_company.html', {'user': username_temp, 'flag': x})
    except:
        return HttpResponseRedirect('/registration/jobseeker/thanks/')


def home(request):
    if (request.session.has_key('username') or request.session.has_key('companyname')):
        x = "off"

    else:
        x = "on"
    print (x)
    return render(request, 'Home.html', {'flag': x})


def logout(request):
    try:
        del request.session['username']
        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"

        return render(request, 'Home.html', {'flag': x})

    except:
        del request.session['companyname']
        if (request.session.has_key('username') or request.session.has_key('companyname')):
            x = "off"

        else:
            x = "on"

        return render(request, 'Home.html', {'flag': x})
    finally:
        pass
