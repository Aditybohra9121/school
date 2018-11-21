# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import addStudentForm
from .models import Student
# Create your views here.
def index(request):
    stu=Student.objects.all()
    return render(request,"main/index.html",{'student':stu})
def add(request):
    form    =addStudentForm()
    if request.POST:
        form    =addStudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age =form.cleaned_data['age']
            gender=form.cleaned_data['age']
            form.save()
            return redirect('/index/')
    return render(request,"main/add.html",{'form':form})    