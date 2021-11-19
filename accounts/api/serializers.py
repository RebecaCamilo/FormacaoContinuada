from rest_framework import serializers
from ..models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'course', 'email', 'cpf', 'password', 'password2')
        #extra_kwargs = {'password': {'write_only': True}} #faz com que não apareça o valor enviado deste campo no template da API
    

    # def confirm_password(self, data):
    #     if not data.get('password') or not data.get('confirm_password'):
    #         raise serializers.ValidationError("Please enter a password and "
    #             "confirm it.")
    #     if data.get('password') != data.get('confirm_password'):
    #         raise serializers.ValidationError("Those passwords don't match.")
    #     return data

    
    def create(self,validated_data):
        '''Função para encriptar a senha enviada pela API e para confirmação de senha'''
        user = User(**validated_data)
        if(user.password == user.password2):
            user.set_password(validated_data['password'])
            user.password2 = user.password
            user.save()
            return user
        raise serializers.ValidationError("Those passwords don't match.")




#ctrl + ;  Comentar linha inteira