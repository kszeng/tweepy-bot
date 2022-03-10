import re, string, unicodedata
import random
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

def clean_and_tokenize(text):
    '''Takes a string and removes any unnecessary material,
    then tokenizes and returns tokens with their Part of Speech tags'''

    # clean and tokenize text
    text = text.replace("'", "")
    words = word_tokenize(re.sub(r"http\S+", "", text))

    # remove punctuation and stopwords
    new_words = []
    s = set(string.punctuation)
    s.add("''")
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '' and word not in stopwords.words('english'):
            new_words.append(word)

    # returm tagged tokens
    return nltk.pos_tag(new_words)

def create_corpus(texts):
    '''takes a list of texts, each a string, and created a corpus by mapping
    words to parts of speech tokens'''

    tag_pairs = []
    tagset = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
              'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$',
              'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG',
              'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB',]

    corpus = {key: set() for key in tagset}

    iter = 1
    for text in texts:
        tag_pairs = clean_and_tokenize(text)
        for pair in tag_pairs:
            corpus[pair[1]].add(pair[0])
        iter += 1

    return corpus

def generate_tweet(corpus):
    '''Generates and returns one headline formatted using catchy headline templates
    and words from the created corpus'''

    def p(pos):
        try:
            choice = random.choice(list(corpus[pos]))
        except:
            choice = ""
        else:
            choice = random.choice(list(corpus[pos]))

        return choice

    # so far, template sentences are hard-coded this way. would be good to get a cleaner sweep from real tweets
    templates = [f"Everyone's talking about {p('NNS')}, but what about {p('JJ')} {p('NNS')}?",
                 f"{p('NN')} is here and already {p('NNP')} has {p('VBN')} {p('NN')}. I don't know about this.",
                 f"{p('JJ')} {p('NN')} is on the rise. We all need to protect ourselves.",
                 f"{p('NN')}: The top {p('CD')} ways to prevent {p('JJR')} {p('NN')}. I don't buy it!",
                 f"Anyone else think {p('NN')} is the beginning of a {p('VBG')}?",
                 f"We're failing the {p('NNS')} . But {p('NNP')} can help save them. I'm looking at you, {p('NNP')}!",
                 f"{p('NNP')} is finally joining forces with {p('NNP')} to {p('VB')} the {p('NN')}, but what will happen to the {p('NNS')}??",
                 f"The {p('NN')} is {p('NNP')}. And that's not good news.",
                 f"The {p('NN')} is {p('NNP')}. And that's actually good news.",
                 f"As {p('RBR')} {p('NN')} increases, experts expect a rise in {p('NN')}. Always thought it was {p('JJ')} of {p('NNP')} to {p('VB')}.",
                 f"As {p('NN')} decreases, experts expect a decline in {p('NNP')}. Can we get a reading on {p('NNP')}'s opinion of this?'",
                 f"As {p('VBG')} increases, experts expect a devastating decline in {p('NNS')}. This is why {p('NNP')} should {p('VB')}!",
                 f"If {'NN'} is {p('VBG')}, experts say it might be because {p('NNP')} can't {p('VB')}. I, for one, am not {p('VBG')} when {p('NNS')} are everywhere.",
                 f"So this weekend I learned {p('CD')} ways {p('NNS')} can prevent a {p('JJ')} {p('NN')}...",
                 f"I'm not sure {p('NNS')} can {p('VB')} {p('NNS')}, but it's pretty obvious that {p('NNS')} can {p('VB')}.",
                 f"{p('NNP')} working with {p('NN')} is an attempt at {p('NN')}, but what does this mean for {p('NNS')} and {p('NNS')}?",
                 f"{p('NNP')} to {p('VB')} with {p('NNS')}. is it really possible?",
                 f"{p('NNS')} will never be {p('JJR')} than {p('NNS')}, in my opinion. But hey, if {p('NNP')} wants a {p('NN')}, more power to them.",
                 f"I don't care if {p('NN')} doesn't {p('VB')}. If {p('NNP')} is involved, then I want {p('NN')}.",
                 f"Whatever happens, the {p('NN')} to me will always be the best in {p('VBG')}.",
                 f"I used to think that {p('NN')} {p('VBD')} {p('NN')}, but ultimately it seems instead that {p('NN')} {p('VBZ')} {p('NN')}",
                 f"Anyone else also think that {p('NNS')} are {p('JJ')} and {p('NNS')} are {p('JJ')}? No? Just Me?",
                 f"Everyone seems to notice {p('NNS')} and their {p('NNS')}, but the only thing I wonder is how {p('NNS')} {p('VB')}...",
                 f"Honestly, the idea of {p('VBG')} {p('NN')} seems {p('JJ')} to me, but maybe it's worth a shot?",
                 f"When will {p('NNP')} {p('VB')}??? It seems like {p('NNS')} are slow to {p('VB')}...",
                 f"Maybe the time has come for {p('NNS')} to start {p('VBG')}. I would've {p('VBN')} the {p('NN')} right away.",
                 f"Can we please just go back to when {p('NN')} was still {p('JJ')}?",
                 f"Maybe it's better that {p('NNS')} {p('VB')}? At least it's better than {p('NNS')} {p('VBG')}.",
                 f"{p('NN')} is only the beginning. I think {p('NN')} and {p('NN')} are probably going to follow.",
                 f"Can someone explain why the {p('NN')} isn't {p('JJ')} yet? I've been looking into {p('NNS')} but none of it makes sense!",
                 f"So the idea was to {p('VB')} {p('NNS')} and {p('VB')} {p('NNS')}? It can't be that simple.",
                 f"Imo, {p('NNP')} should {p('VB')} ASAP. Otherwise, {p('NN')} would be able to {p('VB')}...",
                 f"There's no way {p('NNP')} would actually {p('VB')} and then just {p('VB')}. Right??",
                 f"The last thing we need is {p('NNP')} {p('VBG')} when {p('NNS')} are {p('VBG')}.",
                 f"I'm not ready to believe {p('NNP')} rly {p('VBD')} {p('NNS')}. It's {p('JJ')}.",
                 f"Look, idk everything, but it's at least obvious that {p('NN')} should {p('VB')} so {p('NNP')} can finally {p('VB')}",
                 f"Maybe I'm being naive, but {p('NN')} doesn't seem to {p('VB')} at all. Maybe {p('NNP')} was right.",
                 f"{p('NNP')}'s idea to {p('VB')} {p('NN')} is too {p('JJ')} for me to grasp."]

    return random.choice(templates)
