from twitter_api import TwitterAPI
import pandas as pd
import csv
import time


df = pd.read_csv('Data/cleaned_Tweet.csv')

# Count the number of unique writers
writers = df['writer'].unique().tolist()

# Print the result
# print('Number of unique writers:', len(writers))
# with open('Data/follower_names.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for w in writers:
#         writer.writerow(f'{w}')
# test api
# twitter = TwitterAPI()
# follower_counts = twitter.get_follower_counts(["VisualStockRSRC", "OpenAI"])
# print(follower_counts)  # Output: [4166, 385495]

pass
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

    try:
        # Get the follower counts for the current batch of writers
        follower_counts = twitter.get_follower_counts(batch)

        # Write the results to the CSV file
        with open('Data/follower_counts.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for username, follower_count in follower_counts.items():
                writer.writerow([username, follower_count])

    except TwitterAPI.TwitterError as e:
        if e.status_code == 429: # TooManyRequests
            print("Too many requests. Waiting for 15 minutes...")
            time.sleep(900) # 15 minutes = 900 seconds
            continue # Try again after waiting
        else:
            raise e # Re-raise the exception if it's not a 429 error