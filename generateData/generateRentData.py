import csv
import uuid
import random
from datetime import date, timedelta
import pandas as pd

month_map = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


tenant_info_df = pd.read_csv(
    filepath_or_buffer="tenantInformation.csv", index_col="UUID"
)
fill_na_values = {"Pet_Amount": 0.0}
tenant_info_df = tenant_info_df.fillna(value=fill_na_values)

rent_dataset = []

for row in tenant_info_df.itertuples():
    rent_row = []
    lease_start_date = date.fromisoformat(row.Lease_Start_Date)
    while lease_start_date < date.today():
        payment_id = uuid.uuid4()
        month_year = (
            month_map[lease_start_date.month] + "_" + str(lease_start_date.year)
        )
        total_rent_amount = row.Rent_Amount + row.Utility_Amount + row.Pet_Amount
        try:
            payment_date = date(
                year=lease_start_date.year,
                month=lease_start_date.month,
                day=random.randint(lease_start_date.day, 31),
            )
        except ValueError:
            payment_date = date(
                year=lease_start_date.year,
                month=lease_start_date.month,
                day=28,
            )
        late_payment = "Y" if payment_date.day > 27 else "N"
        rent_row.append(
            [
                payment_id,
                row.Index,
                row.Tenant_Name,
                month_year,
                payment_date,
                total_rent_amount,
                total_rent_amount,
                total_rent_amount - total_rent_amount,
                late_payment,
            ]
        )
        lease_start_date += timedelta(days=30)
    rent_dataset.extend(rent_row)
print(rent_dataset)
rent_info_df = pd.DataFrame(
    data=rent_dataset,
    columns=[
        "Payment_ID",
        "Tenant_UUID",
        "Tenant_Name",
        "Month_year",
        "Rent_Paid_Date",
        "Rent_Amount_Paid",
        "Total_Rent_Amount",
        "Rent_Amount_Due",
        "Late_Payment"
    ]
)
rent_info_df.to_csv(path_or_buf="rentInformation.csv", index=False)
