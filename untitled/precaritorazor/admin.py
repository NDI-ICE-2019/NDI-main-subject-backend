from django.contrib import admin

from .models import Organization
from .models import Category
from .models import Type
from .models import Aid
from .models import Criteria

admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Aid)
admin.site.register(Criteria)
