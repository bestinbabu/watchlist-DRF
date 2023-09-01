from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    
    watchlist = serializers.StringRelatedField(read_only=True)
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['watchlist']
        
        
class WatchListSerializer(serializers.ModelSerializer):
    
    #extra fields for model
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
            model = WatchList
            fields = '__all__'
            # exclude = ['id']
    reviews = ReviewSerializer(many=True,read_only=True) # for get readonly access


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'  
    watchlist = WatchListSerializer(many=True,read_only=True)
    #watchlist = serializers.StringRelatedField(many=True,read_only=True)










    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and description must be different")
    #     return  data
    
    # def validate_name(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("Name must be at least 2 characters long")
    #     return data

    # def get_len_name(self, data):
    #     return len(data.name)


























# def description_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Description must be at least 2 characters long")
    


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data);
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description must be different")
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long")
#         return value