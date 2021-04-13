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
    # ingredients = serializers.StringRelatedField(many=True)
    # ingredients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # ingredients = serializers.HyperlinkedRelatedField()
    # ingredients = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='protein'
    # )

    class Meta:
        model = Course
        fields = ['id', 'Name', 'price', 'Discount', 'Duration', 'AuthorName', 'ingredients']

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


# nested serilaizers

class NestedCourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['protein', 'title', 'duration']


class NestedCourseSerilaizers(serializers.ModelSerializer):
    ingredients = NestedCourseCategorySerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'Name', 'price', 'Discount', 'Duration', 'AuthorName', 'ingredients']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        product = Course.objects.create(**validated_data)
        for track_data in ingredients_data:
            CourseCategory.objects.create(product=product, **track_data)
        return product

    # def update(self, instance, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #
    #     category = instance.ingredients
    #
    #     instance.Name = validated_data.get('username', instance.username)
    #     instance.price = validated_data.get('email', instance.email)
    #     instance.Discount = validated_data.get('email', instance.email)
    #     instance.Duration = validated_data.get('email', instance.email)
    #     instance.AuthorName = validated_data.get('email', instance.email)
    #     instance.save()
    #
    #     for track_data in ingredients_data:
    #         CourseCategory.objects.create(product=instance, **track_data)
    #         category.save()
    #     return instance

