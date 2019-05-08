from django.shortcuts import render, redirect, HttpResponse
from app.models import Classes


def classes_list(request):
    classes_obj = Classes.objects.all()
    return render(request, 'classes/classes_list.html', {'classes_obj': classes_obj})


def add_classes(request):
    if request.method == 'POST':
        classes_name = request.POST.get('classes_name')
        Classes.objects.create(name=classes_name)
        return redirect('/classes_list/')
    return render(request, 'classes/add_classes.html')


def delete_classes(request):
    delete_classes_id = request.GET.get('id')
    Classes.objects.filter(id=delete_classes_id).delete()
    return redirect('/classes_list/')


def edit_classes(request):
    edit_classes_id = request.GET.get('id')
    edit_classes_obj = Classes.objects.get(id=edit_classes_id)
    if request.method == 'POST':
        new_classes_name = request.POST.get('classes_name')
        edit_classes_obj.name = new_classes_name
        edit_classes_obj.save()
        return redirect('/classes_list/')
    return render(request, 'classes/edit_classes.html', {'edit_classes_obj': edit_classes_obj})
