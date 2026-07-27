from rest_framework import serializers
from academico.models import Carrera, Alumno, Materia, Inscripcion

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    carrera_nombre = serializers.ReadOnlyField(source='carrera.nombre')

    class Meta:
        model = Alumno
        fields = '__all__'

class MateriaSerializer(serializers.ModelSerializer):
    carrera_nombre = serializers.ReadOnlyField(source='carrera.nombre')

    class Meta:
        model = Materia
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    alumno_nombre = serializers.ReadOnlyField(source='alumno.__str__')
    materia_nombre = serializers.ReadOnlyField(source='materia.nombre')

    class Meta:
        model = Inscripcion
        fields = '__all__'