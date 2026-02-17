# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
total_payment = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

overshoot = 0.0

while principal > 0:
    if total_months >= extra_payment_start_month and total_months < extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    old_principal = principal
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment



    total_months += 1
    print(f"{total_months} {total_paid:0.2f} {principal:0.2f}" )
        
    if principal < 0:
        overshoot = abs(old_principal - total_payment)
        print(f"{total_months} overpaid by {overshoot}")
print(f"Total Paid: {total_paid:0.2f} Total_Months: {total_months}")
