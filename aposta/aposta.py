from decimal import Decimal
from django.conf import settings
from bets.models import Jogo

"""
Classe para o gerenciamento de apostas.
1) Você tenta obter as apostas da Sessão atual.
2) Se não encontrar, será criada uma aposta vazia. 
"""
class Aposta(object):
    def __init__(self, request):
        """
        Inicializando a Aposta.
        """
        self.session = request.session
        ch_aposta = self.session.get(settings.APOSTA_SESSION_ID)
        if not ch_aposta:
            # salvar uma aposta vazia na session.
            ch_aposta =self.session[settings.CART_SESSION_ID] ={}
            self.ch_aposta = ch_aposta

    def __iter__(self):
        """
        Iterage os itens no carrinho e obtenha os jogos da base de dados.
        """
        jogos_ids = self.ch_aposta.keys()
        # get the product objects and add them to the cart
        jogos = Jogo.objects.filter(id__in=jogos_ids)

        ch_aposta = self.ch_aposta.copy()
        for jogo in jogos:
            ch_aposta[str(jogo.id)]['jogo'] = jogo

        for item in ch_aposta.values():
            item['palpite'] = item['palpite']
            #item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Quantidade de itens na Aposta ...
        """
        return sum(item['quantity'] for item in self.ch_aposta.values())


    def add(self, jogo, palpite=1, override_quantity=False):
        """
        Adicione um jogo a aposta ou atualize seu palpite.
        """
        jogo_id = str(jogo.id)
        if jogo_id not in self.ch_aposta:
            self.ch_aposta[jogo_id] = {'palpite': 0)}

        if  override_quantity:
            self.ch_aposta[jogo_id]['palpite'] = palpite
        self.save()


    def save(self):
        # marcando a session como "modified" para garantir q ela seja salva.
        self.session.modified = True


    def remove(self, jogo):
        """
        Remove o jogo da Aposta.
        """
        jogo_id = str(jogo.id)
        if jogo_id in self.ch_aposta:
            del self.ch_aposta[jogo_id]
            self.save()

    def clear(self):
        # remove cart from session
        del self.session[settings.APOSTA_SESSION_ID]
        self.save()