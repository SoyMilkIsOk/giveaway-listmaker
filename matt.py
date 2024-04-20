import pandas as pd
import re
import sys

if len(sys.argv) < 2:
  print("No input file supplied dummy")
  sys.exit(1)

unique_users = set()

csv_files = sys.argv[1:]

for file in csv_files:
  df = pd.read_csv(file)
  for username in df["username"]:
    if username not in unique_users:
      unique_users.add(username)
      print(re.sub("@", "", username.lower()))
