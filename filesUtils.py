import os.path


def writeOhlcToCsv(stockSymbol, stockData):
    columnList = ["Open", "High", "Low", "Close"]
    csvFilename = "csv/" + stockSymbol + ".csv"
    stockData[columnList].to_csv(csvFilename, encoding='utf-8')


def writeToTextFile(filename, stocksData):
    textFilename = "txt/" + filename + ".txt"
    if os.path.isfile(textFilename):
        stocksData.to_csv(textFilename, mode='a', index=True, header=False, encoding='utf-8')
    else:
        stocksData.to_csv(textFilename, encoding='utf-8')
