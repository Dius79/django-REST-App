from django.db import models
from django.conf import settings
from profiles.models import CustomerProfile, TechnicianProfile

class WorkOrder(models.Model):
    STATUS_NEW = 'new'
    STATUS_SCHEDULED = 'scheduled'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'
    STATUS_PAID = 'paid'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_PAID, 'Paid'),
    ]

    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
    technician = models.ForeignKey(TechnicianProfile, on_delete=models.SET_NULL, null=True, blank=True)
    appliance_type = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100, blank=True)
    issue_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.appliance_type}"

class WorkOrderMedia(models.Model):
    workorder = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='workorder_media/')

    def __str__(self):
        return str(self.file)
