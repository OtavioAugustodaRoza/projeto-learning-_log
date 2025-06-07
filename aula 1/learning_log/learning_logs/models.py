from django.db import models

class topicos(models.Model):
    texto = models.CharField(max_length=200)
    data_e_horario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.texto
