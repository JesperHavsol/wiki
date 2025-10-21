import wikipedia

def scrape(topic="Microsoft", sentences=1):
    res = wikipedia.summary(topic, sentences)
    return res