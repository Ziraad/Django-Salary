from django.shortcuts import render, redirect, get_object_or_404

from person.forms import PersonForm
from person.models import Person


def persons(request):
    all_person = Person.objects.filter(company__accountant=request.user)
    context = {
        'persons': all_person,
    }

    if request.method == 'POST':
        print('in post request')
        if 'activate' in request.POST:
            print('activate')
            personnel_code = request.POST['activate']
            get_person = get_object_or_404(Person, personnel_code=personnel_code)
            get_person.is_active = True
            get_person.save()
        if 'deactivate' in request.POST:
            print('deactivate')
            personnel_code = request.POST['deactivate']
            get_person = get_object_or_404(Person, personnel_code=personnel_code)
            get_person.is_active = False
            get_person.save()
        if 'delete' in request.POST:
            print('delete')
            personnel_code = request.POST['delete']
            get_person = get_object_or_404(Person, personnel_code=personnel_code)
            get_person.delete()

        return redirect('person:persons')
    return render(request, 'person/persons.html', context)


def add_person(request):
    if request.method == 'POST':
        details = PersonForm(request.POST, request.FILES, request=request)

        if details.is_valid():
            print('form is valid')
            new_person = details.save(commit=False)
            new_person.accountant = request.user
            new_person.save()
            return redirect('person:persons')
        else:
            print('form is not valid')
            return render(request, 'person/add_person.html', {'form': details, 'error': 'در ثبت فرم خطایی رخ داد!'})
    else:
        form = PersonForm(request=request)
        return render(request, 'person/add_person.html', {'form': form})
