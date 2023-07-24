from rest_framework import serializers 
from cars.models import Car, CompanyInfo 

########## 

class CarSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField()

    class Meta:
        model = Car 
        fields = "__all__"

    def get_created_at(self,instance):
        return instance.created_at.strftime('%d %B %Y') 


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = "__all__"