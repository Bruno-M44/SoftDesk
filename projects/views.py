from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from projects.serializers import ProjectsListSerializer, \
    ProjectsDetailSerializer, ContributorSerializer
from projects.models import Projects, Contributors


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsListSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_queryset(self):
        return Projects.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    @action(detail=True, methods=["get", "post"],
            serializer_class=ContributorSerializer)
    def users(self, request, pk):
        contributors = Contributors.objects.filter(project=self.get_object())
        print(contributors)
        serializer = [ContributorSerializer(contributors)
                      for contributor in contributors]
        print(serializer)

        return Response(serializer.data)




    '''
    @action(detail=True, methods=["get"])
    def users(self, request, pk):
        contributors = Contributors.objects.get(project=self.get_object())
        serializer = ContributorSerializer(contributors)
        return Response(serializer.data)
    '''


