from django.urls import path, include
from api.views import Company_ViewSet, Employee_ViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', Company_ViewSet)
router.register(r'employees', Employee_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]