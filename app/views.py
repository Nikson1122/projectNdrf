from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import ProductForm, BuyProductForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

from .models import Event, Product, Order


# Create your views here.

def home(request):
    return render(request, 'app/base.html')

def about(request):
    return render(request, 'app/about.html')

def meeting(request):
    return render(request, 'app/meeting.html')

def contact(request):
    return render(request, 'app/contact.html')

def login_user(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)

         if user is not None:
             login(request, user)
             return redirect('events')
         else:
                return render(request, 'app/login.html', {'error': 'Invalid username or password'})
         
    return render(request, 'app/login.html')

@login_required
def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        pdf = request.FILES.get('pdf')

        Event.objects.create(
            title=title,
            description=description,
            pdf=pdf
        )

        return redirect('events')  # your event list page

    return render(request, 'app/event.html')

def event_list(request):
    events = Event.objects.order_by('title')  
    return render(request, 'app/upcomingevent.html', {'events': events})

def logout_user(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    
    if not getattr(request.user, 'is_app_admin', False):
        return HttpResponseForbidden("You are not allowed to access this page.")
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('addproduct') 
        
    else:
        form = ProductForm()  

    return render(request, 'app/addproduct.html', {'form': form})


def our_store(request):
    products = Product.objects.all()
    return render(request, 'app/ourstore.html', {'products': products})




def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    total_price = None
    success = False

    if request.method == "POST":
        form = BuyProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # Check if this is the "save_order" submission
            if request.POST.get("save_order"):
                Order.objects.create(
                    product=product,
                    customer_name=form.cleaned_data['customer_name'],
                    email=form.cleaned_data['email'],
                    phone_number=form.cleaned_data['phone_number'],
                    quantity=quantity,
                    total_price=total_price,
                )
                messages.success(request, "Order placed successfully!")
                return redirect('ourstore')

            # Step 1: calculation only
            success = True

    else:
        form = BuyProductForm(initial={
            'product_id': product.id,
            'product_name': product.name,
            'product_price': product.price,
        })

    return render(request, 'app/buy_product.html', {
        'form': form,
        'product': product,
        'total_price': total_price,
        'success': success
    })



@login_required

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'app/order_list.html', {'orders': orders})