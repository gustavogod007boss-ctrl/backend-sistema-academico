from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet, AlumnoViewSet, MateriaViewSet, InscripcionViewSet

router = DefaultRouter()
router.register(r'carreras', CarreraViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'inscripciones', InscripcionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]