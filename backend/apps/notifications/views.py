from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer
from apps.notifications.services import mark_read
from apps.core.responses import success
from apps.core.audit import record_event


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        role = getattr(self.request.user, "role", None)
        if role == "manager":
            return Notification.objects.all()
        return Notification.objects.filter(recipient=self.request.user)

    def perform_create(self, serializer):
        obj = serializer.save(delivery_status="delivered")
        record_event(self.request.user, "notification.create", obj)

    @action(detail=True, methods=["post"], url_path="mark-read")
    def mark_read_action(self, request, pk=None):
        return success(self.get_serializer(mark_read(self.get_object())).data)

    @action(detail=False, methods=["post"], url_path="mark-all-read")
    def mark_all_read(self, request):
        self.get_queryset().filter(read_at__isnull=True).update(delivery_status="read", read_at=timezone.now())
        return success(message="Notifications marked read")

