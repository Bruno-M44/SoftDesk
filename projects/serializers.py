from rest_framework.serializers import ModelSerializer

from projects.models import Projects, Contributors, Issues, Comments


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = "__all__"


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issues
        fields = "__all__"


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"


class ProjectsListSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class ProjectsDetailSerializer(ModelSerializer):
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Projects
        fields = "__all__"
