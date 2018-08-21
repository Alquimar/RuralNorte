from django import forms
from . import models

class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = '__all__'

ContatoFormSet = forms.modelformset_factory(
    models.Contato,
    form=ContatoForm,
    extra=0
)

ContatoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Contato,
    extra=0,
    min_num=1,
    fields=('telefone',),
    formset=ContatoFormSet,
    can_delete=True,
    widgets={
        'telefone': forms.TextInput(
            attrs={
                'class': 'form-control contatos',
                'placeholder': 'Informe o telefone',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class DocumentoLoteForm(forms.ModelForm):
    class Meta:
        model = models.DocumentoLote
        fields = '__all__'

DocumentoLoteFormSet = forms.modelformset_factory(
    models.DocumentoLote,
    form=DocumentoLoteForm,
    extra=0
)

DocumentoLoteInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.DocumentoLote,
    extra=0,
    min_num=1,
    fields=('tipo_documento',),
    formset=DocumentoLoteFormSet,
    can_delete=True,
    widgets={
        'tipo_documento': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class BeneficioSocialForm(forms.ModelForm):
    class Meta:
        model = models.BeneficioSocial
        fields = '__all__'

BeneficioSocialFormSet = forms.modelformset_factory(
    models.BeneficioSocial,
    form=BeneficioSocialForm,
    extra=0
)

BeneficioSocialInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.BeneficioSocial,
    extra=0,
    min_num=1,
    fields=('tipo_beneficio', 'outros'),
    formset=BeneficioSocialFormSet,
    can_delete=True,
    widgets={
        'tipo_beneficio': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class AutoDeclaracaoEtniaForm(forms.ModelForm):
    class Meta:
        model = models.AutoDeclaracaoEtnia
        fields = '__all__'

AutoDeclaracaoEtniaFormSet = forms.modelformset_factory(
    models.AutoDeclaracaoEtnia,
    form=AutoDeclaracaoEtniaForm,
    extra=0
)

AutoDeclaracaoEtniaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.AutoDeclaracaoEtnia,
    extra=0,
    min_num=1,
    fields=('tipo_declaracao_etnia', 'quantidade', 'outros'),
    formset=AutoDeclaracaoEtniaFormSet,
    can_delete=True,
    widgets={
        'tipo_declaracao_etnia': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'quantidade': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class EstruturaOrganizativaForm(forms.ModelForm):
    class Meta:
        model = models.EstruturaOrganizativa
        fields = '__all__'

EstruturaOrganizativaFormSet = forms.modelformset_factory(
    models.EstruturaOrganizativa,
    form=EstruturaOrganizativaForm,
    extra=0
)

EstruturaOrganizativaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.EstruturaOrganizativa,
    extra=0,
    min_num=1,
    fields=('tipo_estrutura_organizativa', 'frequencia'),
    formset=EstruturaOrganizativaFormSet,
    can_delete=True,
    widgets={
        'tipo_estrutura_organizativa': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'frequencia': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class FonteAguaForm(forms.ModelForm):
    class Meta:
        model = models.FonteAgua
        fields = '__all__'

FonteAguaFormSet = forms.modelformset_factory(
    models.FonteAgua,
    form=FonteAguaForm,
    extra=0
)

FonteAguaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.FonteAgua,
    extra=0,
    min_num=1,
    fields=('fonte_agua', 'outra'),
    formset=FonteAguaFormSet,
    can_delete=True,
    widgets={
        'fonte_agua': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outra': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class TratamentoAguaForm(forms.ModelForm):
    class Meta:
        model = models.TratamentoAgua
        fields = '__all__'

TratamentoAguaFormSet = forms.modelformset_factory(
    models.TratamentoAgua,
    form=TratamentoAguaForm,
    extra=0
)

TratamentoAguaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.TratamentoAgua,
    extra=0,
    min_num=1,
    fields=('tratamento_agua', 'outros'),
    formset=TratamentoAguaFormSet,
    can_delete=True,
    widgets={
        'tratamento_agua': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class AguaParaAnimaisPlantioForm(forms.ModelForm):
    class Meta:
        model = models.AguaParaAnimaisPlantio
        fields = '__all__'

AguaParaAnimaisPlantioFormSet = forms.modelformset_factory(
    models.AguaParaAnimaisPlantio,
    form=AguaParaAnimaisPlantioForm,
    extra=0
)

AguaParaAnimaisPlantioInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.AguaParaAnimaisPlantio,
    extra=0,
    min_num=1,
    fields=('agua_para_animais_plantio', 'outros'),
    formset=AguaParaAnimaisPlantioFormSet,
    can_delete=True,
    widgets={
        'agua_para_animais_plantio': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class ConstrucaoLoteForm(forms.ModelForm):
    class Meta:
        model = models.ConstrucaoLote
        fields = '__all__'

ConstrucaoLoteFormSet = forms.modelformset_factory(
    models.ConstrucaoLote,
    form=ConstrucaoLoteForm,
    extra=0
)

ConstrucaoLoteInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.ConstrucaoLote,
    extra=0,
    min_num=1,
    fields=('construcao_no_lote', 'quantidade', 'outros'),
    formset=ConstrucaoLoteFormSet,
    can_delete=True,
    widgets={
        'construcao_no_lote': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'quantidade': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class BemProdutivoForm(forms.ModelForm):
    class Meta:
        model = models.BemProdutivo
        fields = '__all__'

BemProdutivoFormSet = forms.modelformset_factory(
    models.BemProdutivo,
    form=BemProdutivoForm,
    extra=0
)

BemProdutivoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.BemProdutivo,
    extra=0,
    min_num=1,
    fields=('bem_produtivo', 'quantidade', 'outros'),
    formset=BemProdutivoFormSet,
    can_delete=True,
    widgets={
        'bem_produtivo': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'quantidade': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class AplicacaoCreditoForm(forms.ModelForm):
    class Meta:
        model = models.AplicacaoCredito
        fields = '__all__'

AplicacaoCreditoFormSet = forms.modelformset_factory(
    models.AplicacaoCredito,
    form=AplicacaoCreditoForm,
    extra=0
)

AplicacaoCreditoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.AplicacaoCredito,
    extra=0,
    min_num=1,
    fields=('tipo_aplicacao_credito', 'valor'),
    formset=AplicacaoCreditoFormSet,
    can_delete=True,
    widgets={
        'tipo_aplicacao_credito': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'valor': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        )
    }
)

class CreditoBancarioForm(forms.ModelForm):
    class Meta:
        model = models.CreditoBancario
        fields = '__all__'

CreditoBancarioFormSet = forms.modelformset_factory(
    models.CreditoBancario,
    form=CreditoBancarioForm,
    extra=0
)

CreditoBancarioInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.CreditoBancario,
    extra=0,
    min_num=1,
    fields=('credito_bancario', 'valor', 'adimplente', 'outros'),
    formset=CreditoBancarioFormSet,
    can_delete=True,
    widgets={
        'credito_bancario': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'valor': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'adimplente': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class CulturaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CulturaForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['tipo_producao'].required = False

    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Cultura.CULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Cultura
        fields = '__all__'
        widgets = {
            'tipo_producao_outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            ),
            'area_plantada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'producao_consumo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade',
                }
            ),
            'producao_comercio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            ),
            'irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'area_irrigada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'medida_area_irrigada': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'tipo_irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'canal_comercializacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'mercado_institucional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }

CulturaFormSet = forms.modelformset_factory(
    models.Olericultura,
    form=CulturaForm,
    extra=0
)

CulturaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Cultura,
    extra=0,
    min_num=1,
    fields=(
        'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio', 'valor',
        'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao', 'canal_comercializacao', 'mercado_institucional'
    ),
    form=CulturaForm,
    formset=CulturaFormSet,
    can_delete=True
)

class OlericulturaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(OlericulturaForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['tipo_producao'].required = False

    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Olericultura.OLERICULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Olericultura
        fields = '__all__'
        widgets = {
            'tipo_producao_outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            ),
            'area_plantada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'producao_consumo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade',
                }
            ),
            'producao_comercio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'producao_unidade_medida': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            ),
            'irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'area_irrigada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'medida_area_irrigada': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'tipo_irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'canal_comercializacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'mercado_institucional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }

OlericulturaFormSet = forms.modelformset_factory(
    models.Olericultura,
    form=OlericulturaForm,
    extra=0
)

OlericulturaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Olericultura,
    extra=0,
    min_num=1,
    fields=(
        'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio',
        'producao_unidade_medida', 'valor', 'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao',
        'canal_comercializacao', 'mercado_institucional'
    ),
    form=OlericulturaForm,
    formset=OlericulturaFormSet,
    can_delete=True
)

class FruticulturaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(FruticulturaForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['tipo_producao'].required = False

    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Fruticultura.FRUTICULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Fruticultura
        fields = '__all__'
        widgets = {
            'tipo_producao_outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            ),
            'area_plantada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'producao_consumo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade',
                }
            ),
            'producao_comercio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            ),
            'irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'area_irrigada': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'medida_area_irrigada': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'tipo_irrigacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'canal_comercializacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'mercado_institucional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }

FruticulturaFormSet = forms.modelformset_factory(
    models.Fruticultura,
    form=FruticulturaForm,
    extra=0
)

FruticulturaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Fruticultura,
    extra=0,
    min_num=1,
    fields=(
        'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio', 'valor',
        'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao', 'canal_comercializacao', 'mercado_institucional'
    ),
    form=FruticulturaForm,
    formset=FruticulturaFormSet,
    can_delete=True
)

class AtividadeExtrativistaForm(forms.ModelForm):
    class Meta:
        model = models.AtividadeExtrativista
        fields = '__all__'

AtividadeExtrativistaFormSet = forms.modelformset_factory(
    models.AtividadeExtrativista,
    form=AtividadeExtrativistaForm,
    extra=0
)

AtividadeExtrativistaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.AtividadeExtrativista,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'outros', 'quantidade_frutos_ano', 'quantidade_palmitos_ano', 'valor', 'canal_comercializacao',
        'mercado_institucional'
    ),
    formset=AtividadeExtrativistaFormSet,
    can_delete=True,
    widgets={
        'especificacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        ),
        'quantidade_frutos_ano': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'quantidade_palmitos_ano': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade',
                'style': 'max-width: 95%'
            }
        ),
        'valor': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'canal_comercializacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'mercado_institucional': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class ProducaoFlorestalForm(forms.ModelForm):
    class Meta:
        model = models.ProducaoFlorestal
        fields = '__all__'

ProducaoFlorestalFormSet = forms.modelformset_factory(
    models.ProducaoFlorestal,
    form=ProducaoFlorestalForm,
    extra=0
)

ProducaoFlorestalInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.ProducaoFlorestal,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'outros', 'quantidade_produzida_ano', 'area_plantada', 'valor', 'canal_comercializacao'
    ),
    formset=ProducaoFlorestalFormSet,
    can_delete=True,
    widgets={
        'especificacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        ),
        'quantidade_produzida_ano': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'area_plantada': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o valor'
            }
        ),
        'valor': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'canal_comercializacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class BovinoculturaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(BovinoculturaForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['especificacao'].required = False

    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Bovinocultura.BOVINOCULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Bovinocultura
        fields = '__all__'
        widgets = {
            'tipo_criacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'especificacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'quantidade_cabecas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor_cabeca': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            )
        }

BovinoculturaFormSet = forms.modelformset_factory(
    models.Bovinocultura,
    form=BovinoculturaForm,
    extra=0
)

BovinoculturaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Bovinocultura,
    extra=0,
    min_num=1,
    fields=('tipo_criacao', 'especificacao', 'quantidade_cabecas', 'valor_cabeca'),
    form=BovinoculturaForm,
    formset=BovinoculturaFormSet,
    can_delete=True
)

class OutraCriacaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(OutraCriacaoForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['especificacao'].required = False

    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OutraCriacao.OUTRA_CRIACAO + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.OutraCriacao
        fields = '__all__'
        widgets = {
            'especificacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'quantidade_cabecas': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor_cabeca': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            )
        }

OutraCriacaoFormSet = forms.modelformset_factory(
    models.OutraCriacao,
    form=OutraCriacaoForm,
    extra=0
)

OutraCriacaoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.OutraCriacao,
    extra=0,
    min_num=1,
    fields=('especificacao', 'quantidade_cabecas', 'valor_cabeca'),
    form=OutraCriacaoForm,
    formset=OutraCriacaoFormSet,
    can_delete=True
)

class BovinoculturaLeiteiraForm(forms.ModelForm):
    class Meta:
        model = models.BovinoculturaLeiteira
        fields = '__all__'

BovinoculturaLeiteiraFormSet = forms.modelformset_factory(
    models.BovinoculturaLeiteira,
    form=BovinoculturaLeiteiraForm,
    extra=0
)

BovinoculturaLeiteiraInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.BovinoculturaLeiteira,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'quantidade_cabecas_consumo', 'quantidade_cabecas_comercio', 'valor_cabeca',
        'canal_comercializacao', 'canal_comercializacao_outros'
    ),
    formset=BovinoculturaLeiteiraFormSet,
    can_delete=True,
    widgets={
        'especificacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'quantidade_cabecas_consumo': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'quantidade_cabecas_comercio': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'valor_cabeca': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'canal_comercializacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'canal_comercializacao_outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class BovinoculturaCorteForm(forms.ModelForm):
    class Meta:
        model = models.BovinoculturaCorte
        fields = '__all__'

BovinoculturaCorteFormSet = forms.modelformset_factory(
    models.BovinoculturaCorte,
    form=BovinoculturaCorteForm,
    extra=0
)

BovinoculturaCorteInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.BovinoculturaCorte,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'quantidade_cabecas_consumo', 'quantidade_cabecas_comercio', 'valor_cabeca',
        'canal_comercializacao', 'canal_comercializacao_outros'
    ),
    formset=BovinoculturaCorteFormSet,
    can_delete=True,
    widgets={
        'especificacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'quantidade_cabecas_consumo': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'quantidade_cabecas_comercio': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'valor_cabeca': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'canal_comercializacao': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'canal_comercializacao_outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class OrigemAnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(OrigemAnimalForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['especificacao'].required = False

    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OrigemAnimal.ORIGEM_ANIMAL + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.OrigemAnimal
        fields = '__all__'
        widgets = {
            'outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            ),
            'producao_consumo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'producao_comercio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            ),
            'canal_comercializacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'mercado_institucional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }

OrigemAnimalFormSet = forms.modelformset_factory(
    models.OrigemAnimal,
    form=OrigemAnimalForm,
    extra=0
)

OrigemAnimalInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.OrigemAnimal,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'outros', 'producao_consumo', 'producao_comercio', 'valor', 'canal_comercializacao',
        'mercado_institucional'
    ),
    form=OrigemAnimalForm,
    formset=OrigemAnimalFormSet,
    can_delete=True
)

class ProcessadoBeneficiadoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProcessadoBeneficiadoForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['especificacao'].required = False

    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.ProcessadoBeneficiado.PROCESSADO_BENEFICIADO + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.ProcessadoBeneficiado
        fields = '__all__'
        widgets = {
            'outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            ),
            'producao_consumo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'producao_comercio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'valor': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe o valor'
                }
            ),
            'canal_comercializacao': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'mercado_institucional': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }

ProcessadoBeneficiadoFormSet = forms.modelformset_factory(
    models.ProcessadoBeneficiado,
    form=ProcessadoBeneficiadoForm,
    extra=0
)

ProcessadoBeneficiadoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.ProcessadoBeneficiado,
    extra=0,
    min_num=1,
    fields=(
        'especificacao', 'outros', 'producao_consumo', 'producao_comercio', 'valor', 'canal_comercializacao',
        'mercado_institucional'
    ),
    form=ProcessadoBeneficiadoForm,
    formset=ProcessadoBeneficiadoFormSet,
    can_delete=True
)

class NivelTecnologicoProducaoAnimalForm(forms.ModelForm):
    class Meta:
        model = models.NivelTecnologicoProducaoAnimal
        fields = '__all__'

NivelTecnologicoProducaoAnimalFormSet = forms.modelformset_factory(
    models.NivelTecnologicoProducaoAnimal,
    form=NivelTecnologicoProducaoAnimalForm,
    extra=0
)

NivelTecnologicoProducaoAnimalInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.NivelTecnologicoProducaoAnimal,
    extra=0,
    min_num=1,
    fields=('tipo_capineira', 'area_capineira'),
    formset=NivelTecnologicoProducaoAnimalFormSet,
    can_delete=True,
    widgets={
        'tipo_capineira': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'area_capineira': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a área'
            }
        )
    }
)

class ProblemaAmbientalForm(forms.ModelForm):
    class Meta:
        model = models.ProblemaAmbiental
        fields = '__all__'

ProblemaAmbientalFormSet = forms.modelformset_factory(
    models.ProblemaAmbiental,
    form=ProblemaAmbientalForm,
    extra=0
)

ProblemaAmbientalInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.ProblemaAmbiental,
    extra=0,
    min_num=1,
    fields=('tipo_problema', 'outros'),
    formset=ProblemaAmbientalFormSet,
    can_delete=True,
    widgets={
        'tipo_problema': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class PraticaConservacionistaForm(forms.ModelForm):
    class Meta:
        model = models.PraticaConservacionista
        fields = '__all__'

PraticaConservacionistaFormSet = forms.modelformset_factory(
    models.PraticaConservacionista,
    form=PraticaConservacionistaForm,
    extra=0
)

PraticaConservacionistaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.PraticaConservacionista,
    extra=0,
    min_num=1,
    fields=('tipo_pratica',),
    formset=PraticaConservacionistaFormSet,
    can_delete=True,
    widgets={
        'tipo_pratica': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class DestinoLixoDomesticoNaoOrganicoForm(forms.ModelForm):
    class Meta:
        model = models.DestinoLixoDomesticoNaoOrganico
        fields = '__all__'

DestinoLixoDomesticoNaoOrganicoFormSet = forms.modelformset_factory(
    models.DestinoLixoDomesticoNaoOrganico,
    form=DestinoLixoDomesticoNaoOrganicoForm,
    extra=0
)

DestinoLixoDomesticoNaoOrganicoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.DestinoLixoDomesticoNaoOrganico,
    extra=0,
    min_num=1,
    fields=('destino_lixo_domestico_nao_organico',),
    formset=DestinoLixoDomesticoNaoOrganicoFormSet,
    can_delete=True,
    widgets={
        'destino_lixo_domestico_nao_organico': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class DestinoMaterialOrganicoForm(forms.ModelForm):
    class Meta:
        model = models.DestinoMaterialOrganico
        fields = '__all__'

DestinoMaterialOrganicoFormSet = forms.modelformset_factory(
    models.DestinoMaterialOrganico,
    form=DestinoMaterialOrganicoForm,
    extra=0
)

DestinoMaterialOrganicoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.DestinoMaterialOrganico,
    extra=0,
    min_num=1,
    fields=('destino_material_organico',),
    formset=DestinoMaterialOrganicoFormSet,
    can_delete=True,
    widgets={
        'destino_material_organico': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class LicenciamentoAmbientalForm(forms.ModelForm):
    class Meta:
        model = models.LicenciamentoAmbiental
        fields = '__all__'

LicenciamentoAmbientalFormSet = forms.modelformset_factory(
    models.LicenciamentoAmbiental,
    form=LicenciamentoAmbientalForm,
    extra=0
)

LicenciamentoAmbientalInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.LicenciamentoAmbiental,
    extra=0,
    min_num=1,
    fields=('tipo_atividade', 'outros'),
    formset=LicenciamentoAmbientalFormSet,
    can_delete=True,
    widgets={
        'tipo_atividade': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class AtendimentoSaudeForm(forms.ModelForm):
    class Meta:
        model = models.AtendimentoSaude
        fields = ['hospital', 'posto_saude', 'farmacia', 'outros', 'outros_especificacao']
        widgets = {
            'hospital': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'posto_saude': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'farmacia': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'outros': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'outros_especificacao': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Especifique'
                }
            )
        }

class ProgramaSaudeForm(forms.ModelForm):
    class Meta:
        model = models.ProgramaSaude
        fields = '__all__'

ProgramaSaudeFormSet = forms.modelformset_factory(
    models.ProgramaSaude,
    form=ProgramaSaudeForm,
    extra=0
)

ProgramaSaudeInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.ProgramaSaude,
    extra=0,
    min_num=1,
    fields=('programa_saude',),
    formset=ProgramaSaudeFormSet,
    can_delete=True,
    widgets={
        'programa_saude': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class AtividadeFisicaForm(forms.ModelForm):
    class Meta:
        model = models.AtividadeFisica
        fields = '__all__'

AtividadeFisicaFormSet = forms.modelformset_factory(
    models.AtividadeFisica,
    form=AtividadeFisicaForm,
    extra=0
)

AtividadeFisicaInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.AtividadeFisica,
    extra=0,
    min_num=1,
    fields=('atividade_fisica', 'outros'),
    formset=AtividadeFisicaFormSet,
    can_delete=True,
    widgets={
        'atividade_fisica': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        )
    }
)

class EspacoDisponivelForm(forms.ModelForm):
    class Meta:
        model = models.EspacoDisponivel
        fields = '__all__'

EspacoDisponivelFormSet = forms.modelformset_factory(
    models.EspacoDisponivel,
    form=EspacoDisponivelForm,
    extra=0
)

EspacoDisponivelInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.EspacoDisponivel,
    extra=0,
    min_num=1,
    fields=('espaco_disponivel',),
    formset=EspacoDisponivelFormSet,
    can_delete=True,
    widgets={
        'espaco_disponivel': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class EstabelecimentoEnsinoForm(forms.ModelForm):
    class Meta:
        model = models.EstabelecimentoEnsino
        fields = '__all__'

EstabelecimentoEnsinoFormSet = forms.modelformset_factory(
    models.EstabelecimentoEnsino,
    form=EstabelecimentoEnsinoForm,
    extra=0
)

EstabelecimentoEnsinoInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.EstabelecimentoEnsino,
    extra=0,
    min_num=1,
    fields=('estabelecimento_ensino',),
    formset=EstabelecimentoEnsinoFormSet,
    can_delete=True,
    widgets={
        'estabelecimento_ensino': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class NaoPossuiDocumentoForm(forms.ModelForm):
    class Meta:
        model = models.NaoPossuiDocumento
        fields = ['certidao_nascimento', 'identidade', 'cpf', 'carteira_de_trabalho', 'certidao_de_casamento_ou_uniao_estavel']
        widgets = {
            'certidao_nascimento': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'identidade': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'cpf': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade',
                    'style': 'margin-top: 1.5rem;'
                }
            ),
            'carteira_de_trabalho': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'certidao_de_casamento_ou_uniao_estavel': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade'
                }
            )
        }

class MembroForm(forms.ModelForm):
    class Meta:
        model = models.Membro
        fields = '__all__'

MembroFormSet = forms.modelformset_factory(
    models.Membro,
    form=MembroForm,
    extra=0
)

MembroInlineFormSet = forms.inlineformset_factory(
    models.Lote,
    models.Membro,
    extra=0,
    min_num=1,
    fields=(
        'codigo_familia', 'nome', 'parentesco', 'idade', 'escolaridade', 'estuda', 'cpf', 'trabalho_antes_do_lote',
        'trabalho_fora_lote_quantidade_dias_ano', 'trabalho_fora_lote_valor_diaria', 'uso_frequente_bebida_alcoolica',
        'uso_frequente_cigarro', 'uso_frequente_remedios_alto_custo', 'uso_frequente_outros', 'opcao_ensino_utilizada',
        'opcao_ensino_utilizada_distancia_ate_escola', 'opcao_ensino_utilizada_oferta_de_transporte'
    ),
    formset=MembroFormSet,
    can_delete=True,
    widgets={
        'codigo_familia': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o código'
            }
        ),
        'nome': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o nome'
            }
        ),
        'parentesco': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'idade': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a idade'
            }
        ),
        'escolaridade': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'estuda': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'cpf': forms.TextInput(
            attrs={
                'class': 'form-control cpf',
                'placeholder': 'Informe o CPF'
            }
        ),
        'trabalho_antes_do_lote': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'trabalho_fora_lote_quantidade_dias_ano': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'trabalho_fora_lote_valor_diaria': forms.TextInput(
            attrs={
                'class': 'form-control valor',
                'placeholder': 'Informe o valor'
            }
        ),
        'uso_frequente_bebida_alcoolica': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'uso_frequente_cigarro': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'uso_frequente_remedios_alto_custo': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'uso_frequente_outros': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Especifique'
            }
        ),
        'opcao_ensino_utilizada': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ),
        'opcao_ensino_utilizada_distancia_ate_escola': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a quantidade'
            }
        ),
        'opcao_ensino_utilizada_oferta_de_transporte': forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        )
    }
)

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = models.Lote
        fields = [
            'projeto_assentamento', 'codigo_sipra', 'data_homologacao', 'data_visita', 'area', 'numero',
            'ocupante_irregular', 'ocupante_irregular_tempo', 'entrevistador', 'coordenada_x', 'coordenada_y',
            'banda_coordenada', 'outra_familia_no_lote', 'cad_unico', 'recebe_beneficio_social', 'moradia_assentamento',
            'tipo_parede_externa', 'tipo_instalacao_eletrica', 'tipo_instalacao_sanitaria', 'localizacao_fonte_agua',
            'abastecimento_agua_suficiente', 'quantas_familias_utilizam_mesma_fonte_agua',
            'quantidade_familias_utilizacao_mesma_fonte_agua', 'regularidade_abastecimento_agua', 'tipo_estrada_acesso',
            'situacao_estrada_acesso', 'situacao_cercado_lote', 'possui_pastagem_em_pastejo_rotacionado',
            'pratica_inseminacao_artificial_no_rebanho_leiteiro', 'area_preservacao_permanente',
            'area_preservacao_permanente_cercada', 'area_pastejo_rotacionado',
            'necessita_autoriacao_exploracao_florestal_queima_controlada', 'qualidade_servico_saude',
            'frequencia_atividade_fisica', 'oferta_transporte_interno'
        ]

        widgets = {
            'projeto_assentamento': forms.HiddenInput(),
            'codigo_sipra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o código'
                }
            ),
            'data_homologacao': forms.DateInput(
                attrs={
                    'class': 'form-control data',
                    # 'type': 'date'
                }
            ),
            'data_visita': forms.DateInput(
                attrs={
                    'class': 'form-control data'
                    # 'type': 'date'
                }
            ),
            'area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a área'
                }
            ),
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o número'
                }
            ),
            'ocupante_irregular': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ocupante_irregular_tempo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o tempo'
                }
            ),
            'entrevistador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o nome'
                }
            ),
            'coordenada_x': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a coordenada'
                }
            ),
            'coordenada_y': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a coordenada'
                }
            ),
            'banda_coordenada': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a banda'
                }
            ),
            'outra_familia_no_lote': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cad_unico': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'recebe_beneficio_social': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'moradia_assentamento': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 8.5%;'
                }
            ),
            'tipo_parede_externa': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_instalacao_eletrica': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 8.5%;'
                }
            ),
            'tipo_instalacao_sanitaria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-top: 8.5%;'
                }
            ),
            'localizacao_fonte_agua': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'abastecimento_agua_suficiente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantas_familias_utilizam_mesma_fonte_agua': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantidade_familias_utilizacao_mesma_fonte_agua': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe a quantidade',
                    'style': 'margin-top: 12%;'
                }
            ),
            'agua_para_animais_plantio': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'agua_para_animais_plantio_outros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o nome'
                }
            ),
            'regularidade_abastecimento_agua': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo_estrada_acesso': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': "margin-top: 1.5rem;"
                }
            ),
            'situacao_estrada_acesso': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'situacao_cercado_lote': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': "margin-top: 1.5rem;"
                }
            ),
            'possui_pastagem_em_pastejo_rotacionado': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pratica_inseminacao_artificial_no_rebanho_leiteiro': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'area_preservacao_permanente': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'area_preservacao_permanente_cercada': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'destino_lixo_domestico_nao_organico': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'destino_material_organico': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'possui_capineira': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'area_pastejo_rotacionado': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Informe o tamanho'
                }
            ),
            'necessita_licenciamento_ambiental': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'necessita_autoriacao_exploracao_florestal_queima_controlada': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'qualidade_servico_saude': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'frequencia_atividade_fisica': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'oferta_transporte_interno': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
