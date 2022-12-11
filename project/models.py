from django.db import models
from django.utils import timezone

# Create your models here.
#Creación del modelo Project para guardar los proyectos del portafolio según lo solicitado
class Project(models.Model):
    photo = models.URLField(max_length=5000)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=200, null=True)
    url = models.URLField(max_length=5000)
    created_at = models.DateTimeField(editable=False)
    udpated_at = models.DateTimeField()
    delete_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at= timezone.now()
        self.udpated_at = timezone.now()
        return super(Project, self).save(*args, **kwargs)
        
    class Meta:
        db_table = "project"

#Creación del modelo Ip para guardar las direcciones IP de los visitantes con IPWARE
class Ip(models.Model):
    ip = models.GenericIPAddressField()

    class Meta:
        db_table = "ip_visitors"