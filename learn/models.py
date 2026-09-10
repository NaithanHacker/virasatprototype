from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=150, null=True)
    course_desc = models.TextField()
    course_tutor_name = models.CharField(max_length=150, null=True)
    course_price = models.IntegerField()
    course_video = models.FileField(
        upload_to='videos_uploaded/', 
        null=True, 
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'wmv', 'avi', 'mov'])]
    )

    def __str__(self):
        return self.course_name