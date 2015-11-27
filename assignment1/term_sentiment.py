import sys, re, string
from collections import defaultdict
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def scr(text, scores):
    # split on spaces
    text = text.split(" ")

    # remove punctuation, lowercase.
    text =  [re.sub(r'[\W+]','', word).lower() for word in text]

    # remove empty strings
    text = filter(len, text)

    sent = 0
    for word in text:
        try:
            sent += scores[word]
        except KeyError:
            sent += 0
    return text,sent


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    tweets = []
    for line in tweet_file:
        fullTweet = json.loads(line)
        try:
            tweets.append(fullTweet["text"])
        except KeyError:
            tweets.append("")

    tweetScores = []
    for tweet in tweets:
        # print(tweet)
        tweetScores.append(scr(tweet, scores))

    newSents = []
    for tweet in tweetScores:
        score=tweet[1]
        for word in tweet[0]:
            newSents.append([word,score])

    res = defaultdict(list)
    for v, k in newSents: res[v].append(k)

    resList = []
    for key, value in res.iteritems():
        temp = [key,value]
        resList.append(temp)

    results = []
    for word, sentList in resList:
        results.append([word, sum(sentList)/float(len(sentList))])

    for word, sent in results:
        print("%s %s") % (word, sent )

if __name__ == '__main__':
    main()
