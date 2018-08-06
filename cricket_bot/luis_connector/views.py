from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

luis_url="https://api.projectoxford.ai/luis/v2.0/apps/810ba923-69e0-4749-8c72-d31e68b777e2?subscription-key=5b5c7845848840efaa69ef66d3d838b2&verbose=true"
@api_view(['GET'])
def luis(request):
    
    user_input = request.GET.get('q', '')
    #print
    params = {"q" : user_input}
    r = requests.get(luis_url, params = params)
    luis_response = r.json()
    print(luis_response)
    
    manual_dict={"standard" : "Law 1", "players" : "Law 1", "substitutes" : "Law 2", "umpires" : "Law 3", "scorers" : "Law 4", "bat" : "Law 6", "pitch" : "Law 7", "wickets" : "Law 8" ,"crease" : "Law 9", "maintenance" : "Law 10", "Innings" : "Law 12", "follow-on" : "Law 13", "declaration" : "Law 14", "intervals" : "Law 15", "runs" : "Law 18", "boundaries" : "Law 19", "lost" : "Law 20", "over" : "Law 22", "dead" : "Law 23", "no" : "Law 24", "wide" : "Law 25", "bye" : "Law 26", "appeal" : "Law 27" }   
    filename="luis_connector/rules.txt"
    f=open(filename, "r")
    contents =f.read()
    #contents.lower()
    #print(contents)
    flag=0
    bot_output=""
    b=-1
    for entity in luis_response['entities']:
        entity=entity['entity']
        print(entity)
        if entity is not "ball":
            print("entered" + entity)
    
            if entity in manual_dict:
                flag=1
                
                a=manual_dict[entity]
                
                b=contents.find(a)
                
                print(b)
                s=contents[b:]
                b1=s.find("\n\n\n\n")
                print(b1)
                final=contents[b:b1+b]
                
                

            else:
                b=contents.find(entity)
                flag=1              
                print(b)
                s=contents[b:]
                b1=s.find("\n\n\n\n")
                print(b1)
                final=contents[b-25:b+25]
                
            bot_output=bot_output+final+"\n"
        
        #s=len(luis_response['query'].split(" "))
    if flag==1 and b == -1:
        print("please be specific")
        return Response("please be specific")
    else:
        print(bot_output)
        return Response(bot_output)
    s=len(luis_response['query'].split(" "))
    if flag==0 :
        b=contents.find(luis_response['query'])
        print(b)
        s=contents[b:]
        s=contents[b-200:b+200]
        if(b==-1):
            print("dosent match")
            return Response("dosent match")
            
        else:
            print(s)
            return Response(s)
            #return Response(s)
