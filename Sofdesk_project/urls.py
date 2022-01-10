from rest_framework import routers
from django.urls import include, path
from django.contrib import admin

from authentication.views import SignupView
from projects.views import ProjectsViewset

router = routers.SimpleRouter()
router.register("projects", ProjectsViewset, basename="projects")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupView.as_view()),
    path("", include(router.urls))

]
