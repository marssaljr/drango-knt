from django.contrib import admin

# Register your models here.
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome','livro','imagem')

admin.site.register(Produto, ProdutoAdmin)