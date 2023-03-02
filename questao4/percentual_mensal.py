monthly_revenue_percentage = [
    {"state": "SP", "value": 67836.43},
    {"state": "RJ", "value": 36678.66},
    {"state": "MG", "value": 29229.88},
    {"state": "ES", "value": 27165.48},
    {"state": "Outros", "value": 19849.53},
]

total_revenue = 0
for revenue in monthly_revenue_percentage:
    total_revenue += revenue["value"]

print(f'Rendimento mensal total da empresa: R$ {total_revenue:_.2f}'.replace('.',',').replace('_', '.'))
print(f'\nA representação percentual por estado foi:\n')

percentage = 0
for revenue in monthly_revenue_percentage:
    percentage = (revenue["value"] / total_revenue) * 100
    percentage = round(percentage, 2)
    revenue.update({"percentage":percentage})
    
    print(f'{revenue["state"]}: R$ {revenue["value"]:_.2f} equivalente a {revenue["percentage"]}%'.replace('.',',').replace('_', '.'))