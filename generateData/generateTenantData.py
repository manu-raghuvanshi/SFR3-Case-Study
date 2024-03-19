import csv
import random
from datetime import date, timedelta


# initialize list of first names, list of last names, Counties in Georgia, House Plans
first_name = []
last_name = []
counties = [
    "Appling",
    "Atkinson",
    "Bacon",
    "Baker",
    "Calhoun",
    "Camden",
    "Candler",
    "Carroll",
    "Mitchell",
    "Monroe",
    "Montgomery",
    "Morgan",
    "Murray",
    "Pulaski",
    "Putnam",
    "Quitman",
    "Rabun",
    "Wheeler",
    "White",
    "Whitfield",
]

house_plans = [
    "1BHK", "2BHK", "3BHK"
]

# read the listOfNames.csv file and populate the list initialized above
with open(
    "generateData/listOfNames.csv", newline="", encoding="utf-8-sig"
) as listOfNames:
    reader = csv.reader(listOfNames, delimiter=",")
    for row in reader:
        first_name.append(row[0])
        last_name.append(row[1])
listOfNames.close()

with open("generateData/tenantInformation.csv", "w", newline="") as tenantInformation:
    writer = csv.writer(tenantInformation)
    writer.writerow(
        [
            "UUID",
            "Tenant_Name",
            "Rent_Amount",
            "Lease_Start_Date",
            "Lease_End_Date",
            "Utility_Amount",
            "Pet_Amount",
            "Tenant_Screening_Score",
            "House_Plan",
            "Counties"
        ]
    )
    # generate random data
    for uuid in range(1, 101):
        tenant_name = random.choice(first_name) + " " + random.choice(last_name)
        rent_amount = random.randint(15, 40) * 50
        lease_start_date = date(
            2023,
            random.choice([month for month in range(1, 13)]),
            random.choice([day for day in range(1, 31)]),
        )
        lease_end_date = lease_start_date + timedelta(
            days=random.choice([30, 180, 365])
        )
        utility_amount = round(random.uniform(10, 200), 2)
        pet_amount = None
        if random.choice([True, False]):
            pet_amount = 10.00
        tenant_screening_score = random.randint(538, 850)
        # https://www.turbotenant.com/blog/what-is-a-tenant-screening-report/
        tenant_house_plan = random.choice(house_plans)
        tenant_county = random.choice(counties)
        writer.writerow(
            [
                uuid,
                tenant_name,
                rent_amount,
                lease_start_date,
                lease_end_date,
                utility_amount,
                pet_amount,
                tenant_screening_score,
                tenant_house_plan,
                tenant_county
            ]
        )

tenantInformation.close()
