# http://www.city-data.com/zips/75024.html

import time
import urllib 
import urllib.request 
import re


super = ['http://www.city-data.com/zips/75024.html']

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
    print(population_density)
    return population_density
'''
def get_males(text): 
    males = re.findall("/<tr><td><b>Males:</b>\s([\d,]+)&nbsp/g", text)

    return males
    
'''




####################### Execution part #######################

for i in super:
    try:
        page_contents = graburlcontent(i)
        population = get_population(page_contents)
        population_density = get_population_density(page_contents)
        males = get_males(page_contents)
        print(i, '\t', population[0], population_density[0], 'test')
        print(population_density)
        #time.sleep(10)
    except:
        print(i)
        continue