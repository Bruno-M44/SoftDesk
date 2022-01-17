from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_204_NO_CONTENT

from projects.serializers import ProjectsListSerializer, \
    ProjectsDetailSerializer, ContributorSerializer, IssueSerializer, \
    CommentSerializer
from projects.models import Projects, Contributors, Issues, Comments


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsListSerializer
    detail_serializer_class = ProjectsDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.auth.payload["user_id"]
        authorized_projects = [contributor.project.id for contributor in
                               Contributors.objects.filter(user_id=user_id)]
        return Projects.objects.filter(id__in=authorized_projects)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        if request.data:
            request.data._mutable = True
            request.data["author_user"] = self.request.auth.payload["user_id"]
            request.data._mutable = False
        else:
            request.data["author_user"] = self.request.auth.payload["user_id"]
        serializer = self.get_serializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        project_instance = Projects(id=serializer.data["id"],
                                    title=serializer.data["title"],
                                    description=serializer.data["description"],
                                    type=serializer.data["type"],
                                    author_user=self.request.user)
        Contributors.objects.create(user=self.request.user,
                                    project=project_instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        if self.request.user == self.get_object().author_user:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user == self.get_object().author_user:
            self.perform_destroy(self.get_object())
            return Response(HTTP_204_NO_CONTENT)
        else:
            return Response(HTTP_401_UNAUTHORIZED)


class UsersViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    detail_serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "user"

    def get_queryset(self):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            return Contributors.objects.filter(
                project_id=self.kwargs["project_pk"])
        else:
            return Contributors.objects.none()

    def create(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            if request.data:
                request.data._mutable = True
                request.data["project"] = self.kwargs["project_pk"]
                request.data._mutable = False
            else:
                request.data["project"] = self.kwargs["project_pk"]
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            self.perform_destroy(self.get_object())
            return Response(HTTP_204_NO_CONTENT)
        else:
            return Response(HTTP_401_UNAUTHORIZED)


class IssuesViewset(ModelViewSet):
    serializer_class = IssueSerializer
    detail_serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            return Issues.objects.filter(
                project_id=self.kwargs["project_pk"])
        else:
            return Issues.objects.none()

    def create(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            if request.data:
                request.data._mutable = True
                request.data["project"] = self.kwargs["project_pk"]
                request.data["author_user"] = Projects.objects.get(
                        id=self.kwargs["project_pk"]).author_user.pk
                if "assignee_user" not in request.data:
                    request.data["assignee_user"] = request.data["author_user"]
                request.data._mutable = False
            else:
                request.data["project"] = self.kwargs["project_pk"]
                request.data["author_user"] = Projects.objects.get(
                        id=self.kwargs["project_pk"]).author_user.pk
                if "assignee_user" not in request.data:
                    request.data["assignee_user"] = request.data["author_user"]
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            self.perform_destroy(self.get_object())
            return Response(HTTP_204_NO_CONTENT)
        else:
            return Response(HTTP_401_UNAUTHORIZED)


class CommentsViewset(ModelViewSet):
    serializer_class = CommentSerializer
    detail_serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            return Comments.objects.filter(
                issue_id=self.kwargs["issue_pk"])
        else:
            return Comments.objects.none()

    def create(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            if request.data:
                request.data._mutable = True
                request.data["issue"] = self.kwargs["issue_pk"]
                request.data["author_user"] = Projects.objects.get(
                        id=self.kwargs["project_pk"]).author_user.pk
                request.data._mutable = False
            else:
                request.data["issue"] = self.kwargs["issue_pk"]
                request.data["author_user"] = Projects.objects.get(
                        id=self.kwargs["project_pk"]).author_user.pk
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if self.request.user == Projects.objects.get(
                id=self.kwargs["project_pk"]).author_user:
            self.perform_destroy(self.get_object())
            return Response(HTTP_204_NO_CONTENT)
        else:
            return Response(HTTP_401_UNAUTHORIZED)
