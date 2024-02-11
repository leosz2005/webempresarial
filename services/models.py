from django.db import models

# Create your models here.
class Services(models.Model):
    title= models.CharField(max_length=200, verbose_name= 'título')
    subtitle= models.CharField(max_length=200, verbose_name= 'subtítulo')
    content= models.TextField(verbose_name='contenido')
    image= models.ImageField(verbose_name='imagen', upload_to='services')
    created= models.DateTimeField(verbose_name='fecha de creación', auto_now_add=True)
    updated= models.DateTimeField(verbose_name='fecha de edición', auto_now=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']
        
    def __str__(self) -> str:
        return self.title