"""
    Application tested by Postman
    The code here is a draft test
    It isn't working
"""


from django.urls import reverse_lazy
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from projects.models import Contributors, Projects, Issues, Comments
from django.contrib.auth.models import User
from projects.views import ProjectsViewset


class TestProject(APITestCase):
    url = reverse_lazy("projects-list")
    url_token = reverse_lazy("obtain_token")

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        factory = APIRequestFactory()
        view = ProjectsViewset.as_view({"get": "list"})
        request = factory.get(self.url)
        User.objects.create_user(username="Olivia",
                                 password="django123!")
        token = self.client.post(self.url_token,
                                 data={"username": "Olivia",
                                       "password": "django123!"})
        print(factory.get(self.url))
        print(User.objects.get(username="Olivia"))
        force_authenticate(request=request,
                           user=User.objects.get(username="Olivia"),
                           token=token)
        print(view)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.assertFalse(Projects.objects.exists())
        response = self.client.post(self.url, data={"title": "tentative"})
        self.assertEqual(response.status_code, 401)
        self.assertFalse(Projects.objects.exists())
