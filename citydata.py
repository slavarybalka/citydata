# http://www.city-data.com/zips/75024.html


import time
import urllib 
import urllib.request 
import re


#zips = ['http://www.city-data.com/zips/92020.html','http://www.city-data.com/zips/90210.html','http://www.city-data.com/zips/91316.html','http://www.city-data.com/zips/75024.html']
zips = ['http://www.city-data.com/zips/92021.html']
zipsx = ["http://www.unitedstateszipcodes.org/92021/"]


####################### Setting the Stage (methods) #######################


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



#+====================> DEMOGRAPHIC <==================+


def get_population_by_age_group(text):
    xxx = text.split('<h3>Total Population by Age</h3>')
    
    males_by_age = [elem.replace('</td>','') for elem in xxx[1].split('</td></tr><tr><td>')[1].split('<td align=right>')[1:]]
    females_by_age = [elem.replace('</td>','').replace('</tr><tr><td>Total','') for elem in xxx[1].split('</td></tr><tr><td>Female')[1].split('<td align=right>')[1:19]]
    #print(males_by_age)
    #print(females_by_age)
    
    people = {"Males Under 5" : males_by_age[0]}

    print(people["Males Under 5"])
    
    return people



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

def get_never_married(text): 
    never_married = re.findall("Never married:</b>\s([\d.%]+)", text)
    
    return never_married

def get_married(text): 
    married = re.findall("Now married:</b>\s([\d.%]+)", text)
    
    return married

def get_separated(text): 
    separated = re.findall("Separated:</b>\s([\d.%]+)", text)
    
    return separated

def get_widowed(text): 
    widowed = re.findall("Widowed:</b>\s([\d.%]+)", text)
    
    return widowed

def get_divorced(text): 
    divorced = re.findall("Divorced:</b>\s([\d.%]+)", text)
    
    return divorced

def get_foreign_born(text):
    foreign_born = re.findall('Foreign born population:</b>\s([\d,]+)', text)

    return foreign_born

#+====================> EDUCATION <==================+

def get_high_school(text): 
    high_school = re.findall("High school or higher:</b>\s([\d.%]+)", text)
    
    return high_school

def get_bachelors(text): 
    bachelors = re.findall("Bachelor\\'s degree or higher:</b>\s([\d.%]+)", text)
    
    return bachelors

def get_professional_degree(text): 
    professional = re.findall("Graduate or professional degree:</b>\s([\d.%]+)", text)
    
    return professional

def get_private_schools(text): 
    private_schools = re.findall("elementary and middle school\)\:<\/b>\s[\d,]+<br>\\r\\n<div\sclass\=\\'hgraph\\'><table><tr><td><b>Here:<\/b><\/td><td><p class=\\\'h\\\'\sstyle=\\'padding-left:[\d,]+px;\\'><\/p>([\d\.%]+)", text)
    
    return private_schools


#+====================> EMPLOYMENT <==================+


def get_travel_time_to_work(text): 
    travel_time_to_work = re.findall("Mean travel time to work \(commute\)\:</b>\s([\d.]+)", text)
    
    return travel_time_to_work

def get_employment(text): 
    employment = re.findall("Unemployed:</b>\s([\d.%]+)", text)
    
    return employment

def get_median_income(text): 
    median_income = re.findall("Estimated median household income in 2013:\s</b></b><table><tr><td><b>This zip code:</b></td><td><p\sclass=\\'h\\'\sstyle=\\'padding-left:\d{3}px;\\'></p>([$\d,]+)", text)
       
    return median_income


 #+====================> HOUSING <==================+   

def get_median_rent(text): 
    median_rent = re.findall("Median gross rent in 2013:</b>\s([$\d,]+)", text)
       
    return median_rent

def get_house_value(text): 
    house_value = re.findall("Estimated median house or condo value in 2013:\s</b>([$\d,]+)", text)
       
    return house_value

def get_renters(text): 
    renters = re.findall("% of renters here:<\/b><\/td><td><p class=\\'h\\' style=\\'padding-left:\d+px;\\'><\/p>([\d.%]+)", text)
       
    return renters

    





####################### Execution part #######################
for i in zipsx:
    try:
        page_contents = graburlcontent(i)
        population_by_age = get_population_by_age_group(page_contents)
        print(i)
        print("Population by age group: %s" % (population_by_age))

    except:
        print("can't print for some reason, check the control flow in zips2")
        continue

for i in zips:
    try:
        page_contents = graburlcontent(i)
        population = get_population(page_contents)
        
        population_density = get_population_density(page_contents)
        males = get_males(page_contents)
        females = get_females(page_contents)
        median_age = get_median_age(page_contents)
        never_married = get_never_married(page_contents)
        married = get_married(page_contents)
        separated = get_separated(page_contents)
        widowed = get_widowed(page_contents)
        divorced = get_divorced(page_contents)
        foreign_born = get_foreign_born(page_contents)
        employment = get_employment(page_contents)
        median_income = get_median_income(page_contents)
        median_rent = get_median_rent(page_contents)
        house_value = get_house_value(page_contents)
        high_school = get_high_school(page_contents)
        bachelors = get_bachelors(page_contents)
        professional = get_professional_degree(page_contents)
        private_schools = get_private_schools(page_contents)
        travel_time_to_work = get_travel_time_to_work(page_contents)
        renters = get_renters(page_contents)



        #print(page_contents)
        
        print('\n')
        print(i)
        
        print('\nDEMOGRAPHIC:\n')
        print("Population by age group: %s" % (population_by_age))
        print("Total population: %s" % (population[0]))
        print("Population density is: %s per square mile." % (population_density[0]))
        print("Males: %s" % (males[0]), '(' + format(float(males[0].replace(',',''))/float(population[0].replace(',',''))*100, '.1f') + '%)')
        print("Females: %s" % (females[0]), '(' + format(float(females[0].replace(',',''))/float(population[0].replace(',',''))*100, '.1f') + '%)')
        print("Median age: %s" % (median_age[0]))
        print("Never married: %s" % (never_married[0]))
        print("Married: %s" % (married[0]))
        print("Separated: %s" % (separated[0]))
        print("Widowed: %s" % (widowed[0]))
        print("Divorced: %s" % (divorced[0]))
        print("Foreign born: %s" % (foreign_born[0]))

        print('\nEDUCATION:\n')
        print("Completed high school: %s" % (high_school[0]))
        print("Have Bachelors degree: %s" % (bachelors[0]))
        print("Have Professional degree: %s" % (professional[0]))
        print("Students in private schools in grades 1 to 8: %s" % (private_schools[0]))

        print('\nWORK:\n')
        print("Travel time to work: %s" % (travel_time_to_work[0]) + ' minutes')
        print("Unemployed: %s" % (employment[0]))

        print('\nHOUSING:\n')
        print("Median income: %s" % (median_income[0]))
        print("Median rent:  %s" % '$' + str(int(int(median_rent[0].replace(',','').replace('$',''))*1.10)))
        print("House value:  %s" % '$' + str(int(int(house_value[0].replace(',','').replace('$',''))*1.30)))
        print("Renters: %s" % (renters[0]))

   
        print('\n')

        #time.sleep(10)
    except:
        print("can't print for some reason, check the control flow")
        continue