from pytrends.request import TrendReq
import pandas as pd

pd.set_option("future.no_silent_downcasting", True)
pytrends = TrendReq(hl='en-US')

kw_list = []
listed=[]

n = int(input("Enter the number of words to be searched."))
for i in range(0,n):
    str = input()
    kw_list[i] = str  

def check_trends():
    pytrends.build_payload(listed, 
                       cat='0', 
                       timeframe='today 5-y', 
                       geo='', 
                       gprop='')

    data = pytrends.interest_over_time()
    mean = round(data.mean() , 2)
    # print(kw + ': ' + str(mean[kw]))
    avg = round(data[kw][-52:].mean() , 2)  #Last year avg
    avg2 = round(data[kw][:52].mean() , 2)  #Yearly avg of 5yrs ago
    trend = round(((avg/mean[kw])-1)*100 , 2)
    trend2 = round(((avg/avg2)-1)*100 , 2)
    print('The average 5 years interest of ' + kw + ' was ' + str(mean[kw]) + '.')
    print('The last year interest of ' + kw + ' compared to the last 5 years' + ' has changed by ' + str(trend) + '%')
    
    #Stable Trend
    if mean[kw] > 75 and abs(trend) <= 5:
        print('The interest for ' + kw + ' is stabel in the last five years.')
    elif mean[kw] >75 and trend > 5 :
        print("The interest for " + kw + ' is stable and increasing in the last 5 years.')
    elif mean[kw] >75 and trend < 5 :
        print("The interest for " + kw + ' is stable and decreasing in the last 5 years.')

    #Relatively Stable
    elif mean[kw] > 60 and abs(trend) <= 15:
        print('The interest for ' + kw + 'relatively stable in the last five years.')
    elif mean[kw] > 60 and abs(trend) > 15:
        print('The interest for ' + kw + 'relatively stable and increasing in the last five years.')

    #Seasonal
    elif mean[kw] > 20 and abs(trend) <=15:
        print("The interest for " + kw + ' is seasonal.')
    
    #New 
    elif mean[kw] > 20 and abs(trend) > 15:
        print("The interest for " + kw + ' is trending.')
    
    #Decreasing 
    elif mean[kw] > 20 and abs(trend) < -15:
        print("The interest for " + kw + ' is significantly decreasing.')

    #Cyclical
    elif mean[kw] > 5 and abs(trend) <=15:
        print('The interest for ' + kw + ' is cyclical.')

    #New
    elif mean[kw] > 0 and abs(trend) > 15:
        print('The interest for ' + kw + ' is new and trending.')
    
    #Declining
    elif mean[kw] > 0 and abs(trend) < -15:
        print('The interest for ' + kw + ' is declining and not comparable to its peak.')

    #Other
    else:
        print('This is something to be checked.')

    #Comparision
    if avg2 == 0:
        print('This doesn\'t exist five years ago.')
    elif trend2> 15:
        print('The last year interest is quite higher compared to five years ago.' + 'It has increased by ' + str(trend2) + '%')
    elif trend2< 15:
        print('The last year interest is quite lower compared to five years ago.' + 'It has decreased by ' + str(trend2) + '%')
    else:
        print('The last year is interest is comparable to five years ago' + 'It has changed by ' + str(trend2) + '%')

    print(' ')

for kw in kw_list:
    listed.append(kw)
    check_trends()
    listed.pop()
    