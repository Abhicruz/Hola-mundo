# Import required libraries
import PyPDF2
import numpy
import os
import fitz

import re
import string
import pandas as pd
# Initializie score counters for each area
#HR = 0
#operations = 0
#supplychain = 0
#project = 0
#data = 0
#healthcare = 0
# Create an empty list where the scores will be stored
scores = []
terms2=[[0,0,0,0,0,0],['HR','operations magagement','supply chain','project management','data analytics','health care']]

# Create dictionary with industrial and system engineering key terms by area
terms = {'HR':['collective agreement','benefits and compensation','performane mangement','job analyis','training and development','fishbone',
                              'payroll administration', 'industrial releation','contract negotiation','risk management','collective agreement','conflict negoiation','lean','metrics'
                            ,'performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm','warden','extreme'],      
        'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                 'machinery','maintenance','manufacture','line balancing','oee','operations',
                                 'operations research','optimization','overall equipment effectiveness',
                                 'pfmea','process','process mapping','production','resources','safety',
                                 'stoppage','value stream mapping','utilization'],
        'Supply chain':['abc analysis','apics','conjunction','customer','customs','delivery','distribution','eoq','epq',
                        'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                        'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                        'third party logistics','transport','transportation','traffic',
                        'vendor','warehouse','wip','work in progress',],
        'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','schedule','scrum','stakeholders'],
        'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','bootstrap','internet','machine learning','modeling','basic in c','nosql','nlp',
                          'predictive','programming','python','sql','tableau','computer skills','text mining',
                          'visualuzation','html','css',],
        'Healthcare':['adverse events','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system','cluster']}
# Initializie score counters for each area

path = 'resume'
file=os.listdir(path)
print(file)
for filename in file:
    fo=os.path.join(path,filename )
    print("fo",fo)
    doc = fitz.open(fo)
    page=doc.pageCount
    print("total page:",page)
    count=0
    
    while count<page:
        page1=doc.loadPage(count)
        text=page1.getText()
        text=text.lower()
        count+=1
       # print(text)
        
    
    

# Obtain the scores for each area
    for area in terms.keys():
        if area == 'HR':
            for word in terms[area]:
                if word in text:
                    scores.append(word)
                    
            
                    terms2[0][0]+=1
        
        elif area == 'Operations management':
            for word in terms[area]:
                if word in text:
                    scores.append(word)
                    
                    
                           #operations +=1
                           #scores.append(operations)
                    terms2[0][1]+=1
        
        elif area == 'Supply chain':
            for word in terms[area]:
                if word in text:
                    scores.append(word)
                    
                    
                    
                           #supplychain +=1
                           #scores.append(supplychain)
                    terms2[0][2]+=1
        
        elif area == 'Project management':
            for word in terms[area]:
                 if word in text:
                     scores.append(word)
                     print(scores)
                     
                     
                           #project +=1
                           #scores.append(project)
                     terms2[0][3]+=1
        
        elif area == 'Data analytics':
            for word in terms[area]:
                 if word in text:
                     scores.append(word)
                     
                     
                     
                           #data +=1
                           #scores.append(data)
                     terms2[0][4]+=1
        
        else:
            for word in terms[area]:
                if word in text:
                    scores.append(word)
                    
                    #healthcare +=1
                           #scores.append(healthcare
                    terms2[0][5]+=1
                           

        
    print(scores)
    for i in range(0,6):
        print(terms2[1][i]," :",terms2[0][i])
        print("")
        
     
     

     
     
     

