from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    year_of_study = models.IntegerField()


    def create(self, validated_data):
        student = Student(**validated_data)
        student.save()
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.year_of_study = validated_data.get('year_of_study', instance.year_of_study)
        instance.save()
        return instance


