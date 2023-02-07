
from django.urls import path
from . import views
from .views import IndexView, TabelaServicoView, TabelaProdutoView
from .views import FormProdutoView, FormServicoView
from .views import DeletaProdutoView, DeletaServicoView
from .views import AtualizaServicoView, AtualizaProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('tabela/produto/', TabelaProdutoView.as_view(), name = 'produto'),
    path('tabela/servico/', TabelaServicoView.as_view(), name = 'servico'),

    #formularios
    path('form/produto/', FormProdutoView.as_view(), name = 'form_produto'),
    path('form/servico/', FormServicoView.as_view(), name = 'form_servico'),

    #deleta dados
    path('deletar/produto/<int:pk>/', DeletaProdutoView.as_view(), name = 'deletar_produto'),
    path('deletar/servico/<int:pk>/', DeletaServicoView.as_view(), name = 'deletar_servico' ),

    #atualiza dados da tabela
    path('atualiza/servico/<int:pk>/', AtualizaServicoView.as_view(), name = 'atulizar_servico'),
    path('atualiza/produto/<int:pk>/', AtualizaProdutoView.as_view(), name = 'atualizar_produto')
]
