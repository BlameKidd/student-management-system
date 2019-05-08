from django.shortcuts import render, redirect
from app.models import Classes


def classes_list(request):
    classes_obj = Classes.objects.all()
    return render(request, 'classes/classes_list.html', {'classes_obj': classes_obj})


def add_classes(request):
    return


def delete_classes(request):
    return


def edit_classes(request):
    return
