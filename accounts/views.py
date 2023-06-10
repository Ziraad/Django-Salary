from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from company.forms import CompanyForm
from company.models import Company
from .models import UserBase

# from SafeBox import settings
# from accounts.forms import MyUserForm, ProfileForm, PasswordForm, RegisterForm
# from accounts.models import Profile
# from orders.models import Order

# VERIFICATION EMAIL
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


@login_required
def dashboard(request):
    return render(request, 'accounts/index.html')


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        print('login for')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('salary:home_page')
            return HttpResponseRedirect(redirect_url)
        else:
            # undefined user or wrong password
            context = {
                'email': email,
                'error': 'کاربری با این مشخصات یافت نشد!'
            }
    else:
        context = {
        }
    return render(request, 'accounts/pages/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('salary:home_page'))


@login_required
def profile_details(request):
    profile = request.user
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile_details.html', context)


def register_user(request):
    users = UserBase.objects.all()
    usernames = [i.username.lower() for i in users]
    emails = [i.email for i in users]
    res = None
    # if request.method == 'POST' and request.is_ajax():
    #     register_form = RegisterForm(data=request.POST)
    #     email = request.POST.get('email')
    #     username = request.POST.get('username')
    #     username = username.lower()
    #     password = request.POST.get('password')
    #     if register_form.is_valid():
    #         try:
    #             assert email not in emails, 'این ایمیل از قبل وجود داشته است!'
    #             assert username not in usernames, 'این نام کاربری از قبل وجود داشته است!'
    #             user = User.objects.create_user(username=username, password=password, email=email)
    #             user.is_staff = True
    #             user.save()
    #             Profile.objects.create(user=user)
    #             res = 'حساب شما با موفقیت ایجاد شد'
    #         except Exception as e:
    #             res = str(e)
    #         return JsonResponse({'data': res}, safe=False)
    # else:
    #     register_form = RegisterForm()
    # context = {
    #     'register_form': register_form,
    #     'message': res,
    #     'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY,
    # }

    return render(request, 'accounts/pages/create-account.html')


# @login_required
# def profile_edit(request):
#     profile = request.user.profile

#     context = {
#         'profile': profile,
#     }

#     if request.method == 'POST':
#         print('in post form')
#         user_form = MyUserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             context['message'] = 'success'
#             return JsonResponse({'data': 'اطلاعات با موفقیت ویرایش شد'}, safe=False)
#         else:
#             context['message'] = 'error'
#             return JsonResponse({'error': 'در ثبت اطلاعات خطایی رخ داده است!'}, safe=False)

#     else:
#         user_form = MyUserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)

#     context['user_form'] = user_form
#     context['profile_form'] = profile_form

#     return render(request, 'accounts/profile_edit.html', context)


# def orders(request):
#     my_orders = Order.objects.filter(customer=request.user.profile)
#     shopping = my_orders.filter(status=1)
#     registered = my_orders.filter(status=2)

#     if request.method == 'POST':
#         order_number = request.POST.get('order_number')
#         order = Order.objects.get(order_number=order_number)
#         order.status = 3
#         order.save()

#     context = {
#         'my_orders': my_orders,
#         'shopping': shopping,
#         'registered': registered,
#     }
#     return render(request, 'accounts/my_orders.html', context)


# @login_required
# def change_pass(request):
#     profile = request.user.profile
#     message = None
#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد!')
#             message = 'success'
#             # return redirect('accounts:change_pass')
#         else:
#             messages.error(request, 'لطفاً خطاهای زیر را تصحیح کنید.')
#             message = 'error'
#     else:
#         form = PasswordForm(request.user)

#     context = {
#         'form': form,
#         'profile': profile,
#         'message': message,
#     }
#     return render(request, 'accounts/change_pass.html', context=context)


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        print('email: ', email)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            # Reset Password
            current_site = get_current_site(request)
            mail_subject = 'بازنشانی گذرواژه'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            print('after message')
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            print('before send email')
            send_email.send()
            print('send email successfully')
            # END Reset Password

            messages.success(request, 'ایمیل بازنشانی گذرواژه به آدرس ایمیل شما ارسال شد!')
            return redirect('accounts:login')

        else:
            messages.error(request, 'حساب کاربری وجود ندارد!')
            return redirect('accounts:forgot_password')

    return render(request, 'accounts/pages/forgot-password.html')

# def reset_password_validate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User._default_manager.get(pk=uid)
#         print('user: ', user)
#     except(TypeError, ValueError, OverflowError, Profile.DoesNotExist):
#         user = None
#         print('user empty')

#     if user is not None and default_token_generator.check_token(user, token):
#         print('is user')
#         request.session['uid'] = uid
#         messages.success(request, 'لطفاً گذرواژه خود را بازنشانی کنید!')
#         return redirect('accounts:reset_password')
#     else:
#         print('user noting')
#         messages.error(request, 'این لینک منقضی شده است!')
#         return redirect('accounts:login')


# def reset_password(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             uid = request.session.get('uid')
#             user = User.objects.get(pk=uid)
#             user.set_password(password)
#             user.save()
#             messages.success(request, 'بازنشانی پسورد با موفقیت انجام شد!')
#             return redirect('accounts:login')
#         else:
#             messages.error(request, 'گذرواژه همخوانی ندارد!')
#             return redirect('accounts:reset_password')
#     else:
#         return render(request, 'accounts/resetPassword.html')
