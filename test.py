import re
import pandas as pd
import csv


df = pd.read_csv('Data/cleaned_Tweet.csv')

# Count the number of unique writers
writers = df['writer'].unique().tolist()

# Print the result
# with open('Data/follower_names.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for w in writers:
#         writer.writerow(f'{w}')

for s in writers:
    if not re.match('^[A-Za-z0-9_]{1,15}$', s):
        print(f"{s} does not match the pattern.")

print("done")