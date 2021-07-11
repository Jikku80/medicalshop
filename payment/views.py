from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from orders.models import Order
from django.http import JsonResponse
import requests
from .tasks import payment_completed


class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            'order': order
        }
        return render(request, 'payment/khalti.html', context)


class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        amount = request.GET.get('amount')
        o_id = request.GET.get('order_id')
        print(token, amount, o_id)
        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "Key test_secret_key_e870cfff05194c559c7e89cab66ab904"
        }
        order_obj = Order.objects.get(id=o_id)
        response = requests.post(url, payload, headers=headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.paid = True
            order_obj.save()
            payment_completed.delay(order_obj.id)
        else:
            success = False
        data = {
            'success': success
        }
        return JsonResponse(data)


class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, 'payment/esewa.html', context)


class OrderDoneView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get('o_id')
        order = Order.objects.get(id=o_id)
        context = {
            'order': order
        }
        return render(request, 'payment/ordered.html', context)


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
