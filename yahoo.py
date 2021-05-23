#sklearn modules
from sklearn.preprocessing import LabelEncoder
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
#genral modules
import random, sys, os, time
import numpy as np
import pandas as pd
#web scrappiung modules
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
'''
find elements by id, name, className and other locator; last try path
'''

#determine purchase
#if highest - lowest > 0 price then buy (1); else do not buy (0)
def f(low,high):
    o_tmp = high - low
    # print(high, " - " , low , ' = ',o_tmp)

    if o_tmp > 1:
        return 1
    else:
        return 0
    # print(o_tmp, ' --> ', tmp)
    # return tmp

def data():
    #read scv data of operation
    data = pd.read_csv('AAPL.csv')
    #drop nan rows
    data = data.dropna()

    X = data[['Open','Low','Close']].values

    #convert x
    Le = LabelEncoder()
    for i in range(0,len(X[0])):
        X[:,i]= Le.fit_transform(X[:,i])
    # print(X)


    #convert y
    y = data.apply(lambda x: f(x.Open, x.High),axis=1)
    #predict highest value of the day
    # y = data[['High']]
    # print(y)

    #Create KNN model
    knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='distance')
    #separate train and test data
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    #train model
    knn.fit(X_train,y_train)

    #Test the model performance
    prediction = knn.predict(X_test)
    #compare model results to true results
    accuracy = metrics.accuracy_score(y_test,prediction)


    #print results
    # print('predictions:',prediction)
    print('accuracy:',accuracy)

    t= random.randint(0,len(y))
    print('actual value:',y[t])
    print('predicted value:', knn.predict([X[t]]))
    print('Open =', data['Open'][t])
    print('Close =', data['Close'][t])

def yahoo_indicators(driver,indicator):
    #NEED to add indicators manually to panel
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Indicators']"))).click()

    #click to add indicator to panel
    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/section/section/div[1]/div/div[1]/span[1]/div/div/div/div[3]/div[2]/ul[1]/li[5]/button").click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='%s']"%(indicator)))).click()

    #confirm values for RSI
    time.sleep(0.2)
    #save RSI value settings
    # driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/section/section/div[1]/div/div[1]/span[1]/div[2]/div/div/div[2]/button[1]").click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']"))).click()

    time.sleep(0.2)

#connect to yahoo finance
def yahoo_parse():
    #current directory
    path = os.getcwd()
    ticker = 'AAPL'
    #confirm current directory
    if os.path.exists(path):
        #driver full path
        path = path + '/chromedriver'
        #define selenium driver
        driver = webdriver.Chrome(executable_path=r'%s'%(path))
        #yahoo finance url for ticker
        url = "https://finance.yahoo.com/quote/%s?p=%s&guccounter=1"%(ticker,ticker)

        #fetch url html
        driver.get(url)
        time.sleep(3)

        #click on graph stock graph
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/canvas[2]").click()
        time.sleep(0.3)

        #add indicators to yahoo panel
        yahoo_indicators(driver,"RSI")
        yahoo_indicators(driver,"Williams %R")

        #fetch dynamic indicators values
        time.sleep(0.3)
        #gets to center now shift to the right side for current price

        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='RSI']"))).click()




        # #move by x,y offset
        # x = 200
        # y = 0
        # actions = ActionChains(driver)
        #
        # #reset mouse positon
        # actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
        # driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[2]/section/section/div[2]/div[12]/div").click()
        # #click edge of graph for current price
        # actions.move_by_offset(int(x), int(y)).click().perform()




        #try to save them so they can be used repeatedly for other stocks

        time.sleep(1000)

        driver.close()

    #invalid working path
    else:
    	print("No valid web browser driver found! :" + path)
    sys.exit()

#yahoo finance API
yahoo_parse()

#get price of stock during different intervals (1d, 5d, 1m, 6m )
#classify stoks from most purchasable to least

#get RSI value from yahoo - the last one reported
#below 20 {min value during the day & what was the last value}

#get Williams %R (5) - the last one repored
#below -80 {min value during the day & what was the last value}
