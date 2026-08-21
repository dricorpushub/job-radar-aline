"""Regras profissionais específicas da Aline."""

import pytest

from core.job import Job
from core.perfis import PERFIL_ALINE


def _vaga(titulo, local, modalidade):
    return Job(
        titulo=titulo,
        empresa="Empresa Teste",
        local=local,
        modalidade=modalidade,
        link=f"https://exemplo.com/{abs(hash((titulo, local, modalidade)))}",
        site="Teste",
    )


@pytest.mark.parametrize("titulo", [
    "Customer Success Manager Sênior",
    "Account Manager Pleno",
    "Gerente de Contas Estratégicas",
    "Gerente de Parceiros",
    "Customer Delivery Manager",
    "Consultora de Implantação ERP",
    "Consultora SAP SD",
    "Sales Operations Specialist",
])
def test_cargos_prioritarios_remotos_passam(titulo):
    assert _vaga(titulo, "Brazil", "Remoto").combina_com(PERFIL_ALINE.regras)


def test_hibrido_em_curitiba_passa():
    assert _vaga("Account Manager", "Curitiba - PR", "Híbrido").combina_com(PERFIL_ALINE.regras)


@pytest.mark.parametrize("modalidade", ["Presencial", ""])
def test_presencial_ou_modalidade_nao_informada_em_curitiba_nao_passa(modalidade):
    assert not _vaga("Account Manager", "Curitiba - PR", modalidade).combina_com(PERFIL_ALINE.regras)


def test_hibrido_fora_de_curitiba_nao_passa():
    assert not _vaga("Customer Success Manager", "São Paulo - SP", "Híbrido").combina_com(PERFIL_ALINE.regras)


@pytest.mark.parametrize("titulo", [
    "SDR", "BDR", "Executivo de Contas Hunter", "Vendedor Externo",
    "Representante Comercial", "Executivo Comercial New Business B2B",
])
def test_cargos_bloqueados_nao_passam(titulo):
    assert not _vaga(titulo, "Brazil", "Remoto").combina_com(PERFIL_ALINE.regras)


def test_senioridade_senior_pontua_acima_de_junior():
    senior = _vaga("Account Manager Sênior", "Brazil", "Remoto")
    junior = _vaga("Account Manager Júnior", "Brazil", "Remoto")
    assert senior.pontuar_relevancia(PERFIL_ALINE.regras) > junior.pontuar_relevancia(PERFIL_ALINE.regras)
