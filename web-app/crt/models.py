from django.db import models

# Create your models here.
class EBooksModel(models.Model):
 
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='crt_pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"