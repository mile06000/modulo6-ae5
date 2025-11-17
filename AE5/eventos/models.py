from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre
