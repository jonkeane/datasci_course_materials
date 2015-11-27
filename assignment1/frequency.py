import sys, re, string
from collections import defaultdict
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def cleaner(text):
    # split on spaces
    text = text.split(" ")

    # remove punctuation, lowercase.
    text =  [re.sub(r'[\W+]','', word).lower() for word in text]

    # remove empty strings
    text = filter(len, text)

    return text


def main():
    tweet_file = open(sys.argv[1])

    tweets = []
    for line in tweet_file:
        fullTweet = json.loads(line)
        try:
            tweets.append(fullTweet["text"])
        except KeyError:
            tweets.append("")

    tweetWords = []
    for tweet in tweets:
        # print(tweet)
        [tweetWords.append(word) for word in cleaner(tweet)]


    res = defaultdict(list)
    for v in tweetWords: res[v].append(1)

    resList = []
    for key, value in res.iteritems():
        temp = [key,value]
        resList.append(temp)

    results = []
    for word, counts in resList:
        results.append([word, sum(counts)])

    wordCount = sum([word[1] for word in results])

    for word, count in results:
        print("%s %s") % (word, count/float(wordCount) )

if __name__ == '__main__':
    main()
