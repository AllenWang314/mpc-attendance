import pandas as pd

static_path = "static/"
csv_name = "poker_club_users.csv"
email_file_name = "emails.txt"
missing_accounts_file = "missing.txt"

# get only the columns you want from the csv file
df = pd.read_csv(static_path + csv_name)
result = df.to_dict()
emails_registered = result["Email"].values()
emails_registered_processed = [e.lower() for e in emails_registered if type(e) == str]

inFile = open(static_path + email_file_name, "r")
emails = inFile.readlines()
outFile = open(static_path + missing_accounts_file, "w")

emails_unregistered = []

for email in emails:
    if email[:-1].lower() not in emails_registered_processed:
        emails_unregistered.append(email[:-1].lower())

for email in emails_unregistered:
    outFile.write(email + "\n")

inFile.close()
outFile.close()
