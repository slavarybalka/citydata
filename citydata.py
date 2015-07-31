# http://www.city-data.com/zips/75024.html

import time
import urllib 
import urllib.request 
import re


super = ['http://www.city-data.com/zips/91316.html','http://www.city-data.com/zips/92021.html','http://www.city-data.com/zips/90210.html']

def graburlcontent(pageurl, *args): 
    opener = urllib.request.build_opener() 
    opener.addheaders = [('User-agent', 'Mozilla/5.0')] 
 
    try: 
        page = opener.open(pageurl) 
        x = page.read(*args) # number of bytes is optional
        #print(x)
        return x.decode('UTF-8')
        

    except: 
        print("some error occured in graburlcontent function")
        pass


def get_population(text): 
    population = re.findall("Estimated zip code population in 2013:</b>\s([\d,]+)<br>", text)

    return population

def get_population_density(text): 
    population_density = re.findall("Population density:</b>\s([\d,]+\s)<b>", text)
    
    return population_density

def get_males(text): 
    males = re.findall("<tr><td><b>Males:</b>\s([\d,]+)", text)
    
    return males

def get_females(text): 
    females = re.findall("<tr><td><b>Females:</b>\s([\d,]+)", text)
    
    return females

def get_median_age(text): 
    median_age = re.findall("Median\sresident\sage\:\<\/b\>\<table><tr><td><b>This\szip\scode\:\</b><\/td><td><p\sclass=\\'h\\'\sstyle=\\'padding-left:\d{3}px;\\'></p>([\d.]+)\syears", text)
    
    return median_age

def get_median_income(text): 
    median_income = re.findall("Estimated median household income in 2013:\s</b></b><table><tr><td><b>This zip code:</b></td><td><p\sclass=\\'h\\'\sstyle=\\'padding-left:\d{3}px;\\'></p>([$\d,]+)", text)
    
    return median_income


    

####################### Execution part #######################

for i in super:
    try:
        page_contents = graburlcontent(i)
        population = get_population(page_contents)
        population_density = get_population_density(page_contents)
        males = get_males(page_contents)
        females = get_females(page_contents)
        median_age = get_median_age(page_contents)
        median_income = get_median_income(page_contents)
        #print(page_contents)
        
        print('\n')
        print(i)
        print("Total population: %s" % (population[0]))
        print("Population density is: %s per square mile." % (population_density[0]))
        print("Males: %s" % (males[0]), format(float(males[0].replace(',',''))/float(population[0].replace(',',''))*100, '.1f'))
        print("Females: %s" % (females[0]), format(float(females[0].replace(',',''))/float(population[0].replace(',',''))*100, '.1f'))
        print("Median age at this zip code: %s" % (median_age[0]))
        print("Median income at this zip code: %s" % (median_income[0]))

        print('\n')

        #time.sleep(10)
    except:
        print("can't print for some reason, check the control flow")
        continue
