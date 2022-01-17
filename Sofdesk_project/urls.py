from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView
from django.urls import include, path
from django.contrib import admin

from authentication.views import SignupViewset
from projects.views import ProjectsViewset, UsersViewset, IssuesViewset, \
    CommentsViewset

router = routers.SimpleRouter()
router.register("projects", ProjectsViewset, basename="projects")

router_signup = routers.SimpleRouter()
router_signup.register("signup", SignupViewset, basename="signup")

user_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
user_router.register("users", UsersViewset, basename="users")

issue_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
issue_router.register("issues", IssuesViewset, basename="issues")

comment_router = routers.NestedSimpleRouter(issue_router, "issues",
                                            lookup="issue")
comment_router.register("comments", CommentsViewset, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("", include(router_signup.urls)),
    path("", include(router.urls)),
    path("", include(user_router.urls)),
    path("", include(issue_router.urls)),
    path("", include(comment_router.urls))
]
