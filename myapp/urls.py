from django.urls import path
from . import views


urlpatterns = [
    path('expenses/',views.ExpenseManagement.as_view(),name='expense_management'),
    path('filter-expense/<str:year>/<str:month>/',views.filter_expense,name='filter_expense'),
    path('total_expense/<str:year>/<str:month>/',views.filter_expense,name='filter_expense'),
]