from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from person.forms import PersonForm, DecreeForm, SalaryReceiptForm
from person.models import Person
from salary.models import Decree, SalaryReceipt
from salary.views import represents_int
from django.template.defaulttags import register


def persons(request):
    all_person = Person.objects.filter(company__accountant=request.user)
    context = {
        'persons': all_person,
    }

    if request.method == 'POST':
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


def decrees(request):
    all_decrees = Decree.objects.filter(created_by=request.user)
    context = {
        'decrees': all_decrees,
    }
    if request.method == 'POST':
        if 'delete' in request.POST:
            print('delete')
            decree_id = request.POST['delete']
            get_decree = get_object_or_404(Decree, id=decree_id)
            get_decree.delete()
            return redirect('person:decrees')
    return render(request, 'person/decrees.html', context)


def add_decree(request):
    if request.method == 'POST':
        details = DecreeForm(request.POST, request=request)
        person = request.POST['person']
        year = request.POST['year']
        job_title = request.POST['job_title']
        base_salary = request.POST['base_salary']
        print('len job title: ', len(job_title))

        is_decree = Decree.objects.filter(person=person, year__exact=year)
        # get_person = Person.objects.get(__)
        # is_warrant = Warrant.objects.filter(Q(person=person) | Q(year__exact=year))
        print('decree: ', is_decree)
        try:
            get_person = Person.objects.get(id=person)
            print('person: ', person)
            assert get_person.is_active == True, 'برای صدور حکم، باید وضعیت کاربر تایید شده باشد!'
            assert not is_decree.exists(), 'برای این کاربر در سال مورد نظر قبلاً حکم صادر شده است!'
            assert len(year) > 0, 'سال را وارد کنید'
            assert represents_int(year), 'فرمت سال باید یک عدد صحیح 4 رقمی باشد'
            assert len(job_title) > 0, 'عنوان شغلی را وارد کنید'
            assert len(job_title) > 3, 'تعدا کاراکترهای عنوان شغلی باید از 3 بیشتر باشد'
            assert len(base_salary) > 0, 'حقوق پایه را وارد کنید'
            assert represents_int(base_salary), 'فرمت حقوق پایه باید یک عدد صحیح باشد!'
            if details.is_valid():
                print('form is valid')
                new_decree = details.save(commit=False)
                new_decree.created_by = request.user
                new_decree.save()
                return redirect('person:decrees')
        except Exception as e:
            print('form is not valid')
            return render(request, 'person/add_decree.html', {'form': details, 'error': str(e)})
    else:
        form = DecreeForm(request=request)
        return render(request, 'person/add_decree.html', {'form': form})


# def add_person_decree(request, personal_code):
#     if request.method == 'POST':
#         details = DecreeForm(request.POST, request=request, slug=personal_code)
#         person = request.POST['person']
#         year = request.POST['year']
#
#         is_decree = Decree.objects.filter(person=person, year__exact=year)
#         # get_person = Person.objects.get(__)
#         # is_warrant = Warrant.objects.filter(Q(person=person) | Q(year__exact=year))
#         print('decree: ', is_decree)
#         try:
#             get_person = Person.objects.get(personnel_code=personal_code)
#             print('person: ', person)
#             assert get_person.is_active == True, 'برای صدور حکم، باید وضعیت کاربر تایید شده باشد!'
#             assert not is_decree.exists(), 'برای این کاربر در سال مورد نظر قبلاً حکم صادر شده است!'
#             assert represents_int(request.POST['base_salary']), 'فرمت حقوق پایه باید یک عدد صحیح باشد!'
#             if details.is_valid():
#                 print('form is valid')
#                 new_decree = details.save(commit=False)
#                 new_decree.created_by = request.user
#                 new_decree.save()
#                 return redirect('person:decrees')
#         except Exception as e:
#             print('form is not valid')
#             return render(request, 'person/add_decree.html', {'form': details, 'error': str(e)})
#     else:
#         form = DecreeForm(request=request, slug=personal_code)
#         return render(request, 'person/add_decree.html', {'form': form})


def wages(request):
    all_wage = SalaryReceipt.objects.filter(created_by=request.user)

    context = {
        'wages': all_wage,
    }
    if request.method == 'POST':
        if 'delete' in request.POST:
            print('delete')
            wage_id = request.POST['delete']
            get_wage = get_object_or_404(SalaryReceipt, id=wage_id)
            get_wage.delete()
            return redirect('person:wages')
    return render(request, 'person/wages.html', context)


def add_wage(request):
    if request.method == 'POST':
        details = SalaryReceiptForm(request.POST, request=request)
        person = request.POST['person']
        month_name = request.POST['month_name']
        year = request.POST['year']
        working_days = request.POST['working_days']
        overtime = request.POST['overtime']
        closed_work = request.POST['closed_work']
        mission = request.POST['mission']

        weekly_days = {
            'Farvardin': '31',
            'Ordibehesht': '31',
            'Khordad': '31',
            'Tir': '31',
            'Mordad': '31',
            'Shahrivar': '31',
            'Mehr': '30',
            'Aban': '30',
            'Azar': '30',
            'Dey': '30',
            'Bahman': '30',
            'Esfand': '29',
        }

        try:
            assert len(year) > 0, 'سال را وارد کنید'
            assert represents_int(year), 'فرمت سال باید یک عدد صحیح 4 رقمی باشد'
            is_decree = Decree.objects.filter(person=person, year__exact=year)
            assert is_decree.exists(), 'برای این کاربر در سال مورد نظر هیچ حکمی صادر نشده است!'
            is_wage = SalaryReceipt.objects.filter(person=person, month_name__exact=month_name, year__exact=year)
            print('wage: ', is_wage)
            assert represents_int(working_days), 'فرمت روزهای کارکرد باید یک عدد صحیح باشد!'
            # number_of_days = 0
            for key, value in weekly_days.items():
                if month_name == key:
                    number_of_days = int(weekly_days[key])
                    assert int(working_days) <= number_of_days, \
                        f'تعداد روزهای ماه انتخاب شده نمی تواند از {number_of_days} بیشتر باشد!'
                    assert int(working_days) > 0, \
                        'روزهای کارکرد باید از 0 بیشتر باشد!'
                    break
            assert represents_int(overtime), 'فرمت اضافه کاری باید یک عدد صحیح باشد!'
            assert represents_int(closed_work), 'فرمت تعطیل کاری باید یک عدد صحیح باشد!'
            assert represents_int(mission), 'فرمت مأموریت باید یک عدد صحیح باشد!'
            assert not is_wage.exists(), 'برای این کاربر در سال و ماه مورد نظر قبلاً فیش حقوقی صادر شده است!'

        except Exception as e:
            print('form is not valid')
            return render(request, 'person/add_wage.html', {'form': details, 'error': str(e)})
        if details.is_valid():
            print('form is valid')
            new_wage = details.save(commit=False)
            new_wage.created_by = request.user
            new_wage.save()
            return redirect('person:wages')
        else:
            print('form is not valid')
            return render(request, 'person/add_wage.html', {'form': details, 'error': 'در ثبت فرم خطایی رخ داد!'})
    else:
        form = SalaryReceiptForm(request=request)
        return render(request, 'person/add_wage.html', {'form': form})


def wage_detail(request, wage_id):
    wage = get_object_or_404(SalaryReceipt, id=wage_id)
    context = {
        'wage': wage,
    }
    return render(request, 'salary/wage_detail.html', context)
