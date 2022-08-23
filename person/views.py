from django.shortcuts import render, redirect

from person.forms import PersonForm
from person.models import Person


def persons(request):
    all_person = Person.objects.filter(company__accountant=request.user)
    context = {
        'persons': all_person,
    }
    return render(request, 'person/persons.html', context)


def add_person(request, *args, **kwargs):
    if request.method == 'POST':
        details = PersonForm(request.POST, request.FILES)
        print('details: ', details)

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
        # user = request.user
        form = PersonForm()
        return render(request, 'person/add_person.html', {'form': form})
