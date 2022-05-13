from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Call(models.Model):
    from_number = PhoneNumberField()
    to_number = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20)
    sid = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('from_number', 'to_number', 'created_at')
