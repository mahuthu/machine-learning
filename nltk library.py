#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk


# In[27]:


from nltk.tokenize import sent_tokenize

stop_words = set(stopwords.words("english")+ [',', '.', '?'])
To remove the ", . ?"
tokenized_text = sent_tokenize(text)

# output
tokenized_text


# In[9]:


from nltk.tokenize import word_tokenize


# In[14]:


tokenized_word = word_tokenize(text_one)
tokenized_word


# In[12]:


import nltk
nltk.download("punkt")
#importing  nltk package not part of the code


# In[15]:


text_two = """Backgammon is one of the oldest known board games. 
Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. 
It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll
of two dice.
"""

tokenized_text_two = sent_tokenize(text_two)

tokenized_text_two


# In[16]:


for i in tokenized_text_two:
    print(i)


# In[17]:


from nltk.tokenize import word_tokenize

tokenized_word = word_tokenize(text_one)
tokenized_word


# In[18]:


from nltk.stem import PorterStemmer

ps = PorterStemmer()

word1 = "meeting"
word2 = "connecting"
word3 = "goes"
word4 = "registered"
word5 = "better"

stem_word1 = ps.stem(word1)
stem_word2 = ps.stem(word2)
stem_word3 = ps.stem(word3)
stem_word4 = ps.stem(word4)
stem_word5 = ps.stem(word5)


print(stem_word1)
print(stem_word2)
print(stem_word3)
print(stem_word4)
print(stem_word5)


# In[ ]:





# In[21]:


from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()


word1 = "flying"
word2 = "went"
word3 = "better"
word4 = "registered"


lem_word1 = lem.lemmatize(word1,"v") #wordnet v-verb
lem_word2 = lem.lemmatize(word2,"v")
lem_word3 = lem.lemmatize(word3,"a")
lem_word4 = lem.lemmatize(word4,"v")


print(lem_word1)
print(lem_word2)
print(lem_word3)
print(lem_word4)


# In[20]:


import nltk
nltk.download('wordnet')
#not part of the code


# In[24]:


import nltk
nltk.download("stopwords")


# In[25]:


from nltk.corpus import stopwords
print(stopwords.words("english"))


# In[26]:


stop_words = set(stopwords.words("english"))
sentence = "Backgammon is one of the oldest known board games."


words = nltk.word_tokenize(sentence)
without_stop_words = [word for word in words if not word in stop_words]
print(without_stop_words)


# In[29]:


sent2 = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""


# step 1
tk_sent2 = word_tokenize(sent2)


# step 2
tk_sent2_without_stopwords = [word for word in tk_sent2 if not word in stop_words]


tk_sent2_without_stopwords

# tk_sent2_without_stopwords


tk_sent2_without_punct = [ word for word in tk_sent2_without_stopwords if word.isalnum() ]
tk_sent2_without_punct


# In[31]:


import nltk
nltk.download('averaged_perceptron_tagger')


# In[32]:


sent = "Albert Einstein was born in Ulm, Germany in 1879."


tokens=nltk.word_tokenize(sent)
print(tokens)


nltk.pos_tag(tokens)


# In[ ]:




