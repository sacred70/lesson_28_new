from django.urls import path

from ads.views.ad import AdListCreateView, AdDitailView

urlpatterns = [
    path('', AdListCreateView.as_view()),
    path('/<int:pk>', AdDitailView.as_view())
    ]
