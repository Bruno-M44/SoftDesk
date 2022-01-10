from rest_framework.serializers import ModelSerializer

from projects.models import Projects, Contributors


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = ["id", "project", "permission", "role"]


class ProjectsListSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ["id", "title", "description", "type", "author_user_id"]


class ProjectsDetailSerializer(ModelSerializer):

    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Projects
        fields = ["id", "title", "description", "type", "author_user_id",
                  "contributors"]
