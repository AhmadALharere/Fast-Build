from rest_framework import serializers
from .models import profile
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer




class CustomRegisterSerializer(RegisterSerializer):
    
    def validate_email(self, value):
        print("validate_email called!")
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value




class User_Serializer(serializers.ModelSerializer):
     # بيانات من User (للعرض فقط)
  
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        


class Profile_Serializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username', required=False)
    email = serializers.EmailField(source='user.email', read_only=True)

    # بيانات من User (قابلة للتعديل)
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)

    class Meta:
        model = profile
        fields =['username','email','first_name','last_name','birth_date','phone_number','gender','image']
        
    def update(self, instance, validated_data):
        # فصل بيانات user عن باقي الحقول
            user_data = validated_data.pop('user', {})

        # تعديل الاسم الأول والأخير فقط
            user = instance.user
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        # تعديل حقول البروفايل
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            return instance

