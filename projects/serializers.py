from rest_framework import serializers
from .models import Project, ProjectStat, ProjectSection


class ProjectStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStat
        fields = ["value", "label"]


class ProjectSectionSerializer(serializers.ModelSerializer):
    imageAlt = serializers.CharField(source="image_alt", read_only=True)

    class Meta:
        model = ProjectSection
        fields = ["heading", "text", "image", "imageAlt"]


class ProjectSerializer(serializers.ModelSerializer):
    shortTitle = serializers.CharField(source="short_title", read_only=True)
    stats = ProjectStatSerializer(many=True, read_only=True)
    detailedContent = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "slug",
            "title",
            "shortTitle",
            "description",
            "image",
            "content",
            "category",
            "featured",
            "stats",
            "detailedContent",
        ]

    def get_detailedContent(self, obj):
        sections = obj.sections.all()
        return {
            "introduction": obj.introduction,
            "sections": ProjectSectionSerializer(sections, many=True).data,
        }