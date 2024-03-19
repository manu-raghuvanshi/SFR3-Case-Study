# SFR3 Case Study

## Technology Used
- Python
- Pandas library for data analysis
- Matplotlib library for visualization

## Project Structure
- **generateData/**: contains Python code to generate random data in csv files. Three datasets are being generated:
  - Tenant Information: `generateTenantData.py` is generating tenant information and storing it in a csv file called `tenantInformation.csv`. Someone is categorized as a tenant if they are living in one of SFR3 properties and paying rent.
  - Rent Information: `generateRentData.py` is generating rent history information of a tenant and storing it in a csv file called `rentInformation.csv`.
  - Applicant Information: `generateApplicantData.py` is generating applicant information and storing it in a csv file called `applicantInformation.csv`. Someone is categorized as an applicant if they have applied for a lease for one of SFR3 properties.
<br></br>
- `data_dictionary.json`: Json file that contains the name of datasets and their corresponding columns with its meanings.
<br></br>
- `sfr3.ipynb`: Python code that includes
  - Data loading e.g.: Tenant, Rent, and Applicant
  - Data cleansing
  - Data transformation
  - Data Visualization
  - Analytics summary of data analysis