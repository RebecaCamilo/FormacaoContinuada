from rest_framework import serializers
from ..models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'matricula', 'curso', 'telefone', 'password')
        #extra_kwargs = {'password': {'write_only': True}} #faz com que não apareça o valor enviado deste campo no template da API
    
    def create(self,validated_data):
        '''Para encriptar a senha enviada pela API'''
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

