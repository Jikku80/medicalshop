from django.urls import path
from . import views
from .views import EsewaRequestView, KhaltiRequestView, KhaltiVerifyView, OrderDoneView
from django.utils.translation import gettext_lazy as _
app_name = 'payment'

urlpatterns = [
    path('esewa/', EsewaRequestView.as_view(), name='esewa'),
    path('khalti/', KhaltiRequestView.as_view(), name='khalti'),
    path('khalti-verify/', KhaltiVerifyView.as_view(), name='khalti-verify'),
    path('khalti-verify/done/', KhaltiVerifyView.as_view(), name='done'),

    path(_('ordered/'), OrderDoneView.as_view(), name='ordered'),
    path(_('done/'), views.payment_done, name='done'),
    path(_('canceled/'), views.payment_canceled, name='canceled')
]
