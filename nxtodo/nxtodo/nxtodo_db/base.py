from django.db import models
from django.utils import timezone


class Base(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    priority = models.CharField(max_length=1, null=True)
    category = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def get_notification(self, now):
        notifications = []
        for reminder in self.reminder_set.all():
            notification = reminder.notify(now)
            if notification:
                notifications.append(notification)
        if not notifications:
            return None
        notifications.sort(key=lambda obj: obj, reverse=True)
        return notifications[0]

    def __str__(self):
        return self.title

    class Meta:
        abstract = True