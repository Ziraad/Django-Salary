from django.http import HttpResponse
from django.shortcuts import render

from salary.forms import FreeSalaryForm
from salary.models import BaseInfo, SalaryReceipt


def home(request):

    return render(request, 'salary/home.html')


def salary(request):
    base_info = BaseInfo.objects.all().first()

    if request.method == 'POST':
        print('*******************')
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        month_name = request.POST['month_name'].strip()
        year = request.POST['year'].strip()
        company = request.POST['company'].strip()
        base_salary = request.POST['base_salary'].strip()
        working_days = request.POST['working_days'].strip()
        overtime = request.POST['overtime']
        closed_work = request.POST['closed_work'].strip()
        right_of_grocery = request.POST.getlist('right_of_grocery')
        right_of_house = request.POST.getlist('right_of_house')
        mission = request.POST['mission'].strip()
        reward = request.POST['reward'].strip()
        right_to_supervisor = request.POST.getlist('right_to_supervisor')
        number_of_children = request.POST['number_of_children'].strip()
        print('*******************')

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'month_name': month_name,
            'year': year,
            'company': company,
            'base_salary': base_salary,
            'working_days': working_days,
            'overtime': overtime,
            'closed_work': closed_work,
            'right_of_grocery': right_of_grocery,
            'mission': mission,
            'reward': reward,
            'right_to_supervisor': right_to_supervisor,
            'number_of_children': number_of_children,
        }

        weekly_days = {
            'فروردین': '31',
            'اردیبهشت': '31',
            'خرداد': '31',
            'تیر': '31',
            'مرداد': '31',
            'شهریور': '31',
            'مهر': '30',
            'آبان': '30',
            'آذر': '30',
            'دی': '30',
            'بهمن': '30',
            'اسفند': '29',
        }

        #
        def represents_int(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        try:
            assert first_name, 'لطفاً نام را وارد کنید!'
            assert len(first_name) >= 3, 'طول نام باید از 2 کاراکتر بیشتر باشد!'
            assert last_name, 'لطفاً نام خانوادگی را وارد کنید!'
            assert len(last_name) >= 2, 'طول نام خانوادگی باید از 2 کاراکتر بیشتر باشد!'
            assert represents_int(year), 'فرمت سال باید یک عدد صحیح 4 رقمی باشد'
            assert represents_int(base_salary), 'فرمت حقوق روزانه باید یک عدد صحیح باشد!'
            assert represents_int(working_days), 'فرمت روزهای کارکرد باید یک عدد صحیح باشد!'
            # number_of_days = 0
            for key, value in weekly_days.items():
                if month_name == key:
                    number_of_days = int(weekly_days[key])
                    assert int(working_days) <= number_of_days, f'تعداد روزهای ماه انتخاب شده باید { number_of_days } باشد'
                    break
            assert represents_int(overtime), 'فرمت اضافه کاری باید یک عدد صحیح باشد!'
            assert represents_int(closed_work), 'فرمت تعطیل کاری باید یک عدد صحیح باشد!'
            assert represents_int(mission), 'فرمت مأموریت باید یک عدد صحیح باشد!'
            assert represents_int(reward), 'فرمت پاداش باید یک عدد صحیح باشد!'
            assert represents_int(number_of_children), 'فرمت تعداد فرزندان مشمول باید یک عدد صحیح باشد!'

            calculate_salary = SalaryReceipt.calculate_free_salary(base_salary=base_salary, working_days=working_days,
                                                                   overtime=overtime, closed_work=closed_work,
                                                                   mission=mission, reward=reward,
                                                                   number_of_children=number_of_children)

            context['calculate_salary'] = calculate_salary

        except Exception as e:
            context['error'] = str(e)

    else:
        context = {
            'base_info': base_info,
        }

    return render(request, 'salary/salary_calculate.html', context)
