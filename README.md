# Polars
Este repositorio lo hago con el objetivo de prácticar en el uso de polars y para optimizar tiempos eternos que se hacen en pandas



En el primer ejemplo hemos comparado 2 dataframes iguales 1 en pandas el otro en polars, la diferencia es más estética que no funcional.

DataFrame en Polars:
shape: (5, 4)
┌────────┬──────┬───────────┬─────────┐
│ nombre ┆ edad ┆ ciudad    ┆ salario │
│ ---    ┆ ---  ┆ ---       ┆ ---     │
│ str    ┆ i64  ┆ str       ┆ i64     │
╞════════╪══════╪═══════════╪═════════╡
│ Ana    ┆ 25   ┆ Madrid    ┆ 30000   │
│ Luis   ┆ 30   ┆ Barcelona ┆ 45000   │
│ María  ┆ 28   ┆ Madrid    ┆ 38000   │
│ Carlos ┆ 35   ┆ Valencia  ┆ 52000   │
│ Elena  ┆ 27   ┆ Barcelona ┆ 41000   │
└────────┴──────┴───────────┴─────────┘

DataFrame en Pandas:
   nombre  edad     ciudad  salario
0     Ana    25     Madrid    30000
1    Luis    30  Barcelona    45000
2   María    28     Madrid    38000
3  Carlos    35   Valencia    52000
4   Elena    27  Barcelona    41000
