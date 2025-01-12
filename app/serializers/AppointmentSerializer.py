from rest_framework import serializers
from app.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'client', 'pa_ref', 'gm_ref', 'appointment_date', 'status', 'notes', 'updated_at']
