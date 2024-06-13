from rest_framework import serializers
from .models import employee

class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'first_name','last_name','email_address', 'designation']