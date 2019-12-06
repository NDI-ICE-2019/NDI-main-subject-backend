from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'aids', views.AidViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'criteria', views.CriteriaViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
