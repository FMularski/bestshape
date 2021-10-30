from rest_framework.serializers import ModelSerializer
from shapes.models import User, Shape


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class ShapeSerializer(ModelSerializer):
    class Meta:
        model = Shape
        fields = '__all__'
        