from django.shortcuts import render, get_object_or_404
#from cart.forms import CartAddProductForm
from .models import Jogo, Rodada

def jogo_list(request, rodada_slug=None):
    rodada = None
    rodadas = Rodada.objects.all()
    jogos = Jogo.objects.filter(available=true)
    if rodada_slug:
        rodada = get_object_or_404(Rodada, slug=rodada_slug)
        jogo = jogos.filter(rodada=rodada)
        return
        render(request,
               'bets/jogo/list.html',
               {'rodada': rodada,
                'rodadas': rodadas,
                'jogos': jogos})

def jogo_detail(request, id, slug):
    jogo = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    #cart_product_form = CartAddProductForm()
    return
    render(request,
           'bets/jogo/detail.html',
           {'jogo': jogo})
           # 'cart_product_form': cart_product_form})