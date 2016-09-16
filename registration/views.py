from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserRegister, JobSubmit, ApplicationSubmit, CompanyRegister, ProfileAdd, LogInCompany, LogInUser, SearchJob
from .models import JobSeeker, JobDetails, JobProvider, JobApplication, UserDetails
from django.utils import timezone


def checkuserlogin(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return HttpResponseRedirect('/registration/jobseeker/thanks/' , {"username" : username})
   else:
       return HttpResponseRedirect('/registration/login/user')


def checkcompanylogin(request):
   if request.session.has_key('companyname'):
      companyname = request.session['companyname']
      return HttpResponseRedirect('/registration/jobseeker/thanks/' , {"username" : companyname})
   else:
       return HttpResponseRedirect('/registration/login/company')

def get_user(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_name_temp = form.cleaned_data["user_name"]
            first_name_temp = form.cleaned_data["first_name"]
            last_name_temp = form.cleaned_data["last_name"]
            email_temp = form.cleaned_data["email"]
            password_temp = form.cleaned_data["password"]
            address_temp = form.cleaned_data["address"]
            contact_temp = form.cleaned_data["contact"]
            job_obj = JobSeeker.objects.create(user_name=user_name_temp, first_name=first_name_temp,
                                               last_name=last_name_temp,
                                               email_id=email_temp, password=password_temp,
                                               address=address_temp, contact_number=contact_temp)
            job_obj.save()

            return HttpResponseRedirect('/registration/jobseeker/thanks/')

    return render(request, 'register_user.html', {'form': form})


def get_comapny(request):
    form = CompanyRegister()
    if request.method == 'POST':
        form = CompanyRegister(request.POST)
        print("hello")

        if form.is_valid():
            user_name_temp = form.cleaned_data["company_name"]
            first_name_temp = form.cleaned_data["first_name"]
            last_name_temp = form.cleaned_data["last_name"]
            email_temp = form.cleaned_data["email"]
            password_temp = form.cleaned_data["password"]
            address_temp = form.cleaned_data["address"]
            contact_temp = form.cleaned_data["contact"]
            job_obj1 = JobProvider.objects.create(company_name=user_name_temp, first_name=first_name_temp,
                                                  last_name=last_name_temp,
                                                  email_id=email_temp, password=password_temp,
                                                  address=address_temp, contact_number=contact_temp)
            job_obj1.save()

            return HttpResponseRedirect('/registration/jobprovider/thanks/')

    return render(request, 'register_company.html', {'form': form})


def thanks(request):
    return HttpResponse("Thanks for the Registration you will be redirected to your profile")


def get_job(request):
    form = JobSubmit()
    if request.method == 'POST':
        form = JobSubmit(request.POST)
        print(form.is_valid())
        if form.is_valid():
            company_name = "kunal organisation"
            genre = form.cleaned_data["genre"]
            details = form.cleaned_data["details"]
            pay = form.cleaned_data["pay"]
            dead_line = form.cleaned_data["dead_line"]
            pub_date = timezone.now()
        temp = JobDetails.objects.create(company_name=company_name, genre=genre, details=details, pay=pay,
                                         deadline=dead_line, pub_date=pub_date)
        temp.save()
        return HttpResponseRedirect('/registration/jobseeker/thanks/')

    return render(request, 'JobSubmit/JobSubmit.html', {'form': form})


def get_application(request):
    form = ApplicationSubmit()
    if request.method == 'POST':
        form = ApplicationSubmit(request.POST)
        print (form.is_valid())
        if form.is_valid():
            application = form.cleaned_data["application"]
            pay_expected = form.cleaned_data["pay_expected"]
        temp = JobApplication.objects.create(user_name="kunal", application_text=application,
                                             pay_expected=pay_expected, status=False)
        temp.save()
        return HttpResponseRedirect('/registration/jobseeker/thanks/')

    return render(request, 'JobApplication/JobApplication.html', {'form': form})


def edit_profile(request):
    form = ProfileAdd()
    if request.method == 'POST':
        form = ProfileAdd(request.POST, request.FILES)
        print (form.is_valid())

        profile_img = form.cleaned_data['profile_img']
        website_linked = form.cleaned_data['website_linked']
        user_introduction = form.cleaned_data['user_introduction']
        temp = UserDetails.objects.create(user_name="user_name_temp", first_name='first_name_temp',
                                          last_name='last_name_temp',
                                          email_id='email_temp@gmail.com', address='address_temp',
                                          contact_number=9012670877, img=profile_img,
                                          website_linked=website_linked, user_introduction=user_introduction)

        temp.save()
        return HttpResponseRedirect('/registration/jobseeker/thanks/')
    return render(request, 'ProfileEdit.html', {'form': form})


def login_user(request):
    form = LogInUser()
    if request.method == 'POST':
        form = LogInUser(request.POST)
        if form.is_valid():

            username_tmp = form.cleaned_data["user_name"]
            password_tmp = form.cleaned_data["password"]
            try:
                username_check = JobSeeker.objects.get(user_name=username_tmp)
                if username_check.password == password_tmp:
                    request.session['username'] = username_tmp
                    return HttpResponseRedirect('/registration/userprofile/')
                else:
                    return HttpResponseRedirect('/registration/loginuser/')
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/registration/loginuser/')

    return render(request, 'JobApplication/JobApplication.html', {'form': form})


def login_Company(request):
    form = LogInCompany()
    if request.method == 'POST':
        form = LogInCompany(request.POST)
        if form.is_valid():
            companyname_tmp = form.cleaned_data["company_name"]
            password_tmp = form.cleaned_data["password"]
            try:
                Companyname_check = JobProvider.objects.get(company_name=companyname_tmp)
                if Companyname_check.password == password_tmp:
                    request.session['companyname'] = companyname_tmp
                    return HttpResponse("successful")
                else:
                    return HttpResponse("unsuccessful")
            except ObjectDoesNotExist:
                return HttpResponse("unsuccesful")

    return render(request, 'JobApplication/JobApplication.html', {'form': form})


def search_job(request):
    form = SearchJob()
    if request.method == 'POST':
        form = SearchJob(request.POST)
        if form.is_valid():
            search_tmp = form.cleaned_data["search"]
            pay_tmp = form.cleaned_data["pay_Salary"]
            try:
                search_check = JobDetails.objects.get(genre=search_tmp)
                if search_check.pay == pay_tmp:
                    return HttpResponse("Search successfull")
                else:
                    return HttpResponse("Seach Not Found")

            except:
                return HttpResponse("Search Not Found")

    return render(request, 'JobApplication/JobApplication.html', {'form': form})



def userprofile(request):
    username = request.session['username']
    username_temp = UserDetails.objects.get(user_name=username)


    return render(request, 'profile.html',{'user':username_temp})


def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")