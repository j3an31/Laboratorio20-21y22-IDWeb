print("=" * 40)
print("CALCULADORA DE IMPUESTOS PROGRESIVOS")
print("=" * 40)
ingreso_mensual = float(input("Ingrese su ingreso mensual: "))
ingreso_anual = ingreso_mensual * 14
print(f"Ingreso anual calculado: {ingreso_anual:,.2f}")
print("\n" + "=" * 40)
print("CÁLCULO DE IMPUESTOS POR TRAMO")
print("=" * 40)

impuesto_total = 0
impuesto_tramo1 = 0
impuesto_tramo2 = 0
impuesto_tramo3 = 0
impuesto_tramo4 = 0

if ingreso_anual > 0:
    monto_gravado = min(ingreso_anual, 20000)
    impuesto_tramo1 = monto_gravado * 0.0
    print(f">>> Tramo 1 [0 - 20,000] al 0%:")
    print(f"Monto gravado: {monto_gravado:,.2f}")
    print(f"Impuesto: {impuesto_tramo1:,.2f}")

if ingreso_anual > 20000:
    monto_gravado = min(ingreso_anual - 20000, 30000)
    impuesto_tramo2 = monto_gravado * 0.10
    print(f">>> Tramo 2 <20,000 - 50,000] al 10%:")
    print(f"Monto gravado: {monto_gravado:,.2f}")
    print(f"Impuesto: {impuesto_tramo2:,.2f}")

if ingreso_anual > 50000:
    monto_gravado = min(ingreso_anual - 50000, 50000)
    impuesto_tramo3 = monto_gravado * 0.20
    print(f">>> Tramo 3 <50,000 - 100,000] al 20%:")
    print(f"Monto gravado: {monto_gravado:,.2f}")
    print(f"Impuesto: {impuesto_tramo3:,.2f}")

if ingreso_anual > 100000:
    monto_gravado = ingreso_anual - 100000
    impuesto_tramo4 = monto_gravado * 0.30
    print(f">>> Tramo 4 >100,000 al 30%:")
    print(f"Monto gravado: {monto_gravado:,.2f}")
    print(f"Impuesto: {impuesto_tramo4:,.2f}")

impuesto_total = impuesto_tramo1 + impuesto_tramo2 + impuesto_tramo3 + impuesto_tramo4
tasa_efectiva = (impuesto_total / ingreso_anual) * 100

print("\n" + "=" * 40)
print("RESUMEN")
print("=" * 40)
print(f"> Total de impuestos: {impuesto_total:,.2f}")
print(f"> Tasa efectiva real: {tasa_efectiva:.2f}%")
print(f"> Ingreso neto anual: {ingreso_anual - impuesto_total:,.2f}")