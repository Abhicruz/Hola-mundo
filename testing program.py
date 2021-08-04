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
matched = []

# Create dictionary with industrial and system engineering key terms by area
terms = {'HR':['collective agreement','benefits and compensation','performane mangement','job analyis','training and development','fishbone',
                              'payroll administration', 'industrial releation','contract negotiation','risk management','collective agreement','conflict negoiation','lean','metrics'
                            ,'performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm','warden','expose'],      
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
                          'visualuzation','html','css','mobile app design'],
        'Healthcare':['adverse events','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system','cluster','gem tutor']}
# Initializie score counters for each area

path = 'resume'
file=os.listdir(path)
print(file)
for filename in file:
     fo=os.path.join(path,filename )
     print(fo)
 #open file
     pdfFileObj = open(fo,'rb')
# Read file
     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get total number of pages
     num_pages = pdfReader.numPages

# Initialize a count for the number of pages
     count = 0
     text = ""
     matched.clear()
     terms2=[[0,0,0,0,0,0],['HR','operations magagement','supply chain','project management','data analytics','health care']]

# Extract text from every page on the file
     while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
# Convert all strings to lowercase
        text = text.lower()
    
    
    

# Obtain the count for each area
     for area in terms.keys():
         if area == 'HR':
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                    
            
                     terms2[0][0]+=1
        
         elif area == 'Operations management':
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                     
                     terms2[0][1]+=1
        
         elif area == 'Supply chain':
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                     
                     terms2[0][2]+=1
        
         elif area == 'Project management':
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                     
                     terms2[0][3]+=1
        
         elif area == 'Data analytics':
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                     
                     terms2[0][4]+=1
        
         else:
             for word in terms[area]:
                 if word in text:
                     #matched.append(word)
                     
                     terms2[0][5]+=1
                           

        
     #print(matched)
     for i in range(0,6):
         print(terms2[1][i]," :",terms2[0][i])
         print("")
        
        
     
     

     
     
     

