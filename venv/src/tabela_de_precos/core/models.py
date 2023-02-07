from django.db import models

class TabelaProduto(models.Model):
    produto = models.CharField(max_length=100, verbose_name='Produto')
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    
    class Meta:
        db_table = 'TabelaProduto'

class TabelaServico(models.Model):
    servico = models.CharField(max_length=100, verbose_name='Serviços')
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')

    class Meta:
        db_table = 'TabelaServico'