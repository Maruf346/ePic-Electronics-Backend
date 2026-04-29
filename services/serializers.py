from rest_framework import serializers
from .models import (
    Service,
    ServiceProvideItem,
    ServiceProblem,
    ServiceStat,
    ServiceStep,
    ServiceCapability,
)


class ServiceProvideItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvideItem
        fields = ["text"]


class ServiceProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProblem
        fields = ["title", "description"]


class ServiceStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStat
        fields = ["value", "label"]


class ServiceStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStep
        fields = ["step", "title", "description", "icon"]


class ServiceSerializer(serializers.ModelSerializer):
    shortTitle = serializers.CharField(source="short_title", read_only=True)
    heroSubtitle = serializers.CharField(source="hero_subtitle", read_only=True)
    ctaSecondary = serializers.CharField(
        source="cta_secondary", read_only=True, allow_blank=True
    )
    stats = ServiceStatSerializer(many=True, read_only=True)
    steps = ServiceStepSerializer(many=True, read_only=True)
    capabilities = serializers.SerializerMethodField()
    introSection = serializers.SerializerMethodField()
    whatWeProvide = serializers.SerializerMethodField()
    problemsWeSolve = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "slug",
            "title",
            "shortTitle",
            "description",
            "heroSubtitle",
            "content",
            "cta",
            "ctaSecondary",
            "category",
            "stats",
            "steps",
            "capabilities",
            "image",
            "introSection",
            "whatWeProvide",
            "problemsWeSolve",
        ]

    def get_capabilities(self, obj):
        return list(obj.capabilities.values_list("text", flat=True))

    def get_introSection(self, obj):
        if obj.intro_heading:
            return {
                "heading": obj.intro_heading,
                "subheading": obj.intro_subheading,
                "content": obj.intro_content,
            }
        return None

    def get_whatWeProvide(self, obj):
        if obj.what_we_provide_heading:
            items = list(obj.provide_items.values_list("text", flat=True))
            return {
                "heading": obj.what_we_provide_heading,
                "items": items,
            }
        return None

    def get_problemsWeSolve(self, obj):
        if obj.problems_we_solve_heading:
            problems = obj.problem_items.all()
            return {
                "heading": obj.problems_we_solve_heading,
                "items": ServiceProblemSerializer(problems, many=True).data,
            }
        return None