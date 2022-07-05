#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"what is your name",
        ["my name is electronica\nhow can i help?",]
            
    ],
    [
        r"i need a new phone",
        ["you can purchase any depending on your specifications\n ask me anything about any phone",]
        
    ],
    [
        r"what brands are available",
        ["we have various brands such as samsung, nokia, iphone, tecno, huawei",]
    ],
    [
         r"what are the specifications on samsung",
        ["5 inch display \n 24 mp front camera \n 30 mp rear camera \n 4gb ram \n fingerprint sensor",]
    ],
    [
        r"what is the price of samsung?",
        ["20000",]
        
    ],
    [
        r"what are the specifications of nokia?",
        ["6 inch display \n 20 mp front camera \n 24 mp rear camera \n 4gb ram \n fingerprint sensor",]
    ],
    [
        r"what is the price of nokia",
        ["15000",]
    ],
    [
        r"what are the specifications of iphone",
        ["5.5 inch display \n 12 mp front camera \n 16 mp rear camera \n 2gb ram \n fingerprint sensor",]
    ],
    [
        r"what is the price of iphone",
        ["30000",]
    ],
    ]
        
def  assistant():
 print("Hi,I sell mobile phones ;)\n how can i assist you.  ") 
 chat = Chat(pairs, reflections)
 chat.converse()
if __name__ == "__main__":
      assistant()
    


# In[ ]:





# In[ ]:




