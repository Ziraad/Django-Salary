from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from company.forms import CompanyForm
from company.models import Company


def company(request):
    companies = Company.objects.filter(accountant=request.user)
    context = {
        'companies': companies,
    }
    if request.method == 'POST':
        print('in post request')
        if 'activate' in request.POST:
            print('activate')
            company_slug = request.POST['activate']
            get_company = get_object_or_404(Company, slug=company_slug)
            get_company.is_active = True
            get_company.save()
        if 'deactivate' in request.POST:
            print('deactivate')
            company_slug = request.POST['deactivate']
            get_company = get_object_or_404(Company, slug=company_slug)
            get_company.is_active = False
            get_company.save()
        if 'delete' in request.POST:
            print('delete')
            company_slug = request.POST['delete']
            get_company = get_object_or_404(Company, slug=company_slug)
            get_company.delete()

        return redirect('accounts:companies:company')
    return render(request, 'company/companies.html', context)


def add_company(request):
    if request.method == 'POST':
        details = CompanyForm(request.POST, request.FILES)
        print('details: ', details.data)
        try:
            if details.is_valid():
                try:
                    new_company = details.save(commit=False)
                    name = request.POST.get('name')
                    slug_ = "-".join(name.split())
                    new_company.slug = slug_
                    new_company.accountant = request.user
                    new_company.save()
                    return redirect('accounts:companies:company')
                except Exception as e:
                    print('error: ', str(e))
            else:
                print('form is not valid')
                return render(request, 'company/new_company.html', {'form': details, 'error': 'فرم نامعتبر است!'})
        except Exception as e:
            return render(request, 'company/new_company.html', {'form': details, 'error': str(e)})

    else:
        form = CompanyForm()
        return render(request, 'company/new_company.html', {'form': form})


def company_detail(request, slug):
    company = Company.objects.get(slug=slug)
    context = {
        'company': company,
    }
    return render(request, 'company/company_detail.html', context=context)
