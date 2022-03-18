import os
import pandas as pd

#input file folder
input_path = os. getcwd() +'\\input\\'
full_file = 'training.1600000.processed.noemoticon.csv'
#output file folder
output_path = os. getcwd() +'\\outputs\\'
file = 'selected_tweets.csv'

#save the training exemples
if os.path.exists(output_path + file) is False:
    
    #read the file
    colnames = ['polarity', 'id', 'post_datetime', 'query', 'user', 'tweet']
    df_tweets = pd.read_csv(input_path + full_file,
                            encoding='UTF', names=colnames, encoding_errors='ignore')

    # get the 1600 tweets
    tweets = df_tweets[['polarity','tweet']].sample(n=1600, random_state=0)

    #save to a csv file
    tweets.to_csv(output_path + file, index=False)
else:
    #load the source file
    tweets = pd.read_csv(output_path + file, sep=',')
