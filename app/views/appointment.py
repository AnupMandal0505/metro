from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Appointment
from app.serializers.AppointmentSerializer import AppointmentSerializer
from rest_framework import status

class AppointmentAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    # GET method to fetch appointments
    def get(self, request, pk=None):
        if pk:
            try:
                appointment = Appointment.objects.get(pk=pk)
            except Appointment.DoesNotExist:
                return Response({"detail": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = AppointmentSerializer(appointment)
        else:
            appointments = Appointment.objects.all()
            serializer = AppointmentSerializer(appointments, many=True)
        
        return Response(serializer.data)

    # POST method to create an appointment
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This saves the appointment to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method to update an existing appointment
    def put(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"detail": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete an appointment
    def delete(self, request, pk):
        try:
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"detail": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
        
        appointment.delete()
        return Response({"detail": "Appointment deleted."}, status=status.HTTP_204_NO_CONTENT)
