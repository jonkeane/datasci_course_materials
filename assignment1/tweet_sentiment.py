import sys, re, string
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

    sent = 0
    for word in text:
        try:
            sent += scores[word]
        except KeyError:
            sent += 0
    return sent


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

    for tweet in tweets:
        # print(tweet)
        print(scr(tweet, scores))

if __name__ == '__main__':
    main()
