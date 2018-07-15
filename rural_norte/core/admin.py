from django.contrib import admin
from django import forms
import nested_admin
from django.db.models import Q

from . import models
from django import forms
from django.utils.safestring import mark_safe
from django.template.defaultfilters import date


class CulturaFormAdmin(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Cultura.CULTURA + ((999, 'Outros'),))

    class Meta:
        model = models.Cultura
        fields = '__all__'


class OlericulturaFormAdmin(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Olericultura.OLERICULTURA + ((999, 'Outros'),))

    class Meta:
        model = models.Olericultura
        fields = '__all__'


class FruticulturaFormAdmin(forms.ModelForm):
    tipo_producao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Fruticultura.FRUTICULTURA + ((999, 'Outros'),))

    class Meta:
        model = models.Fruticultura
        fields = '__all__'


class BovinoculturaFormAdmin(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.Bovinocultura.BOVINOCULTURA + ((999, 'Outros'),))

    class Meta:
        model = models.Bovinocultura
        fields = '__all__'


class OutraCriacaoFormAdmin(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OutraCriacao.OUTRA_CRIACAO + ((999, 'Outros'),))

    class Meta:
        model = models.OutraCriacao
        fields = '__all__'


class OrigemAnimalFormAdmin(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.OrigemAnimal.ORIGEM_ANIMAL + ((999, 'Outros'),))

    class Meta:
        model = models.OrigemAnimal
        fields = '__all__'


class ProcessadoBeneficiadoFormAdmin(forms.ModelForm):
    especificacao = forms.ChoiceField(
        choices=(('', '---------'),) + models.ProcessadoBeneficiado.PROCESSADO_BENEFICIADO + ((999, 'Outros'),))

    class Meta:
        model = models.ProcessadoBeneficiado
        fields = '__all__'


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'ano', 'cadastrado_em')
    search_fields = ['numero', 'ano']
    list_filter = ['ano', 'cadastrado_em']
    exclude = ['desativado_por', 'desativado_em']


class ProjetoAssentamentoAdmin(admin.ModelAdmin):

    def get_data_criacao(self, obj):
        return date(obj.data_criacao, 'd/m/Y')

    get_data_criacao.admin_order_field = 'data_criacao'
    get_data_criacao.short_description = 'Data de Criação'

    def get_total_beneficiarios(self, obj):
        return obj.lotes.count()

    get_total_beneficiarios.short_description = 'Total de Beneficiários'

    list_display = ('codigo', 'nome', 'municipio', 'contrato', 'get_data_criacao', 'get_total_beneficiarios', 'capacidade_projeto')
    search_fields = ['codigo', 'nome', 'municipio']
    list_filter = ['contrato', 'municipio', 'cadastrado_em', 'modificado_em']
    exclude = ['desativado_por', 'desativado_em']


class OpcaoEnsinoUtilizadaInlineAdmin(nested_admin.NestedStackedInline):
    model = models.OpcaoEnsinoUtilizada
    exclude = ['desativado_por', 'desativado_em']
    delete = False


class UsoFrequenteInlineAdmin(nested_admin.NestedStackedInline):
    model = models.UsoFrequente
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    delete = False


class RendaTrabalhoForaLoteInlineAdmin(nested_admin.NestedStackedInline):
    model = models.RendaTrabalhoForaLote
    exclude = ['desativado_por', 'desativado_em']
    delete = False


class MembroInlineAdmin(nested_admin.NestedStackedInline):
    model = models.Membro
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    delete = False
    inlines = [RendaTrabalhoForaLoteInlineAdmin, UsoFrequenteInlineAdmin, OpcaoEnsinoUtilizadaInlineAdmin]


class FamiliaInlineAdmin(nested_admin.NestedStackedInline):
    model = models.Familia
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    delete = False
    inlines = [MembroInlineAdmin]
    insert_after = 'coordenada_y'


class ContatoInlineAdmin(admin.StackedInline):
    model = models.Contato
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'outra_familia_no_lote'


class DocumentoLoteInlineAdmin(admin.StackedInline):
    model = models.DocumentoLote
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'ocupante_irregular_tempo'


class BeneficioSocialInlineAdmin(admin.StackedInline):
    model = models.BeneficioSocial
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'recebe_beneficio_social'


class EstruturaOrganizativaInlineAdmin(admin.StackedInline):
    model = models.EstruturaOrganizativa
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'recebe_beneficio_social'


class AutoDeclaracaoEtniaInlineAdmin(admin.StackedInline):
    model = models.AutoDeclaracaoEtnia
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'recebe_beneficio_social'


class FonteAguaInlineAdmin(admin.StackedInline):
    model = models.FonteAgua
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'tipo_instalacao_sanitaria'


class TratamentoAguaInlineAdmin(admin.StackedInline):
    model = models.TratamentoAgua
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'tipo_instalacao_sanitaria'


class ConstrucaoLoteInlineAdmin(admin.StackedInline):
    model = models.ConstrucaoLote
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class BemProdutivoInlineAdmin(admin.StackedInline):
    model = models.BemProdutivo
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class AplicacaoCreditoInlineAdmin(admin.StackedInline):
    model = models.AplicacaoCredito
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class CreditoBancarioInlineAdmin(admin.StackedInline):
    model = models.CreditoBancario
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class CulturaInlineAdmin(admin.StackedInline):
    model = models.Cultura
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = CulturaFormAdmin
    insert_after = 'situacao_cercado_lote'


class OlericulturaInlineAdmin(admin.StackedInline):
    model = models.Olericultura
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = OlericulturaFormAdmin
    insert_after = 'situacao_cercado_lote'


class FruticulturaInlineAdmin(admin.StackedInline):
    model = models.Fruticultura
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = FruticulturaFormAdmin
    insert_after = 'situacao_cercado_lote'


class AtividadeExtrativistaInlineAdmin(admin.StackedInline):
    model = models.AtividadeExtrativista
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class ProducaoFlorestalInlineAdmin(admin.StackedInline):
    model = models.ProducaoFlorestal
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class BovinoculturaInlineAdmin(admin.StackedInline):
    model = models.Bovinocultura
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = BovinoculturaFormAdmin
    insert_after = 'situacao_cercado_lote'


class OutraCriacaoInlineAdmin(admin.StackedInline):
    model = models.OutraCriacao
    exclude = ['classificacao', 'tipo_criacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = OutraCriacaoFormAdmin
    insert_after = 'situacao_cercado_lote'


class ProblemaAmbientalInlineAdmin(admin.StackedInline):
    model = models.ProblemaAmbiental
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'area_preservacao_permanente_cercada'


class PraticaConservacionistaInlineAdmin(admin.StackedInline):
    model = models.PraticaConservacionista
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'area_preservacao_permanente_cercada'


class LicenciamentoAmbientalInlineAdmin(admin.StackedInline):
    model = models.LicenciamentoAmbiental
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'area_preservacao_permanente_cercada'


class AtendimentoSaudeInlineAdmin(admin.StackedInline):
    model = models.AtendimentoSaude
    exclude = ['desativado_por', 'desativado_em']
    insert_after = 'necessita_autoriacao_exploracao_florestal_queima_controlada'


class ProgramaSaudeInlineAdmin(admin.StackedInline):
    model = models.ProgramaSaude
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'necessita_autoriacao_exploracao_florestal_queima_controlada'


class AtividadeFisicaInlineAdmin(admin.StackedInline):
    model = models.AtividadeFisica
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'qualidade_servico_saude'


class EspacoDisponivelInlineAdmin(admin.StackedInline):
    model = models.EspacoDisponivel
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'frequencia_atividade_fisica'


class EstabelecimentoEnsinoInlineAdmin(admin.StackedInline):
    model = models.EstabelecimentoEnsino
    exclude = ['desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'frequencia_atividade_fisica'


class BovinoculturaLeiteiraInlineAdmin(admin.StackedInline):
    model = models.BovinoculturaLeiteira
    exclude = ['tipo_criacao', 'desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class BovinoculturaCorteInlineAdmin(admin.StackedInline):
    model = models.BovinoculturaCorte
    exclude = ['tipo_criacao', 'desativado_por', 'desativado_em']
    extra = 1
    insert_after = 'situacao_cercado_lote'


class OrigemAnimalInlineAdmin(admin.StackedInline):
    model = models.OrigemAnimal
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = OrigemAnimalFormAdmin
    insert_after = 'situacao_cercado_lote'


class NivelTecnologicoProducaoAnimalInlineAdmin(admin.StackedInline):
    model = models.NivelTecnologicoProducaoAnimal
    extra = 1
    exclude = ['desativado_por', 'desativado_em']
    insert_after = 'situacao_cercado_lote'


class ProcessadoBeneficiadoInlineAdmin(admin.StackedInline):
    model = models.ProcessadoBeneficiado
    exclude = ['classificacao', 'desativado_por', 'desativado_em']
    extra = 1
    form = ProcessadoBeneficiadoFormAdmin
    insert_after = 'pratica_inseminacao_artificial_no_rebanho_leiteiro'


class NaoPossuiDocumentoInlineAdmin(admin.StackedInline):
    model = models.NaoPossuiDocumento
    exclude = ['desativado_por', 'desativado_em']


# class ContratoListFilter(admin.SimpleListFilter):
#     title = 'Contrato'
#     parameter_name = 'contrato'
#
#     def lookups(self, request, model_admin):
#         return models.ProjetoAssentamento.contrato_choices
#
#     def queryset(self, request, queryset):
#         value = self.value()
#         if value:
#             value = int(value)
#             if value == models.ProjetoAssentamento.CONTRATO_10:
#                 queryset = queryset.filter(
#                     Q(projeto_assentamento__contrato=models.ProjetoAssentamento.CONTRATO_10)
#                 )
#             if value == models.ProjetoAssentamento.CONTRATO_11:
#                 queryset = queryset.filter(
#                     Q(projeto_assentamento__contrato=models.ProjetoAssentamento.CONTRATO_11)
#                 )
#             if value == models.ProjetoAssentamento.CONTRATO_18:
#                 queryset = queryset.filter(
#                     Q(projeto_assentamento__contrato=models.ProjetoAssentamento.CONTRATO_18)
#                 )
#         return queryset


class LoteAdmin(nested_admin.NestedModelAdmin):
    def beneficiarios(self, obj):
        titular_conjuge = models.Membro.objects.only(
            'nome',
            'parentesco'
        ).filter(
            familia__lote_id=obj.pk,
            parentesco__in=(
                models.Membro.PARENTESCO_TITULAR, models.Membro.PARENTESCO_CONJUGE
            )
        ).order_by('parentesco')
        membros = []
        for membro in titular_conjuge:
            print(membro)
            membros.append('({}) {}'.format(membro.parentesco_choices[membro.parentesco], membro.nome))
        return mark_safe('''<br/>'''.join(membros))

    def get_data_homologacao(self, obj):
        if obj.data_homologacao:
            return date(obj.data_homologacao, 'd/m/Y')
        return '-'

    get_data_homologacao.admin_order_field = 'data_homologacao'
    get_data_homologacao.short_description = 'Data de Homologação'

    def get_ocupante_regular(self, obj):
        if obj.ocupante_irregular == models.Lote.CHOICE_SIM:
            return False
        return True

    get_ocupante_regular.boolean = True
    get_ocupante_regular.short_description = 'Ocupante Regular'
    get_ocupante_regular.admin_order_field = 'ocupante_irregular'

    beneficiarios.short_description = 'Nome do(s) Beneficiário(s)'
    beneficiarios.allow_tags = True

    def get_contrato(self, obj):
        return obj.projeto_assentamento.contrato

    get_contrato.short_description = 'Contrato'
    get_contrato.admin_order_field = 'projeto_assentamento__contrato'

    def get_projeto_assentamento(self, obj):
        return obj.projeto_assentamento

    get_projeto_assentamento.short_description = 'Projeto de Assentamento'
    get_projeto_assentamento.admin_order_field = 'projeto_assentamento'

    list_display = (
        'codigo_sipra', 'get_contrato', 'get_projeto_assentamento', 'beneficiarios', 'get_data_homologacao', 'numero', 'area', 'cad_unico', 'get_ocupante_regular'
    )

    search_fields = ['codigo_sipra', 'numero']
    list_filter = [
        # ContratoListFilter,
        'projeto_assentamento', 'entrevistador', 'outra_familia_no_lote', 'cad_unico', 'ocupante_irregular',
        'recebe_beneficio_social', 'moradia_assentamento', 'tipo_parede_externa', 'tipo_instalacao_eletrica',
        'tipo_instalacao_sanitaria', 'localizacao_fonte_agua', 'abastecimento_agua_suficiente',
        'quantas_familias_utilizam_mesma_fonte_agua', 'agua_para_animais_plantio', 'regularidade_abastecimento_agua',
        'tipo_estrada_acesso', 'situacao_estrada_acesso', 'situacao_cercado_lote', 'area_preservacao_permanente',
        'area_preservacao_permanente_cercada', 'necessita_licenciamento_ambiental',
        'necessita_autoriacao_exploracao_florestal_queima_controlada', 'documentos', 'beneficios', 'etnias',
        'estruturas_organizativas', 'fontes_agua', 'tratamentos_agua', 'construcoes_lote', 'bens_produtivos',
        'aplicacoes_credito', 'creditos_bancarios'
    ]
    inlines = [
        FamiliaInlineAdmin, ContatoInlineAdmin, DocumentoLoteInlineAdmin, BeneficioSocialInlineAdmin,
        AutoDeclaracaoEtniaInlineAdmin, EstruturaOrganizativaInlineAdmin, FonteAguaInlineAdmin,
        TratamentoAguaInlineAdmin,
        ConstrucaoLoteInlineAdmin, BemProdutivoInlineAdmin, AplicacaoCreditoInlineAdmin, CreditoBancarioInlineAdmin,
        CulturaInlineAdmin, OlericulturaInlineAdmin, FruticulturaInlineAdmin, AtividadeExtrativistaInlineAdmin,
        ProducaoFlorestalInlineAdmin, BovinoculturaInlineAdmin, OutraCriacaoInlineAdmin,
        BovinoculturaLeiteiraInlineAdmin,
        BovinoculturaCorteInlineAdmin, OrigemAnimalInlineAdmin, NivelTecnologicoProducaoAnimalInlineAdmin,
        ProcessadoBeneficiadoInlineAdmin, ProblemaAmbientalInlineAdmin, PraticaConservacionistaInlineAdmin,
        LicenciamentoAmbientalInlineAdmin,
        AtendimentoSaudeInlineAdmin, ProgramaSaudeInlineAdmin, AtividadeFisicaInlineAdmin, EspacoDisponivelInlineAdmin,
        EstabelecimentoEnsinoInlineAdmin, NaoPossuiDocumentoInlineAdmin
    ]
    exclude = ['possui_capineira', 'necessita_licenciamento_ambiental', 'desativado_por', 'desativado_em']
    # change_form_template = 'admin/custom/change_form.html'

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }


admin.site.register(models.Contrato, ContratoAdmin)
admin.site.register(models.ProjetoAssentamento, ProjetoAssentamentoAdmin)
admin.site.register(models.Lote, LoteAdmin)
admin.site.disable_action('delete_selected')
