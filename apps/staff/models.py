from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = {
    (0, 'Pending'),
    (1, 'Reviewed'),
    (2, 'Cancel')
}


class Complaint(models.Model):
    complaint = models.CharField(max_length=3000, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, blank=True, null=True)
    review = models.CharField(max_length=3000, blank=True, null=True)
    is_seen = models.BooleanField(blank=True, null=True)
    seen_at = models.DateTimeField(blank=True, null=True)
    seen_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                blank=True, null=True, related_name='complaint_seen_by')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='complaints')
    created_at = models.DateTimeField(default=timezone.now)
    review_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                  blank=True, null=True, related_name='complaint_review_by')
    review_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.complaint)

    class Meta:
        db_table = 'complaint'
        ordering = ('-created_at',)