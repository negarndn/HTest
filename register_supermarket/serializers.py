from rest_framework import serializers
from .models import Supermarket


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = ('id_sup', 'name_sup', 'national_num_sup', 'phone', 'password_sup', 'date_created', 'city', 'address',
                  'owner', 'sms')
