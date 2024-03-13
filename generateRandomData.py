import csv
import random
from datetime import date, timedelta


# initialize list of first names, list of last names
first_name = []
last_name = []

# read the listOfNames.csv file and populate the list initialized above
with open("listOfNames.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        first_name.append(row[0])
        last_name.append(row[1])


# generate random data
for uuid in range(1, 20):
    tenant_name = random.choice(first_name) + " " + random.choice(last_name)
    rent_amount = random.randint(15, 40) * 50
    lease_start_date = date(
        2023,
        random.choice([month for month in range(1, 13)]),
        random.choice([day for day in range(1, 31)]),
    )
    lease_end_date = lease_start_date + timedelta(days=random.choice([30, 180, 365]))
    utility_amount = round(random.uniform(10, 200), 2)
    pet_amount = None
    if random.choice([True, False]):
        pet_amount = 10.00
    tenant_screening_score = random.randint(538, 850)
    # https://www.turbotenant.com/blog/what-is-a-tenant-screening-report/
    print(
        f"UUID - {uuid}, Name - {tenant_name}, Rent Amount - {rent_amount}, "
        f"Lease Start Date - {lease_start_date}, Lease End Date - {lease_end_date}, "
        f"Utility Amount - {utility_amount}, Pet Amount - {pet_amount}, Tenant Screening Score - {}"
    )
