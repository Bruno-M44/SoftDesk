from django.contrib import admin

from .models import Projects, Contributors, Issues, Comments

admin.site.register([Projects, Contributors, Issues, Comments])
