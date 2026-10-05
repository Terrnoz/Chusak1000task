import math

def compound_interest(principal, rate, years, n=12):
    return principal * (1 + rate / n) ** (n * years)

def loan_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)

print("Вклад 100000 под 10% на 5 лет:")
print(f"  С капитализацией: {compound_interest(100000, 0.10, 5):.2f}")

print("\nКредит 1000000 под 12% на 10 лет:")
payment = loan_payment(1000000, 0.12, 10)
print(f"  Ежемесячный платёж: {payment:.2f}")
print(f"  Общая выплата: {payment * 120:.2f}")