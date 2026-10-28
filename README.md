# Power BI Executive Analytics

Projeto de portfólio para **BI Pleno/Sênior**: modelo dimensional, indicadores executivos, DAX e inteligência temporal, usando **dados 100% sintéticos**.

## Entregáveis disponíveis
- `scripts/generate_data.py`: gerador determinístico de 2.400 pedidos, 150 clientes, 16 produtos, 6 vendedores, calendário e metas anuais.
- `data/*.csv`: gerados ao executar o script (não requer pacotes externos).
- `dax/`: catálogo de medidas DAX (cada definição deve ser criada como medida separada).
- `docs/model.md`: modelo estrela, relacionamentos, tipos e regras de negócio.
- `docs/report_blueprint.md`: especificação de quatro páginas do relatório.
- `tests/`: validação automatizada dos dados com `unittest`.
- GitHub Actions: geração e validação automática.

## Executar gratuitamente
```bash
python scripts/generate_data.py
python -m unittest discover -s tests -v
```

No **Power BI Desktop**, importe os CSVs gerados, configure relacionamentos conforme `docs/model.md`, crie as medidas em `dax/` e monte as páginas de `docs/report_blueprint.md`.

> **Status:** base, DAX e especificação prontos. O relatório `.pbix` ainda precisa ser montado e validado no Power BI Desktop; não afirmamos que há um dashboard interativo publicado.

## Regras de negócio
- Receita reconhecida considera apenas pedidos **Completed**.
- Receita líquida = quantidade × preço × (1 − desconto).
- Lucro bruto = receita líquida − custo reconhecido.
- Metas são anuais, fictícias e não equivalem a metas mensais.
- Indicadores temporais usam calendário contínuo e exigem Date table.

## Custos e privacidade
Sem Supabase, banco hospedado, credenciais, dados de clientes reais ou dependências pagas. O Power BI Desktop é gratuito para desenvolvimento local; compartilhamento interativo pode exigir licença.
