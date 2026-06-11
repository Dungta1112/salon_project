from rest_framework import serializers

from apps.appointments.models import Appointment, AppointmentService


class AppointmentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentService
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    appointment_services = AppointmentServiceSerializer(many=True, read_only=True)
    customer_details = serializers.SerializerMethodField()
    employee_details = serializers.SerializerMethodField()
    service_details = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ("is_deleted", "deleted_at", "created_at", "updated_at")

    def get_customer_details(self, obj):
        if obj.customer:
            return {
                "id": obj.customer.id,
                "full_name": obj.customer.full_name,
                "phone": obj.customer.phone,
                "email": obj.customer.email,
            }
        return None

    def get_employee_details(self, obj):
        if obj.staff:
            return {
                "id": obj.staff.id,
                "full_name": obj.staff.full_name,
                "specialties": getattr(obj.staff, "specialties", "Senior Hair Stylist"),
            }
        return None

    def get_service_details(self, obj):
        first_service = obj.appointment_services.first()
        if first_service and first_service.service:
            return {
                "id": first_service.service.id,
                "name": first_service.service.name,
                "price": float(first_service.price_at_booking),
                "duration": first_service.duration_at_booking,
            }
        return None

    def validate(self, attrs):
        start = attrs.get("scheduled_start", getattr(self.instance, "scheduled_start", None))
        end = attrs.get("scheduled_end", getattr(self.instance, "scheduled_end", None))
        if start and end and end <= start:
            raise serializers.ValidationError("scheduled_end must be after scheduled_start.")
        return attrs


class AppointmentTransitionSerializer(serializers.Serializer):
    reason = serializers.CharField(required=False, allow_blank=True)
    scheduled_start = serializers.DateTimeField(required=False)
    scheduled_end = serializers.DateTimeField(required=False)
    staff = serializers.IntegerField(required=False)
