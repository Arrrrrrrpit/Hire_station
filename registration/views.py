from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserRegister, JobSubmit, ApplicationSubmit
from .models import JobSeeker, JobDetails, JobApplication
from django.utils import timezone


def get_name(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_name_temp = form.cleaned_data["user_N"]
            first_name_temp = form.cleaned_data["first_N"]
            last_name_temp = form.cleaned_data["last_N"]
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

    return render(request, 'registration/name.html', {'form': form})


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
        temp = JobDetails.objects.create(company_name=company_name, job_id=1, genre=genre, details=details, pay=pay,
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
        temp = JobApplication.objects.create(user_name="kunal", job_id=1, application_text=application,
                                             pay_expected=pay_expected, status=False)
        temp.save()
        return HttpResponseRedirect('/registration/jobseeker/thanks/')

    return render(request, 'JobApplication/JobApplication.html', {'form': form})
