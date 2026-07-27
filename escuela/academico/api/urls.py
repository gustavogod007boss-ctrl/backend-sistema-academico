from rest_framework.routers import DefaultRouter
from academico.api.views import (
    CarreraViewSet, AlumnoViewSet, MateriaViewSet, InscripcionViewSet, 
    )

router = DefaultRouter()
router.register('carreras', CarreraViewSet, basename='carrera') 
router.register('alumnos', AlumnoViewSet, basename='alumno')
router.register('materias', MateriaViewSet, basename='materia')
router.register('inscripciones', InscripcionViewSet, basename='inscripcion')
urlpatterns = router.urls 