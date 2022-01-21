from unicodedata import category
from rest_framework import serializers

from courses.models import Course, CourseTag


class CourseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTag
        fields = ("content", "color", "fa_icon_name")


class CountsForField(serializers.Field):
    def to_representation(self, value):
        if value.dstudies and value.science:
            return "Digital Studies, CTE, or Science"
        elif value.dstudies:
            return "Digital Studies or CTE"
        elif value.science:
            return "CTE or Science"
        else:
            return "CTE"


class CourseLengthSerializer(serializers.Field):
    def to_representation(self, value):
        if value.semester and value.fullyear:
            return "0.5 or 1.0"
        elif value.semester:
            return "0.5"
        else:
            return "1.0"


class CourseSlugField(serializers.Field):
    def to_representation(self, value):
        return "-".join(value.name.split(" ")).lower()


class CourseSerializer(serializers.ModelSerializer):
    length = CourseLengthSerializer(source='*')
    countsFor = CountsForField(source='*')
    slug = CourseSlugField(source="*")
    tags = CourseTagSerializer(read_only=True, many=True)
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Course
        fields = ('slug', 'name', 'category', 'length', 'countsFor', 'description', 'tags', 'units', 'prereqs')
