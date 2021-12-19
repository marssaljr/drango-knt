from django.db import models

# Create your models here.
class Produto(models.Model):
	nome = models.CharField('Nome', max_length=100)
	subtitulo = models.CharField('Subtitulo', max_length=200, blank=True)
	livro = models.FileField(upload_to='')
	sinopse = models.CharField('Sinopse', max_length=1660)
	imagem = models.CharField('Url', max_length=600, blank=True)
	link_real = models.CharField('Loja', max_length=600, blank=True)
	def __str__(self):
		return f'{self.nome} {self.imagem} {self.sinopse} {self.livro}'