from django.contrib import admin
from .models import WorkOrder, WorkOrderMedia

class WorkOrderMediaInline(admin.TabularInline):
    model = WorkOrderMedia
    extra = 0

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [WorkOrderMediaInline]
    list_display = ('id', 'customer', 'technician', 'status', 'created_at')
