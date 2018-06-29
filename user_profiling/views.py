# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import UserProfile


# Create your views here.
def addView(request):
    return render(request, "user_profiling/add.html")


# Main Page
def IndexView(request):
    return render(request, "user_profiling/index.html")


# Search Data To Edit
def SearchView(request):
    return render(request, "user_profiling/search.html")


# Data View Input
def DataView(request):
    return render(request, "user_profiling/view_search.html")


# Delete Input
def deleteInput(request):
    return render(request, "user_profiling/deleteInput.html")


# Saving a new Entry
def SaveView(request):
    new_user = UserProfile()
    new_user.name = request.POST['name']
    new_user.age = request.POST['age']

    try:            # Check for Pre-existing Data
        UserProfile.objects.filter(name=request.POST['name'], age=request.POST['age'])[0]

    except:     # Exception if data not available
        new_user.address = request.POST['address']
        new_user.gender = request.POST['gender']
        new_user.experience = request.POST['experience']
        new_user.save()

        return HttpResponseRedirect(reverse("user_profiling:index"))
    else:
        return render(request, "user_profiling/add.html", {"error_val": True})


# Edit data
def EditView(request):
    try:
        name = request.POST['name']
        age = request.POST['age']
        main_obj = UserProfile.objects.filter(name=name, age=age)[0]
    except:
        return render(request, "user_profiling/search.html", {"error_val": True})
    else:
        return render(request, "user_profiling/edit.html", {"profile": main_obj})


# Delete Data
def deleteData(request):
    try:
        name = request.POST['name']
        age = request.POST['age']
        main_obj = UserProfile.objects.filter(name=name, age=age)
    except:
        return render(request, "user_profiling/deleteInput.html", {"error_val": True})
    else:
        main_obj.delete()
        return render(request, "user_profiling/successfulDelete.html")


# Search (ReadOnly)
def searchReadOnlyInputView(request):
    try:
        name = request.POST['name']
        age = request.POST['age']
        main_obj = UserProfile.objects.filter(name=name, age=age)[0]
    except:
        return render(request, "user_profiling/view_search.html", {"error_val": True})
    else:

        return render(request, "user_profiling/details.html", {"profile": main_obj})


# Save Edited data
def EditSave(request):
    new_user = UserProfile()
    new_user.name = request.POST['name']
    new_user.age = request.POST['age']
    new_user.address = request.POST['address']
    new_user.gender = request.POST['gender']
    new_user.experience = request.POST['experience']
    new_user.save()
    return HttpResponseRedirect(reverse("user_profiling:index"))






