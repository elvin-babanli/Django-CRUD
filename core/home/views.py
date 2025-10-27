from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

def index(request):
    edit_id = request.GET.get('edit')
    if request.method == 'GET' and edit_id:
        obj = get_object_or_404(Person, id=edit_id)
        return render(request, 'index.html', {'person': obj, 'is_edit': True})
    
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')

        if person_id:
            obj = get_object_or_404(Person, id=person_id)
            obj.name = name
            obj.surname = surname
            obj.email = email
            obj.save()
            return redirect('/data/')
        else:
            Person.objects.create(name=name, surname=surname, email=email)
            return redirect('/')

    return render(request, 'index.html')

def get_data(request):
    people = Person.objects.all()
    return render(request, 'data.html', {'data': people})


def update_data(request, person_id):
    obj = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.surname = request.POST.get('surname')
        obj.email = request.POST.get('email')
        obj.save()
        return redirect('/data/')
    return render(request, 'update.html', {'data': obj})


def delete_data(request, person_id):
    obj = get_object_or_404(Person, id=person_id)
    obj.delete()
    return redirect('/data/')
