# Blueprint do relatório Power BI (16:9)

**Direção visual:** azul-marinho #0B1726, cards #162B40, verde-menta #61E5C4, texto #EFF6FC, alertas em coral discreto. Priorize hierarquia, contraste e poucos elementos decorativos.

## 1. Visão Executiva
Slicers: Ano (dim_year), Região, Segmento. KPIs: Receita Líquida, Lucro Bruto, Margem Bruta %, Pedidos Concluídos, Atingimento Meta %. Gráficos: linha Receita mensal e Receita Ano Anterior; barras Receita por Categoria; tabela Top 5 vendedores. Nota: meta é anual e não deve ser exibida como meta mensal sem regra de rateio.

## 2. Comercial
Slicers: Ano, Equipe, Região. Barras: Receita por vendedor, Receita por categoria; tabela: produto, pedidos, receita, lucro, margem, participação e ranking. Indicadores: Ticket Médio e Crescimento YoY %.

## 3. Clientes
Slicers: Ano, Região, Segmento. KPIs: Clientes Ativos, Clientes Recorrentes, Taxa Recorrência %. Gráficos: receita por segmento, clientes por região. Nota: recorrência é >=2 pedidos concluídos no período filtrado, não retenção de coorte.

## 4. Rentabilidade
KPIs: Lucro Bruto, Margem Bruta %, Variação Margem p.p. Barras: lucro por categoria, margem por produto; tabela: Receita, Custo, Lucro e Margem. Evite somar percentuais de margem.

## Validação antes da entrega
- Conferir relacionamento e direção de filtro; Date table marcada.
- Conferir total da receita líquida em 2024–2026 versus CSV de origem.
- Validar cancelamentos fora de receita e lucro.
- Validar filtro de Ano e metas com dim_year.
- Testar crescimento YoY em 2024 (deve ficar em branco).
- Revisar títulos, tooltips, estados sem dados e versão desktop.
