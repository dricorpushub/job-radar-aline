# JobRadar da Aline

Esta versão já vem configurada para procurar vagas compatíveis com o perfil
profissional de Aline Canedo Vergineli.

## O que entra

- Customer Success, gestão de contas, Key Account e parceiros;
- Customer Experience, Customer Delivery, onboarding e implantação;
- consultoria de negócios, ERP e SAP SD;
- Sales Operations, Sales Enablement, RevOps e projetos em tecnologia;
- trabalho remoto no Brasil;
- trabalho híbrido somente em Curitiba;
- níveis pleno, sênior, especialista e liderança recebem prioridade.

## O que é bloqueado

- SDR, BDR, Hunter e New Business;
- prospecção explícita no título;
- vendedor externo, representante comercial, porta a porta e telemarketing;
- modalidade presencial;
- híbrido fora de Curitiba.

O radar usa apenas as informações disponíveis no card da vaga. Quando a
descrição completa não é coletada, ele não consegue confirmar horário, trabalho
aos sábados, remuneração, intensidade de prospecção ou cultura. Esses pontos
continuam sendo uma conferência humana antes da candidatura.

## Ativação

1. Crie uma cópia deste repositório na sua conta do GitHub.
2. No Telegram, abra o perfil `@BotFather`, envie `/newbot` e guarde o token.
3. Envie uma mensagem para o bot criado e obtenha o seu Chat ID.
4. No GitHub, abra **Settings > Secrets and variables > Actions**.
5. Crie os secrets `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID`.
6. Abra **Actions > JobRadar > Run workflow** para testar.

O arquivo `.github/workflows/jobradar.yml` executa apenas o perfil `aline`, a
cada três horas. Vagas de alta relevância chegam imediatamente; as demais ficam
no resumo diário.

## Ajustes futuros

Os cargos e bloqueios ficam em `core/config_aline.py`. As regras do perfil ficam
em `core/perfis.py`, no objeto `PERFIL_ALINE`.
