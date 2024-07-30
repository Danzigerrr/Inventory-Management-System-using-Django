from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inventory.models import Product, Purchase


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
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
