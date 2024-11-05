
# from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from lms.validators import YouTubeValidator
from lms.models import Course, Lesson, Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [YouTubeValidator(field="url")]
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lesson_set", many=True)  # Выводим список уроков курса
    lesson_count = serializers.SerializerMethodField()  # Выводим количество уроков курса
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, instance):  # Выводим количество уроков курса
        return instance.lesson_set.count()

    def get_subscription(self, instance):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=instance).exists()

    def create(self, validated_data):
        lesson = validated_data.pop('lesson_set')

        course_item = Course.objects.create(**validated_data)

        for l in lesson:
            Lesson.objects.create(**l, course=course_item)

        return course_item


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)
