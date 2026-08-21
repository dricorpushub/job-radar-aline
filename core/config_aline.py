"""Perfil profissional da Aline Canedo Vergineli.

Prioriza relacionamento e gestão de clientes em tecnologia, trabalho remoto
no Brasil e híbrido em Curitiba. Exclui funções de prospecção pura e trabalho
presencial integral sempre que o card informa a modalidade.
"""

KEYWORDS_CARGO_FORTE_ALINE = [
    "Customer Success Manager",
    "Gerente de Customer Success",
    "Gerente de Sucesso do Cliente",
    "Customer Success Specialist",
    "Especialista de Customer Success",
    "Especialista em Customer Success",
    "Analista de Customer Success",
    "Analista de Sucesso do Cliente",
    "Account Manager",
    "Gerente de Contas",
    "Executivo de Contas",
    "Executiva de Contas",
    "Key Account Manager",
    "Key Account",
    "Gerente de Contas Estratégicas",
    "Gerente de Parceiros",
    "Partner Success Manager",
    "Partner Account Manager",
    "Customer Experience Manager",
    "Gerente de Experiência do Cliente",
    "Customer Delivery Manager",
    "Consultor de Implantação",
    "Consultora de Implantação",
    "Implementation Consultant",
    "Onboarding Specialist",
    "Especialista de Onboarding",
    "Consultor de Negócios",
    "Consultora de Negócios",
    "Business Consultant",
    "Consultor ERP",
    "Consultora ERP",
    "Consultor SAP SD",
    "Consultora SAP SD",
    "SAP SD Consultant",
    "Sales Operations",
    "Sales Ops",
    "Sales Enablement",
    "Revenue Operations",
    "RevOps",
    "Gerente de Projetos",
    "Project Manager",
    "Coordenador de Projetos",
    "Coordenadora de Projetos",
]

# Estes títulos podem representar funções muito diferentes. Só entram quando
# o próprio título também traz um sinal do contexto desejado.
KEYWORDS_CARGO_AMBIGUO_ALINE = [
    "Business Analyst",
    "Analista de Negócios",
    "Executivo Comercial",
    "Executiva Comercial",
    "Executivo de Vendas",
    "Executiva de Vendas",
    "Inside Sales",
    "Consultor Comercial",
    "Consultora Comercial",
]

QUALIFICADORES_ALINE = [
    "customer",
    "cliente",
    "clientes",
    "conta",
    "contas",
    "parceiro",
    "parceiros",
    "b2b",
    "saas",
    "software",
    "tecnologia",
    "erp",
    "sap",
    "implantação",
    "onboarding",
    "pós-venda",
    "retenção",
]

FERRAMENTAS_TITULO_ALINE = ["SAP", "ERP"]
QUALIFICADORES_CARGO_ALINE = [
    "consultor", "consultora", "consultant", "analista", "analyst",
    "especialista", "specialist", "gerente", "manager",
]

TERMOS_BLOQUEADOS_TITULO_ALINE = [
    "SDR",
    "BDR",
    "Sales Development Representative",
    "Business Development Representative",
    "Hunter",
    "New Business",
    "Prospecção",
    "Prospector",
    "Vendedor Externo",
    "Vendedora Externa",
    "Representante Comercial",
    "Porta a Porta",
    "Door to Door",
    "Telemarketing",
]

CIDADES_ALINE = ["Remoto", "Curitiba"]
MODALIDADES_ACEITAS_ALINE = ["Remoto", "Híbrido"]
MERCADOS_REMOTO_ACEITOS_ALINE = ["Brasil"]

KEYWORDS_ALINE = KEYWORDS_CARGO_FORTE_ALINE + KEYWORDS_CARGO_AMBIGUO_ALINE
TERMOS_BUSCA_ALINE = sorted(set(k.lower() for k in KEYWORDS_ALINE))
TERMOS_PRIORITARIOS_ALINE = [
    "customer success manager",
    "account manager",
    "gerente de contas",
    "executivo de contas",
    "key account manager",
    "gerente de parceiros",
    "customer delivery manager",
    "consultor de implantação",
    "consultor de negócios",
    "sales operations",
    "sales enablement",
    "consultor sap sd",
]
TERMOS_POR_CICLO_ALINE = 12

LOCATIONS_LINKEDIN_ALINE = ["Brazil"]
LOCATIONS_LINKEDIN_REMOTO_APENAS_ALINE: list[str] = []
LOCATIONS_LINKEDIN_CIDADES_HIBRIDO_ALINE = ["Curitiba"]
