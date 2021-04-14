from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bets.models import Jogo
from .aposta import Aposta
from .forms import ApostaAddProductForm

"""
View para adicionar jogos a aposta e atualizar seus palpites.
O decorador permite apenas solitações POST.
"""
@require_POST
def aposta_add(request, jogo_id):
    aposta = Aposta(request)
    jogo = get_object_or_404(Jogo, id=jogo_id)
    form = ApostaAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        aposta.add(jogo=jogo,
                 palpite=cd['palpite'],
                 override_palpite=cd['override'])
    return redirect('aposta:aposta_detail')


"""
Views q remove itens/jogos da aposta .
"""
@require_POST
def aposta_remove(request, jogo_id):
    aposta = Aposta(request)
    jogo = get_object_or_404(Jogo, id=jogo_id)
    aposta.remove(jogo)
    return redirect('aposta:aposta_detail')

"""
Views q exibe a Aposta e seus itens/jogos.
"""
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_palpite_form'] = ApostaAddProductForm(initial={'palpite': item['palpite'],
                                                                   'override': True})
    return render(request, 'aposta/detail.html', {'aposta': aposta})