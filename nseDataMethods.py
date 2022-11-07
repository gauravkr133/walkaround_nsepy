from nsepy import get_history
import pandas as pd

import dateUtils
import filesUtils

niftyFiftyDataFrame = pd.read_csv('ind_nifty50list.csv')


def getallniftyfiftycompanies():
    return niftyFiftyDataFrame.to_json(orient='records', index=True, indent=2)


def getCompanyDetails(companysymbol):
    companydataframe = niftyFiftyDataFrame[niftyFiftyDataFrame["Symbol"] == companysymbol]
    return companydataframe.to_json(orient='records', index=True, indent=2)


def writeStocksDataToCsv(startDate, endDate):
    for i in range(0, 50):
        stockSymbol = niftyFiftyDataFrame.iloc[i]["Symbol"]
        stockData = get_history(symbol=stockSymbol, start=dateUtils.getDate(startDate), end=dateUtils.getDate(endDate))
        openEqualHighData = stockData[stockData["Open"] == stockData["High"]]
        openEqualLowData = stockData[stockData["Open"] == stockData["Low"]]
        filesUtils.writeToTextFile("openEqualHigh", openEqualHighData)
        filesUtils.writeToTextFile("openEqualLow", openEqualLowData)
        filesUtils.writeOhlcToCsv(stockSymbol, stockData)
    return "Data saved successfully..."


def writeSingleStockDataToCsv(companysymbol, startDate, endDate):
    stockData = get_history(symbol=companysymbol, start=dateUtils.getDate(startDate), end=dateUtils.getDate(endDate))
    filesUtils.writeOhlcToCsv(companysymbol, stockData)
    return "Data saved successfully..."


def getHistoryDataOfCompany(companysymbol, startDate, endDate):
    stockData = get_history(symbol=companysymbol, start=dateUtils.getDate(startDate), end=dateUtils.getDate(endDate))
    return stockData.reset_index().to_json(orient='records', indent=2, index=True, date_format='iso')


def getOpenEqualHighList():
    openEqualHighDataframe = pd.read_csv('txt/openEqualHigh.txt')
    return openEqualHighDataframe.to_json(orient='records', indent=2)


def getOpenEqualHigh(companysymbol, startDate, endDate):
    stockData = get_history(symbol=companysymbol, start=dateUtils.getDate(startDate), end=dateUtils.getDate(endDate))
    openEqualHighData = stockData[stockData["Open"] == stockData["High"]]
    return openEqualHighData.reset_index().to_json(orient='records', indent=2, index=True, date_format='iso')


def getOpenEqualLowList():
    openEqualLowDataframe = pd.read_csv('txt/openEqualLow.txt')
    return openEqualLowDataframe.to_json(orient='records', indent=2)


def getOpenEqualLow(companysymbol, startDate, endDate):
    stockData = get_history(symbol=companysymbol, start=dateUtils.getDate(startDate), end=dateUtils.getDate(endDate))
    openEqualLowData = stockData[stockData["Open"] == stockData["Low"]]
    return openEqualLowData.reset_index().to_json(orient='records', indent=2, index=True, date_format='iso')
