from twitter_api import TwitterAPI
import pandas as pd
import csv

df = pd.read_csv('Data/Tweet.csv')

# Count the number of unique writers
writers = df['writer'].unique().tolist()

# Print the result
print('Number of unique writers:', len(writers))

# test api
# twitter = TwitterAPI()
# follower_counts = twitter.get_follower_counts(["VisualStockRSRC", "OpenAI"])
# print(follower_counts)  # Output: [4166, 385495]


twitter = TwitterAPI()

# Initialize a CSV file to write the results
with open('Data/follower_counts.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['writer', 'follower_count'])

# for i in range(0, len(writers), 100):
#     batch = writers[i:i+100]
#     follower_counts = twitter.get_follower_counts(batch)

#     # Write the results to the CSV file
#     with open('Data/follower_counts.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         for j in range(100):
#             writer.writerow([writers[i+j], follower_counts[j]])


batch_size = 100
for i in range(0, len(writers), batch_size):
    batch = writers[i:i+batch_size]
    # print("bactch", len(batch))
    follower_counts = twitter.get_follower_counts(batch)
    # print(len(follower_counts))
    # Write the results to the CSV file
    with open('Data/follower_counts.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for username, follower_count in follower_counts.items():
            writer.writerow([username, follower_count])