💊 MedManager CLI
Projeto acadêmico para gestão simplificada de horários de medicamentos.

Link do Deploy (Aplicação rodando em nuvem): https://replit.com/@marlosgamer/med-manager

Versão: 1.0.0 (Semantic Versioning)

Autor: Marlos Fagundes

📝 Problema Real
Muitos idosos ou cuidadores têm dificuldade em organizar o ciclo de horários de medicamentos de uso contínuo, o que pode levar ao esquecimento ou doses em duplicidade, comprometendo o tratamento de doenças crônicas.

🚀 Proposta da Solução
O MedManager é uma ferramenta CLI que permite registrar o horário da primeira dose e o intervalo (em horas), calculando automaticamente os horários das próximas tomadas para o ciclo de 24h.

🛠️ Tecnologias
Linguagem: Python 3.10+

QA/Linting: Ruff (Análise estática)

Testes: Pytest

CI/CD: GitHub Actions

## 👥 Equipe (Trabalho Final)
Membro 1 - Marlos Miguel Resende Fagundes 22505518
Membro 2 - Igor Amon Guimaraes Do Nascimento 22507334
Membro 3 - Caua Vinicius Venturell de Carvalho Goncalves Meneses 22511362



☁️ Banco de Dados
A aplicação agora é persistente! Utilizamos o Supabase (PostgreSQL) como Database as a Service (DBaaS). As operações de Read e Create estão implementadas de forma isolada na camada lógica da CLI.
