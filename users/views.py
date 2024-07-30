from .forms import UserForm, CustomerForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventory.models import Purchase
from django.contrib import messages
from .forms import CustomUserCreationForm


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        customer_form = CustomerForm(instance=request.user.customer_profile, data=request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        customer_form = CustomerForm(instance=request.user.customer_profile)
    return render(request, 'users/profile_edit.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # Get the current user
    user = request.user
    # Fetch purchased products for the user
    purchases = Purchase.objects.filter(user=user)

    # Pass the list of purchased products to the template
    context = {
        'purchases': purchases
    }
    return render(request, 'users/profile.html', context)
