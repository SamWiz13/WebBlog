from django.shortcuts import render, get_object_or_404
from .models import Category,Pizza, PizzaNumbers, Chef

def home(request):
    #  All menu for index.html

    pizza = Pizza.objects.filter(category__slug ='pizza')[:6]
    pizza_number =PizzaNumbers.objects.all()
    catogories =Category.objects.all()

    context ={
        'pizza': pizza,
        'catogories': catogories,
        'pizza_number' : pizza_number,
    }
    return render(request, 'index.html', context)

def menu(request):
    #  Only pizza menu price 

    pizza =Pizza.objects.filter(category__slug ='pizza')[:8]

    context ={
        'pizza' : pizza
    }
    return render(request, 'menu.html', context)

def services(request):
    
    return render(request, 'services.html')

def about(request):
    pizza_number = PizzaNumbers.objects.all()
    chefs =Chef.objects.all()

    context ={
        'pizza_number' : pizza_number,
        'chefs' : chefs
    }
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def pizza_list(request, category_slug =None):
    category =None
    catogories =Category.objects.all()
    pizza =Pizza.objects.all()

    if category_slug:
        category =get_object_or_404(Category, slug =category_slug)
        pizza =pizza.filter(category =category)

    context ={
        'category':category,
        'categories':catogories,
        'pizza':pizza
    }

    return render(request, 'index.html', context)


def pizza_detail(request, id,slug):
    pizza =get_object_or_404(Pizza, id =id, slug =slug)

    context ={
        'pizza' :pizza
    }

    return render(request, 'pizza-detail.html', context)

