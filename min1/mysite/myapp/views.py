from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'myapp/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Food, Consume


@login_required(login_url='login')
def index(request):

    foods = Food.objects.all()

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')

        # Safe lookup (no crash)
        food = get_object_or_404(Food, name=food_consumed)

        Consume.objects.create(
            user=request.user,
            food_consumed=food
        )

        return redirect('/')  # Prevent duplicate form submit

    consumed_food = Consume.objects.filter(user=request.user)

    return render(
        request,
        'myapp/index.html',
        {
            'foods': foods,
            'consumed_food': consumed_food
        }
    )


@login_required(login_url='login')
def delete_consume(request, id):

    consumed_food = get_object_or_404(
        Consume,
        id=id,
        user=request.user   # 🔒 user safety
    )

    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')

    return render(request, 'myapp/delete.html', {'item': consumed_food})