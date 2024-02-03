from django.shortcuts import render, get_object_or_404, redirect
from .models import Garment, Schedule, Payment
from .forms import GarmentSchedulePaymentForm


def home_page(request):
    # return HttpResponse("HI THis is ROlO homepage")
    return render(request, 'pages/home.html')


def about_page(request):
    # return HttpResponse("This is aboutpage")
    return render(request, 'pages/about.html')


def contact_page(request):
    # return HttpResponse("This is contactpage")
    return render(request, 'pages/contact.html')


def services_page(request):
    # return HttpResponse("This is services")
    return render(request, 'pages/services.html')


def login_page(request):
    return render(request, 'pages/login.html')


def register_page(request):
    return render(request, 'pages/register.html')


def dashboard_page(request):
    garments = Garment.objects.all()
    return render(request, 'pages/dashboard.html', {'garments': garments})


def create_garment_schedule_payment(request):
    if request.method == 'POST':
        form = GarmentSchedulePaymentForm(request.POST)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.save()

            schedule = Schedule.objects.create(
                garment=garment,
                date=form.cleaned_data['date'],
                time=form.cleaned_data['time']
            )

            Payment.objects.create(
                garment=garment,
                amount=form.cleaned_data['amount'],
                status=form.cleaned_data['status'],
                mode_of_payment=form.cleaned_data['mode_of_payment']
            )

            return redirect('dashboard')  # Redirect to your dashboard page
    else:
        form = GarmentSchedulePaymentForm()

    return render(request, 'pages/repairForm.html', {'form': form})


def update_garment_schedule_payment(request, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    schedule = garment.schedule
    payment = garment.payment

    if request.method == 'POST':
        form = GarmentSchedulePaymentForm(request.POST, instance=garment)
        if form.is_valid():
            garment = form.save(commit=False)
            garment.save()

            schedule.date = form.cleaned_data['date']
            schedule.time = form.cleaned_data['time']
            schedule.save()

            payment.amount = form.cleaned_data['amount']
            payment.status = form.cleaned_data['status']
            payment.mode_of_payment = form.cleaned_data['mode_of_payment']
            payment.save()

            return redirect('dashboard')  # Redirect to your dashboard page
    else:
        form = GarmentSchedulePaymentForm(instance=garment)

    return render(request, 'pages/repairForm.html', {'form': form, 'garment': garment})


def delete_garment(request, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    garment.delete()
    return redirect('dashboard')  # Redirect to your dashboard page


def display_garment(request, garment_id):
    garment = get_object_or_404(Garment, pk=garment_id)
    return render(request, 'pages/displayGarment.html', {'garment': garment})
