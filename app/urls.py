

from django.urls import path
from .views import getUser,signin,signout,appointment,client

urlpatterns = [
    path('get_user/', getUser.GetUser.as_view(), name='get_user'),
    path('login', signin.LoginAPI.as_view(), name='login'),
    path('logout', signout.LogoutAPI.as_view(), name='login'),


    # Apointment..............
    path('appointments/', appointment.AppointmentAPIView.as_view(), name='appointment_list'),  # For GET (list) or POST (create)
    path('appointments/<int:pk>/', appointment.AppointmentAPIView.as_view(), name='appointment_detail'),  # For GET, PUT, DELETE (specific appointment)


    # client......................
    path('clients/', client.ClientAPIView.as_view(), name='client-list'),
    path('clients/<int:pk>/', client.ClientAPIView.as_view(), name='client-detail'),
]
 