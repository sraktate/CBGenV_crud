from django.urls import path
from .views import LaptopListView,LaptopCreateView,LaptopUpdateView,LaptopDeleteView,Homeview

urlpatterns=[
    path('ho/', Homeview, name='home'),
    path('listview/',LaptopListView.as_view(),name='L-list'),
    path('create/',LaptopCreateView.as_view(),name='L-Register'),
    path('update/<int:pk>',LaptopUpdateView.as_view(),name='updateList'),
    path('delete/<int:pk>',LaptopDeleteView.as_view(),name='deleteList')
]


