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
            tweets.append(fullTweet["entities"]["hashtags"])
        except KeyError:
            continue

    tweets = filter(len, tweets)

    tweets = [hash['text'] for tweet in tweets for hash in tweet]

    res = defaultdict(list)
    for v in tweets: res[v].append(1)

    resList = []
    for key, value in res.iteritems():
        temp = [key,value]
        resList.append(temp)

    results = []
    for hash, counts in resList:
        results.append([hash, sum(counts)])

    hashCount = sum([word[1] for word in results])

    results = sorted(results, key=lambda hash: hash[1], reverse=True)

    for word, count in results[0:10]:
        # print("%s %s") % (word, count/float(hashCount) )
        print("%s %s") % (word, count )

if __name__ == '__main__':
    main()
