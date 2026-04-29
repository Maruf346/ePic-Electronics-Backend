from rest_framework import serializers
from .models import Tutorial, TutorialSection


class TutorialSectionSerializer(serializers.ModelSerializer):
    imageAlt = serializers.CharField(source="image_alt", read_only=True)

    class Meta:
        model = TutorialSection
        fields = ["heading", "text", "image", "imageAlt"]


class TutorialSerializer(serializers.ModelSerializer):
    detailedContent = serializers.SerializerMethodField()

    class Meta:
        model = Tutorial
        fields = [
            "id",
            "slug",
            "title",
            "description",
            "image",
            "content",
            "category",
            "detailedContent",
        ]

    def get_detailedContent(self, obj):
        sections = obj.sections.all()
        return {
            "introduction": obj.introduction,
            "sections": TutorialSectionSerializer(sections, many=True).data,
        }