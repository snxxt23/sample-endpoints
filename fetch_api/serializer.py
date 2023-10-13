from rest_framework import serializers
from .models import CustomUser
 

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id','email','first_name','last_name','password','confirm_password','is_active')
        extra_kwargs = {
            'confirm_password':{'write_only':True}
        }

        #validating_password
    def validate(self,data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        print(password)
        print(confirm_password)

        if password != confirm_password:
            raise serializers.ValidationError('Password Mismatch')
        return data