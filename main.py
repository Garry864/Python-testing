from datetime import date
import pandas as pd
from Automatic_Email_sender import send_email

# Public Google Sheet details
SHEET_ID = "1t7QRGlUj64_NovOxSa8odajaC-D7ISJcLff8k3nsVoA"
SHEET_NAME = "Sheet1"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

# print(load_df(CSV_URL))

def data_query_and_email(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject = f"[Coding is fun] Invoice: {row["invoice_no"]}",
                reciever_mail = row["email"],
                name = row["name"],
                due_date = row["due_date"].strftime("%d, %nb, %Y"), # example: 11, Aug 2022
                invoice_no= row["invoice_no"],
                amount = row["amount"]
            )
            email_counter += 1
    return f"Total Emails sent: {email_counter}"


if __name__ == "__main__":
    df = load_df(CSV_URL)
    result = data_query_and_email(df)
    print(result)




