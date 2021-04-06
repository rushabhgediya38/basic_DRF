from rest_framework import serializers
from .models import Course, CourseCategory


# for normal serializers
# class CourseSerializers(serializers.Serializer):
#     Name = serializers.CharField(max_length=256)
#     price = serializers.IntegerField()
#     Discount = serializers.IntegerField()
#     Duration = serializers.DateTimeField(default=datetime.now())
#     AuthorName = serializers.CharField(max_length=256)
#
#     def create(self, validated_data):
#         return Course.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         course = Course(**validated_data, id=instance.id)
#         course.save()
#         return course


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        course = Course(**validated_data, id=instance.id)
        course.save()
        return course


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"
