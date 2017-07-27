from django.db import models

# Create your models here.
class post(models.Model)
  """
  Almacena las publicaciones realizadas por el equipo
  administrativo
  """
  title = models.CharField(max_lenght=50,help_text='Ingrese ')
  pubdate = models.DateTimeField(auto_now=True, help_text
  author = models.ForeignKey (Author, help_ text='Fecha)
