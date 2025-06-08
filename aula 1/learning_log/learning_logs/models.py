from django.db import models

class Topicos(models.Model):
    texto = models.CharField(max_length=200)
    data_e_horario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.texto

class Entry(models.Model):
    topico = models.ForeignKey(Topicos, on_delete=models.CASCADE)
    texto = models.TextField()
    data_e_horario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:10] + "..."
