from rest_framework import serializers 
from .models import Article 

#serialize for article model


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
      model =  Article
      fields = "__all__"
      
#validation globale 
def validate (self,  data):
    if not data.get('title'):
        raise serializers.validationError ("the title is requiered")
    if not data.get ('autor'):
        raise serializers.validationError("the autor")