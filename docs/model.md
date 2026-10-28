# Modelo dimensional

## Tabelas
- `dim_date`: Date (PK), Year, MonthNumber, MonthName, YearMonth, Quarter.
- `dim_customer`: CustomerID (PK), CustomerName, Segment, Region.
- `dim_product`: ProductID (PK), ProductName, Category, StandardCost, ListPrice.
- `dim_seller`: SellerID (PK), SellerName, Team.
- `fact_sales`: OrderID (PK), Date, CustomerID, ProductID, SellerID, Quantity, UnitPrice, UnitCost, DiscountPct, Status.
- `fact_targets`: Year (PK), RevenueTarget.

## Relacionamentos (1:*)
- dim_date[Date] → fact_sales[Date]
- dim_customer[CustomerID] → fact_sales[CustomerID]
- dim_product[ProductID] → fact_sales[ProductID]
- dim_seller[SellerID] → fact_sales[SellerID]

Todos os relacionamentos são **single-direction** (dimensão → fato), ativos, com cardinalidade 1:*.

### Metas anuais — cuidado com granularidade
`fact_targets` está no grão **ano**, não dia. Para que filtros de ano funcionem sem relacionamentos muitos-para-muitos, crie `dim_year` como tabela DAX:

```dax
dim_year = DISTINCT(SELECTCOLUMNS(dim_date, "Year", dim_date[Year]))
```

Relacione `dim_year[Year]` (1) a `dim_date[Year]` (*) e `fact_targets[Year]` (*), direção única. Use **dim_year[Year]** no segmentador de ano. Para filtrar meses, use dim_date. O valor da meta é anual: em recortes mensais, não deve ser interpretado como meta mensal.

## Tipos
Date = Date; IDs e Year = Whole Number; Quantity = Whole Number; UnitPrice e UnitCost = Decimal Number; DiscountPct = Decimal Number (fração de 0 a 1). Marque dim_date como Date table.

## Regras
Receita e custo são reconhecidos somente para pedidos Completed. Desconto reduz receita, não custo. Metas são valores fictícios anuais. Não existe receita realizada de pedidos Cancelled.
