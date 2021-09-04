from django.shortcuts import render

import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import Coffee

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth=("rzp_test_EUlIypwTCIgibx", "QybQj3ZTB0NdmogTBhEEG3NB"))
        payment = client.order.create({'amount':amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        coffee = Coffee(name= name, amount= amount, payment_id = payment['id'])

        payment_id = payment['id']
        order_status = payment['status']
        if order_status =='created':
            coffee = Coffee(
                name= name,
                amount= amount,
                payment_id = payment_id,
            )
        coffee.save()

        payment['name'] = name
    return render(request, 'index.html', {'payment': payment})

@csrf_exempt
def success(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
    return render(request, 'success.html')