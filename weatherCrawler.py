# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
targetUrl1 = 'http://www.kma.go.kr/weather/forecast/timeseries.jsp?searchType=INTEREST&wideCode=1100000000&cityCode=1129000000&dongCode=1129055500'

def fetch(targetUrl):
    URL = targetUrl
    res = urllib.urlopen(URL)
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extractProbability(soup):
    extract = str(soup.find('table', class_='forecastNew3'))
    finding(extract,"PD_non",'\"','\"', 14, 35)
    finding(extract,"강수확률(%)", '\">', '<', 0, 100)
    '''
    tex = extract.find("강수확률(%)")
    Data = extract[tex:]
    num = Data.find('\">')
    num2 = Data[num+1:].find("</")
    print "데이터:"+Data[num+2:num+num2+1]
    '''
def extractTemperature(soup):
    extract = str(soup.find('dd', class_='now_weather1_right temp1 MB10'))
    finding(extract,"MB10", '>', '<', 4, 14)

def finding(text, findString, f1, f2, n1, n2):
    
    tex = text.find(findString)
    Data =text[tex+n1:tex+n2]
    num = Data.find(f1)
    num2 = Data[num+1:].find(f2)
    print "데이터:"+Data[num+1:num+num2+1].strip('>')

extractProbability(fetch(targetUrl1))

extractTemperature(fetch(targetUrl1))


    
