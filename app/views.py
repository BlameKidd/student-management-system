from django.shortcuts import render, redirect
from app.models import Classes


def classes_list(request):
    classes_obj = Classes.objects.all()
    return render(request, 'classes/classes_list.html', {'classes_obj': classes_obj})


def add_classes(request):
    if request.method == 'POST':
        classes_name = request.POST.get('classes_name')
        Classes.objects.create(name=classes_name)
        redirect('/classes/classes_list/')
    return render(request, 'classes/add_classes.html')


def delete_classes(request):
    return


def edit_classes(request):
    return
