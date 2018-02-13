
from rest_framework import serializers
from school_mgmt.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from random import randint



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
		

class SchoolSerializer(serializers.ModelSerializer):
    # school_count = serializers.SerializerMethodField()
    class Meta:
        model = School
        exclude = ('created_date', 'modified_date')


class SchoolListSerializer(serializers.ModelSerializer):
    
    owner = UserSerializer()

    class Meta:
        model = School
        
#add
class UniversityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_at')


class UniversitySerializer(serializers.ModelSerializer):
    school_count = SchoolSerializer(source='school_set.count', read_only=True)


    class Meta:
        model = University
        fields = ('id', 'name', 'website', 'created_date','modified_date','is_active','school_count')

    def get_school_count(self, obj):
        return obj.school_set.count()


class University_SchoolsListSerializer(serializers.ModelSerializer):
    schools = serializers.SerializerMethodField()
    
    def get_schools(self, obj):
        schools = School.objects.filter(university=obj)
        serializer = SchoolListSerializer(schools, many=True)
        return serializer.data

    class Meta:
        model = University
        fields = ('id','name','schools')


class StudentSerializer(serializers.ModelSerializer):
    # school_count = serializers.SerializerMethodField()

    # schools = serializers.SerializerMethodField()
    
    # def get_schools(self, obj):
    #     schools = School.objects.filter(university=obj)
    #     serializer = SchoolListSerializer(schools, many=True)
    #     return serializer.data

    class Meta:
        model = Student


    



  
# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ('order', 'title', 'duration')

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ('album_name', 'artist', 'tracks')



# class GroupSerializer(serializers.ModelSerializer):

#     school_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Group
#         fields = ('id', 'name', 'website', 'created_at','modified_at','is_active','school_count')

#     def get_school_count(self, obj):
#         return obj.school_set.count()

# user_count = serializers.IntegerField(source='user_set.count', read_only=True)

    # def get_comments(self, obj):
    #     comments = Comments.objects.filter(post=obj)
    #     serializer = CommentSerializer(comments, many=True)
    #     return serializer.data

