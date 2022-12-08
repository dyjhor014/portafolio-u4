from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    photo = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=200, null=True)
    url = models.URLField()
    created_at = models.DateTimeField(editable=False)
    done_at = models.DateTimeField(null=True)
    udpated_at = models.DateTimeField()
    delete_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at= timezone.now()
        self.udpated_at = timezone.now()
        return super(Project, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "project"