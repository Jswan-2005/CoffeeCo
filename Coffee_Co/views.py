from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeType, CoffeeRecipeEntry
from .forms import CoffeeTypeForm, CoffeeRecipeEntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    '''The home page for CoffeeCo'''
    return render(request, 'Coffee_Co/index.html')

@login_required
def coffeeTypes(request):
    '''Shows all Coffee Types and its entries'''
    coffeeTypes = CoffeeType.objects.filter(owner = request.user).order_by('date_added')
    context = {'coffeeTypes': coffeeTypes}
    return render(request, 'Coffee_Co/coffeeTypes.html', context)

@login_required
def coffeeType(request, coffeeType_id):
    '''Show a single Coffee Type and its entries'''
    coffeeType = get_object_or_404(CoffeeType, id=coffeeType_id)

    if coffeeType.owner != request.user:
        raise Http404

    entries = coffeeType.coffeerecipeentry_set.order_by('-date_added')
    context = {'coffeeType': coffeeType, 'entries': entries}
    return render(request, 'Coffee_Co/coffeeType.html', context)

@login_required
def newCoffeeType(request):
    '''Add a new coffee type'''
    if request.method != 'POST':
        form = CoffeeTypeForm()
    else:
        form = CoffeeTypeForm(data=request.POST)
        if form.is_valid():
            coffee_type = form.save(commit=False)
            coffee_type.owner = request.user
            coffee_type.save()
            return redirect('Coffee_Co:coffeeTypes')

    context = {'form': form}
    return render(request, 'Coffee_Co/newCoffeeType.html', context)

@login_required
def newCoffeeRecipe(request, coffeeType_id):
    '''Add a new recipe for a Coffee Type'''
    coffeeType = CoffeeType.objects.get(id=coffeeType_id)

    if request.method != 'POST':
        form = CoffeeRecipeEntryForm()
    else:
        form = CoffeeRecipeEntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.coffeeType = coffeeType
            new_entry.save()
            return redirect('Coffee_Co:coffeeType', coffeeType_id=coffeeType_id)

    context = {'coffeeType': coffeeType, 'form': form}
    return render(request, 'Coffee_Co/newCoffeeRecipe.html', context)

@login_required
def editCoffeeRecipe(request, recipe_id):
    recipe = CoffeeRecipeEntry.objects.get(id=recipe_id)
    coffeeType = recipe.coffeeType

    if coffeeType.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = CoffeeRecipeEntryForm(instance=recipe)
    else:
        form = CoffeeRecipeEntryForm(instance=recipe, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Coffee_Co:coffeeType', coffeeType_id=coffeeType.id)

    context = {'recipe': recipe, 'coffeeType': coffeeType, 'form': form}
    return render(request, 'Coffee_Co/editCoffeeRecipe.html', context)

'''No login required for this page'''
def coffee_info(request):
    return render(request, 'Coffee_Co/coffeeInfo.html')


