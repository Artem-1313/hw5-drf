from django.urls import path, include
from .views import today, hello_world, my_name, calculator, ListStore, AddStore, StoreDetail, menu

urlpatterns = [
    path('', menu.as_view()),
    path('today/', today, name='today'),
    path('hello_world/', hello_world, name='hello_world'),
    path('my_name/', my_name, name="my_name"),
    path('calculator/', calculator, name='calculator'),
    path('list_store/', ListStore.as_view(), name="list_store"),
    path('add_store/', AddStore.as_view(), name="add_store"),
    path('detail_store/<int:pk>/', StoreDetail .as_view(), name="detail_store")

]
