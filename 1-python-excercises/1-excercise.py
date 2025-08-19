
monthly_sales = {
    "Enero": [120000, 85000, 95000, 110000],
    "Febrero": [130000, 90000, 88000, 125000],
    "Marzo": [140000, 95000, 105000, 135000]
}


def sales_analisys(monthly_sales):


    total_sales = dict([
      ('Enero', sum(monthly_sales["Enero"])),
      ('Febrero', sum(monthly_sales["Febrero"])),
      ('Marzo', sum(monthly_sales["Marzo"])),
    ])

    print(total_sales)

    print("Mejor Mes : ",max(total_sales, key = total_sales.get ), max(total_sales.values()))

sales_analisys(monthly_sales)
