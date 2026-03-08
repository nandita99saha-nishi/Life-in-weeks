age = input("what is your current age?")

age_as_int = int(age)

years_remaining = 60-age_as_int
days_remaining = years_remaining*365
weeks_remaining = days_remaining*52
months_remaining = weeks_remaining*12

message = f"you have {years_remaining} years,{days_remaining} days , {weeks_remaining } weeks, {months_remaining} months"

print(message)