#else if, en python es elif. es para dar una segunda condicion, y que la terminal me largue un solo resultado

ingreso_mensual = 5000
gasto_mensual = 8000

if ingreso_mensual > 10000:
    if gasto_mensual < 7000:
        print("ahora si estas bien en  cualquier parte del mundo")
    else:
        print("revisa los gastos")

elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")

else: 
    print("sos pobre")