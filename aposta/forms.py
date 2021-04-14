from django import forms


PALPITE_CHOICES = [(i, str(i)) for i in range(1, 4)]


class ApostaAddProductForm(forms.Form):
    palpite = forms.TypedChoiceField(
                                choices=PALPITE_CHOICES,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)