from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import job_S


def get_name(request):
     form=job_S()
     if request.method == 'POST':
        form = job_S(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/registration/jobseeker/thanks/')

     return render(request, 'registration/name.html', {'form': form})

def thanks(request):
    return HttpResponse("Thanks for the Registration")