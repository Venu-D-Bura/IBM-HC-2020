from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import redirect

import tweepy
from textblob import TextBlob
import  numpy as np
import pandas as pd
import re
import pandas as pd

Positive=0
Negative=0
Neutral=0



# Create your views here.  



def homepage(request):
    return render(request,"home.html")



def search(request):
    return render(request,'search.html')



    
def result(request):
    hash = request.POST.get('hashtag')
    
    global Positive,Neutral,Negative

    consumer_key='Jxm97G9XLjso76EesqMjO98MO'
    consumer_secret='xMlZQgZYJQUII28h7ce4HEuJP0BmTdp2nDqUVHi9P626EppAw4'

    access_token='1101020537663426561-Nu3GBN3lED8lZoLEBGLZDOXrAWu3iu'
    access_token_secret='ulU94cQ4FfH3foUgynjgHmd7qkG1Yr4kYMhqbdtpadFNr'

    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    search_word=hash #Search topic

    api=tweepy.API(auth,wait_on_rate_limit=True)
    #date_since='2020-7-15'  # date
    
    #public_tweets=tweepy.Cursor(api.search,q=search_word,lang='en',WOEID_LOOKUP_URL=2282863).items(100000)
    public_tweets=tweepy.Cursor(api.search,q=search_word,lang='en',WOEID_LOOKUP_URL=2282863).items(400)
    
    tweet_details=[[tweet.text,tweet.user.location,tweet.created_at] for tweet in public_tweets]
    df=pd.DataFrame(data=tweet_details,columns=['Tweets','Location','Time'])
    df['Tweets']=df['Tweets'].apply(cleanText)
    l=len(df.index)
    #print(df.head(l-1))
    #Agree=(Positive/l)*100
    #Disagree=(Negative/l)*100
    #Both=(Neutral/l)*100
    
    #print('Agree:',round(Agree,2),"%")
    #print('Disagree:',round(Disagree,2),"%")
    #print('Neutral:',round(Both,2),"%")

    #print('Positive ',Positive)
    #print('Negative ',Negative)
    #print('Neutral ',Neutral)



    #df=['2020-7-15 1212','2020-7-14 1212','2020-7-14 1212','2020-7-13 1212','2020-7-12 1212','2020-7-12 1212''2020-7-11 1212','2020-7-11 1212']
    var_dates={}
    for i in df['Time']:
        x=str(i).split(' ')
        #x=i.split(' ')
        
        
        #print(df['Time'][0],"     ",type(x),"    ",x[0])
        try:
            var_dates[x[0]] += 1
        except:
            var_dates[x[0]] = 1
        
    #print(var_dates)
    '''
    
    var_dates={'2020-5-15':5,'2020-5-14':3,'2020-5-13':5}
    #print("------")
    #print(hash)
    #print(Positive,"  ",Negative,"  ",Neutral)
    #print(var_dates)
    #print("------")
    #for i in var_dates:
        #print(i,"   ",var_dates[i])
    #return HttpResponse('hi')
    '''
    return render(request,'show.html',{'hashtag':hash,'positive':Positive,'negative':Negative,'neutral':Neutral,'data':var_dates})
    









def about(request):
    return render(request,"about.html")


def cleanText(text):
    global Positive,Neutral,Negative
    text=re.sub(r'RT @[\w]*:',"",text)
    text = re.sub('#', '', text)
    text=re.sub(r'@[\w]*',"",text)
    text=re.sub(r'https?://[A-Za-z0-9./]*','',text)
    text=re.sub('\n','',text)
    tb= TextBlob(text)
    if(tb.sentiment.polarity>0):
        Positive+=1
    elif(tb.sentiment.polarity<0):
        Negative+=1
    else:
        Neutral+=1

    #print(str(i) + ". " + text)
    return text