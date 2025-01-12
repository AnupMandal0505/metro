from django.contrib import admin
from .models import User  
from .models import Client
from app.models import Appointment

# Register your custom user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name', 'role')  # Display relevant fields
    search_fields = ('username', 'email')  # Allow searching by username and email
    list_filter = ('role',)  # Filter by role
    ordering = ('username',)  # Order by username by default




class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'pa_ref', 'gm_ref', 'appointment_date', 'status', 'uuid', 'updated_at') 
    list_filter = ('status', 'appointment_date')
    search_fields = ('client__name', 'uuid', 'gm_ref')  
    ordering = ('appointment_date',)  

admin.site.register(Appointment, AppointmentAdmin)




class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'created_at')  # Fields to display in the list view
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')  # Fields that can be searched
    ordering = ('created_at',)  # Default ordering by created date

admin.site.register(Client, ClientAdmin)
