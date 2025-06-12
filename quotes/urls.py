from django.urls import path
from .views import DailyQuoteView

urlpatterns = [
    path('daily-quote/', DailyQuoteView.as_view(), name='daily-quote'),
]
