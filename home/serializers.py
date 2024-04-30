from rest_framework import serializers
from  serializers import Vendor  # Import the Vendor model from your app

class VendorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    contact_details = serializers.TextField()
    address = serializers.TextField()
    vendor_code = serializers.CharField(max_length=50, unique=True)
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()

class PurchaseorderSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    )

    po_number = serializers.CharField(max_length=100)
    vendor = serializers.ForeignKey(Vendor, on_delete=serializers.CASCADE)
    order_date = serializers.DateTimeField()
    delivery_date = serializers.DateTimeField()
    items = serializers.JSONField()
    quantity = serializers.IntegerField()
    status = serializers.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = serializers.FloatField(null=True, blank=True)
    issue_date = serializers.DateTimeField()
    acknowledgment_date = serializers.DateTimeField(null=True, blank=True)
class Historicalperformanceserializer(serializers.Serializer):
    vendor = serializers.ForeignKey(Vendor, on_delete= serializers.CASCADE)
    date = serializers.DateTimeField()
    on_time_delivery_rate = serializers.FloatField()
    quality_rating_avg = serializers.FloatField()
    average_response_time = serializers.FloatField()
    fulfillment_rate = serializers.FloatField()

