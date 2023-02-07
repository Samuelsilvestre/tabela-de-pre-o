from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import TabelaProduto, TabelaServico

# ----------------------------------------------------------
# class exibe tabela de serviços
class TabelaServicoView(ListView):
    model = TabelaServico
    queryset = TabelaServico.objects.all()
    template_name = 'tabela_servico.html'
    context_object_name = 'servico'

# ---------------------------------------------------------------------------------------------
# class exibe tabela de preçõs de produtos
class TabelaProdutoView(ListView):
    model = TabelaProduto
    queryset = TabelaProduto.objects.all()
    template_name = 'tabela_produto.html'
    context_object_name = 'produto'

# ------------------------------------------------------------------
# adiciona serviço a tabela
class FormServicoView(CreateView):
    model = TabelaServico
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('servico')
 
 # --------------------------------------------------------------
# adiciona produtos a tabela
class FormProdutoView(CreateView):
    model = TabelaProduto
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('produto')

# -------------------------------------------------------------------------------
# deletar servico
class DeletaServicoView(DeleteView):
    model = TabelaServico
    template_name = 'deletar.html'
    success_url = reverse_lazy('servico')
# -----------------------------------------------------------------
# deletar pridyto
class DeletaProdutoView(DeleteView):
    model = TabelaProduto
    template_name = 'deletar.html'
    success_url = reverse_lazy('produto')
    
# ---------------------------------------------------------------
# class que atualiza dados da tabela
class AtualizaProdutoView(UpdateView):
    model = TabelaProduto
    fields = '__all__'
    template_name =  'form.html'
    success_url = reverse_lazy('produto')


# ---------------------------------------------------------------
# class que atualiza dados da tabela
class AtualizaServicoView(UpdateView):
    model = TabelaServico
    fields = '__all__'
    template_name =  'form.html'
    success_url = reverse_lazy('servico')

# -------------------------------------------------------
# class index
class IndexView(TemplateView):
    template_name = 'index.html'

