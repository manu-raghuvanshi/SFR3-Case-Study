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

house_plans = ["1BHK", "2BHK", "3BHK"]

# read the listOfNames.csv file and populate the list initialized above
with open("listOfNames.csv", newline="", encoding="utf-8-sig") as listOfNames:
    reader = csv.reader(listOfNames, delimiter=",")
    for row in reader:
        first_name.append(row[0])
        last_name.append(row[1])
listOfNames.close()

with open("applicantInformation.csv", "w", newline="") as applicantInformation:
    writer = csv.writer(applicantInformation)
    writer.writerow(
        [
            "Applicant_UUID",
            "Applicant_Name",
            "Rent_Amount",
            "Lease_Start_Date",
            "Lease_End_Date",
            "Applicant_Screening_Score",
            "House_Plan",
            "Counties",
            "Monthly_Income",
        ]
    )
    # generate random data
    for uuid in range(1, 201):
        applicant_uuid = "Applicant_" + str(uuid)
        applicant_name = random.choice(first_name) + " " + random.choice(last_name)
        rent_amount = random.randint(15, 40) * 50
        applicant_monthly_income = random.randint(15, 40) * 50 * random.randint(1, 10)
        try:
            lease_start_date = date(
                2023,
                random.choice([month for month in range(1, 13)]),
                random.choice([day for day in range(1, 31)]),
            )
        except ValueError:
            payment_date = date(
                year=lease_start_date.year,
                month=lease_start_date.month,
                day=28,
            )
        lease_end_date = lease_start_date + timedelta(
            days=random.choice([30, 180, 365])
        )
        applicant_screening_score = random.randint(350, 850)
        # https://www.turbotenant.com/blog/what-is-a-tenant-screening-report/
        applicant_house_plan = random.choice(house_plans)
        applicant_county = random.choice(counties)
        writer.writerow(
            [
                applicant_uuid,
                applicant_name,
                rent_amount,
                lease_start_date,
                lease_end_date,
                applicant_screening_score,
                applicant_house_plan,
                applicant_county,
                applicant_monthly_income,
            ]
        )

applicantInformation.close()
