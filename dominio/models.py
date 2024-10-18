from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    nascimento = models.DateField()
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    data_publicacao = models.DateField()
    numero_paginas = models.IntegerField()
    sinopse = models.TextField()
    idioma = models.CharField(max_length=30, default="Português")
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"