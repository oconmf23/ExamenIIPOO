from django.db import models

# Create your models here.
class TipoLibros(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Genero(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
    
class Estanterias(models.Model):
    numero_Estanteria = models.CharField(max_length=200)

    def __str__(self):
        return self.numero_Estanteria
    
class Clientes(models.Model):
    id_card = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=200)
    email = models.EmailField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Libros(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    numero_Paginas = models.CharField(max_length=200)
    id_Tipo_libros = models.ForeignKey(TipoLibros, on_delete=models.CASCADE)
    id_Clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_Estanterias = models.ForeignKey(Estanterias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.autor + " " + self.numero_Paginas

