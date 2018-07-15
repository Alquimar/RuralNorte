from django import forms
from extra_views import InlineFormSet as InlineFormSetFactory


from . import models


# from rural_norte.core.forms import BaseFamiliaWithImagesFormset

class BaseNestedInlineFormSet(forms.BaseInlineFormSet):
    """
    The base formset for editing Books belonging to a Publisher, and the
    BookImages belonging to those Books.
    """

    nested_formset = None

    def get_nested_formset(self):
        if not self.nested_formset:
            raise NotImplementedError
        return self.nested_formset

    def add_fields(self, form, index):
        super().add_fields(form, index)

        # Save the formset for a Book's Images in the nested property.
        nested_formset = self.get_nested_formset()
        prefix_nested = '%s-%s' % (
            # self.queryset.model._meta.db_table,
            form.prefix,
            nested_formset.get_default_prefix()
        )
        form.nested_inline = nested_formset(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix=prefix_nested
        )
        x = form

    def is_valid(self):
        """
        Also validate the nested formsets.
        """
        result = super().is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested_inline'):
                    result = result and form.nested_inline.is_valid()

        return result

    def save(self, commit=True):
        """
        Also save the nested formsets.
        """
        result = super().save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested_inline'):
                if not self._should_delete_form(form):
                    form.nested_inline.save(commit=commit)

        return result


class MembroForm(forms.ModelForm):
    class Meta:
        model = models.Membro
        fields = ('nome', 'parentesco', 'idade', 'escolaridade', 'estuda', 'cpf', 'trabalho_antes_do_lote')
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
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
                    'class': 'form-control valor',
                    'placeholder': 'Informe o CPF'
                }
            ),
            'trabalho_antes_do_lote': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


MembroInlineFormSet = forms.inlineformset_factory(
    models.Familia,
    models.Membro,
    form=MembroForm,
    extra=1,
    can_delete=True,
)


class BaseFamiliaMembroFormset(BaseNestedInlineFormSet):
    nested_formset = MembroInlineFormSet


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = models.Familia
        fields = []


FamiliaInlineNovo = forms.inlineformset_factory(
    parent_model=models.Lote,
    model=models.Familia,
    formset=BaseFamiliaMembroFormset,
    form=FamiliaForm,
    extra=0
)


class FamiliaMembrosInline(InlineFormSetFactory):
    model = models.Familia
    form_class = FamiliaForm
    formset_class = BaseFamiliaMembroFormset

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs['extra'] = 0
        return kwargs


class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ('telefone',)
        widgets = {
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control contatos',
                    'placeholder': 'Informe o telefone',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class ContatoInline(InlineFormSetFactory):
    model = models.Contato
    form_class = ContatoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1
    }


class DocumentoLoteForm(forms.ModelForm):
    class Meta:
        model = models.DocumentoLote
        fields = ('tipo_documento',)
        widgets = {
            'tipo_documento': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class DocumentoLoteInline(InlineFormSetFactory):
    model = models.DocumentoLote
    form_class = DocumentoLoteForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1
    }


class BeneficioSocialForm(forms.ModelForm):
    class Meta:
        model = models.BeneficioSocial
        fields = ('tipo_beneficio', 'outros')
        widgets = {
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


class BeneficioSocialInline(InlineFormSetFactory):
    model = models.BeneficioSocial
    form_class = BeneficioSocialForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1
    }


class AutoDeclaracaoEtniaForm(forms.ModelForm):
    class Meta:
        model = models.AutoDeclaracaoEtnia
        fields = ('tipo_declaracao_etnia', 'quantidade', 'outros')
        widgets = {
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


class AutoDeclaracaoEtniaInline(InlineFormSetFactory):
    model = models.AutoDeclaracaoEtnia
    form_class = AutoDeclaracaoEtniaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,

    }


class EstruturaOrganizativaForm(forms.ModelForm):
    class Meta:
        model = models.EstruturaOrganizativa
        fields = ('tipo_estrutura_organizativa', 'frequencia')
        widgets = {
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


class EstruturaOrganizativaInline(InlineFormSetFactory):
    model = models.EstruturaOrganizativa
    form_class = EstruturaOrganizativaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class FonteAguaForm(forms.ModelForm):
    class Meta:
        model = models.FonteAgua
        fields = ('fonte_agua', 'outra')
        widgets = {
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


class FonteAguaInline(InlineFormSetFactory):
    model = models.FonteAgua
    form_class = FonteAguaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class TratamentoAguaForm(forms.ModelForm):
    class Meta:
        model = models.TratamentoAgua
        fields = ('tratamento_agua', 'outros')
        widgets = {
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


class TratamentoAguaInline(InlineFormSetFactory):
    model = models.TratamentoAgua
    form_class = TratamentoAguaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class ConstrucaoLoteForm(forms.ModelForm):
    class Meta:
        model = models.ConstrucaoLote
        fields = ('construcao_no_lote', 'quantidade', 'outros')
        widgets = {
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


class ConstrucaoLoteInline(InlineFormSetFactory):
    model = models.ConstrucaoLote
    form_class = ConstrucaoLoteForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class BemProdutivoForm(forms.ModelForm):
    class Meta:
        model = models.BemProdutivo
        fields = ('bem_produtivo', 'quantidade', 'outros')
        widgets = {
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


class BemProdutivoInline(InlineFormSetFactory):
    model = models.BemProdutivo
    form_class = BemProdutivoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class AplicacaoCreditoForm(forms.ModelForm):
    class Meta:
        model = models.AplicacaoCredito
        fields = ('tipo_aplicacao_credito', 'valor')
        widgets = {
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


class AplicacaoCreditoInline(InlineFormSetFactory):
    model = models.AplicacaoCredito
    form_class = AplicacaoCreditoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class CreditoBancarioForm(forms.ModelForm):
    class Meta:
        model = models.CreditoBancario
        fields = ('credito_bancario', 'valor', 'adimplente', 'outros')
        widgets = {
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


class CreditoBancarioInline(InlineFormSetFactory):
    model = models.CreditoBancario
    form_class = CreditoBancarioForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class CulturaForm(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Cultura.CULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Cultura
        fields = (
            'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio', 'valor',
            'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao', 'canal_comercializacao',
            'mercado_institucional'
        )
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


class CulturaInline(InlineFormSetFactory):
    model = models.Cultura
    form_class = CulturaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class OlericulturaForm(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Olericultura.OLERICULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Olericultura
        fields = (
            'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio',
            'producao_unidade_medida', 'valor', 'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao',
            'canal_comercializacao', 'mercado_institucional'
        )
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


class OlericulturaInline(InlineFormSetFactory):
    model = models.Olericultura
    form_class = OlericulturaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class FruticulturaForm(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Fruticultura.FRUTICULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Fruticultura
        fields = (
            'tipo_producao', 'tipo_producao_outros', 'area_plantada', 'producao_consumo', 'producao_comercio', 'valor',
            'irrigacao', 'area_irrigada', 'medida_area_irrigada', 'tipo_irrigacao', 'canal_comercializacao',
            'mercado_institucional'
        )
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


class FruticulturaInline(InlineFormSetFactory):
    model = models.Fruticultura
    form_class = FruticulturaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class AtividadeExtrativistaForm(forms.ModelForm):
    class Meta:
        model = models.AtividadeExtrativista
        fields = (
            'especificacao', 'outros', 'quantidade_frutos_ano', 'quantidade_palmitos_ano', 'valor',
            'canal_comercializacao',
            'mercado_institucional'
        )
        widgets = {
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


class AtividadeExtrativistaInline(InlineFormSetFactory):
    model = models.AtividadeExtrativista
    form_class = AtividadeExtrativistaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class ProducaoFlorestalForm(forms.ModelForm):
    class Meta:
        model = models.ProducaoFlorestal
        fields = (
            'especificacao', 'outros', 'quantidade_produzida_ano', 'area_plantada', 'valor', 'canal_comercializacao'
        )
        widgets = {
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


class ProducaoFlorestalInline(InlineFormSetFactory):
    model = models.ProducaoFlorestal
    form_class = ProducaoFlorestalForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class BovinoculturaForm(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Bovinocultura.BOVINOCULTURA + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.Bovinocultura
        fields = ('tipo_criacao', 'especificacao', 'quantidade_cabecas', 'valor_cabeca')
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


class BovinoculturaInline(InlineFormSetFactory):
    model = models.Bovinocultura
    form_class = BovinoculturaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class OutraCriacaoForm(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OutraCriacao.OUTRA_CRIACAO + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.OutraCriacao
        fields = ('especificacao', 'quantidade_cabecas', 'valor_cabeca')
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


class OutraCriacaoInline(InlineFormSetFactory):
    model = models.OutraCriacao
    form_class = OutraCriacaoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class BovinoculturaLeiteiraForm(forms.ModelForm):
    class Meta:
        model = models.BovinoculturaLeiteira
        fields = (
            'especificacao', 'quantidade_cabecas_consumo', 'quantidade_cabecas_comercio', 'valor_cabeca',
            'canal_comercializacao', 'canal_comercializacao_outros'
        )
        widgets = {
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


class BovinoculturaLeiteiraInline(InlineFormSetFactory):
    model = models.BovinoculturaLeiteira
    form_class = BovinoculturaLeiteiraForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class BovinoculturaCorteForm(forms.ModelForm):
    class Meta:
        model = models.BovinoculturaCorte
        fields = (
            'especificacao', 'quantidade_cabecas_consumo', 'quantidade_cabecas_comercio', 'valor_cabeca',
            'canal_comercializacao', 'canal_comercializacao_outros'
        )
        widgets = {
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


class BovinoculturaCorteInline(InlineFormSetFactory):
    model = models.BovinoculturaCorte
    form_class = BovinoculturaCorteForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class OrigemAnimalForm(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OrigemAnimal.ORIGEM_ANIMAL + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.OrigemAnimal
        fields = (
            'especificacao', 'outros', 'producao_consumo', 'producao_comercio', 'valor', 'canal_comercializacao',
            'mercado_institucional'
        )
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


class OrigemAnimalInline(InlineFormSetFactory):
    model = models.OrigemAnimal
    form_class = OrigemAnimalForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class ProcessadoBeneficiadoForm(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.ProcessadoBeneficiado.PROCESSADO_BENEFICIADO + ((999, 'Outros'),), widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'margin-bottom: 1rem;'
            }
        ))

    class Meta:
        model = models.ProcessadoBeneficiado
        fields = (
            'especificacao', 'outros', 'producao_consumo', 'producao_comercio', 'valor', 'canal_comercializacao',
            'mercado_institucional'
        )
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


class ProcessadoBeneficiadoInline(InlineFormSetFactory):
    model = models.ProcessadoBeneficiado
    form_class = ProcessadoBeneficiadoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class NivelTecnologicoProducaoAnimalForm(forms.ModelForm):
    class Meta:
        model = models.NivelTecnologicoProducaoAnimal
        fields = ('tipo_capineira', 'area_capineira')
        widgets = {
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


class NivelTecnologicoProducaoAnimalInline(InlineFormSetFactory):
    model = models.NivelTecnologicoProducaoAnimal
    form_class = NivelTecnologicoProducaoAnimalForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class ProblemaAmbientalForm(forms.ModelForm):
    class Meta:
        model = models.ProblemaAmbiental
        fields = ('tipo_problema', 'outros')
        widgets = {
            'tipo_problema': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'outros': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Especifique'
                }
            )
        }


class ProblemaAmbientalInline(InlineFormSetFactory):
    model = models.ProblemaAmbiental
    form_class = ProblemaAmbientalForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class PraticaConservacionistaForm(forms.ModelForm):
    class Meta:
        model = models.PraticaConservacionista
        fields = ('tipo_pratica',)
        widgets = {
            'tipo_pratica': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class PraticaConservacionistaInline(InlineFormSetFactory):
    model = models.PraticaConservacionista
    form_class = PraticaConservacionistaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class LicenciamentoAmbientalForm(forms.ModelForm):
    class Meta:
        model = models.LicenciamentoAmbiental
        fields = ('tipo_atividade', 'outros')
        widgets = {
            'tipo_atividade': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'outros': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Especifique'
                }
            )
        }


class LicenciamentoAmbientalInline(InlineFormSetFactory):
    model = models.LicenciamentoAmbiental
    form_class = LicenciamentoAmbientalForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


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
                    'class': 'form-control valor',
                    'placeholder': 'Especifique'
                }
            )
        }


class AtendimentoSaudeInline(InlineFormSetFactory):
    model = models.AtendimentoSaude
    form_class = AtendimentoSaudeForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 0,
        'max_num': 1
    }


class ProgramaSaudeForm(forms.ModelForm):
    class Meta:
        model = models.ProgramaSaude
        fields = ('programa_saude',)
        widgets = {
            'programa_saude': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class ProgramaSaudeInline(InlineFormSetFactory):
    model = models.ProgramaSaude
    form_class = ProgramaSaudeForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class AtividadeFisicaForm(forms.ModelForm):
    class Meta:
        model = models.AtividadeFisica
        fields = ('atividade_fisica', 'outros')
        widgets = {
            'atividade_fisica': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            ),
            'outros': forms.TextInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Especifique'
                }
            )
        }


class AtividadeFisicaInline(InlineFormSetFactory):
    model = models.AtividadeFisica
    form_class = AtividadeFisicaForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class EspacoDisponivelForm(forms.ModelForm):
    class Meta:
        model = models.EspacoDisponivel
        fields = ('espaco_disponivel',)
        widgets = {
            'espaco_disponivel': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class EspacoDisponivelInline(InlineFormSetFactory):
    model = models.EspacoDisponivel
    form_class = EspacoDisponivelForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class EstabelecimentoEnsinoForm(forms.ModelForm):
    class Meta:
        model = models.EstabelecimentoEnsino
        fields = ('estabelecimento_ensino',)
        widgets = {
            'estabelecimento_ensino': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'margin-bottom: 1rem;'
                }
            )
        }


class EstabelecimentoEnsinoInline(InlineFormSetFactory):
    model = models.EstabelecimentoEnsino
    form_class = EstabelecimentoEnsinoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }


class NaoPossuiDocumentoForm(forms.ModelForm):
    class Meta:
        model = models.NaoPossuiDocumento
        fields = ['certidao_nascimento', 'identidade', 'cpf', 'carteira_de_trabalho', 'certidao_de_casamento_ou_uniao_estavel']
        widgets = {
            'certidao_nascimento': forms.NumberInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'identidade': forms.NumberInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'cpf': forms.NumberInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe a quantidade',
                    'style': 'margin-top: 1.5rem;'
                }
            ),
            'carteira_de_trabalho': forms.NumberInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe a quantidade'
                }
            ),
            'certidao_de_casamento_ou_uniao_estavel': forms.NumberInput(
                attrs={
                    'class': 'form-control valor',
                    'placeholder': 'Informe a quantidade'
                }
            )
        }


class NaoPossuiDocumentoInline(InlineFormSetFactory):
    model = models.NaoPossuiDocumento
    form_class = NaoPossuiDocumentoForm
    factory_kwargs = {
        'extra': 0,
        'min_num': 1,
    }
