from django.shortcuts import render


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def job_list(request):
    return HttpResponse("Available Jobs: Python Developer, Django Developer, React Developer, Data Analyst")
def job_details(request):
    return HttpResponse("Job Name: Python Developer | Company: ABC Technologies | Location: Kochi")
def contact(request):
    return HttpResponse("Contact us at jobportal@gmail.com")