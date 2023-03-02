import json

def over_the_average_revenue(day_revenue:float, avg:float):
    if(day_revenue > avg):
        return True
    
    return False

json_file = open("dados.json")
monthly_revenue_data = json.load(json_file)

lower_revenue = {"dia": None, "valor": None}
higher_revenue = {"dia": None, "valor": None}
avg = number_of_days = 0

for data in monthly_revenue_data:
    value = data["valor"]

    if value == 0:
        continue

    if higher_revenue["valor"] == None or value > higher_revenue["valor"]:
        higher_revenue["dia"] = data["dia"]
        higher_revenue["valor"] = data["valor"]

    if lower_revenue["valor"] == None or value < lower_revenue["valor"]:
        lower_revenue["dia"] = data["dia"]
        lower_revenue["valor"] = data["valor"]

    number_of_days += 1
    avg += value

avg = avg/number_of_days

days_over_the_average = 0
for data in monthly_revenue_data:
    if(data['valor'] == 0):
        continue

    if(over_the_average_revenue):
        days_over_the_average += 1

print(f'Relatório Mensal:\nDia de menor faturamento: dia {lower_revenue["dia"]} com o valor de R$ {lower_revenue["valor"]:.2f}')
print(f'Dia de maior faturamento: dia {higher_revenue["dia"]} com o valor de R$ {higher_revenue["valor"]:.2f}')
print(f'Total de dias que o faturamento foi superior à média mensal: {days_over_the_average}')
json_file.close()
