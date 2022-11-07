from flask import Flask
import nseDataMethods

app = Flask(__name__)


@app.route('/getcompany')
def getallniftyfiftycompanies():
    return nseDataMethods.getallniftyfiftycompanies()


@app.route('/getcompany/<companysymbol>')
def getCompanyDetails(companysymbol):
    return nseDataMethods.getCompanyDetails(companysymbol)


@app.route('/writestockdatatocsv/<startdate>/<enddate>')
def writeAllStocksDataToCsv(startdate, enddate):
    return nseDataMethods.writeStocksDataToCsv(startdate, enddate)


@app.route('/writestockdatatocsv/<companysymbol>/<startdate>/<enddate>')
def writeSingleStockDataToCsv(companysymbol, startdate, enddate):
    return nseDataMethods.writeSingleStockDataToCsv(companysymbol, startdate, enddate)


@app.route('/gethistorydata/<companysymbol>/<startdate>/<enddate>')
def getHistoryDataOfCompany(companysymbol, startdate, enddate):
    return nseDataMethods.getHistoryDataOfCompany(companysymbol, startdate, enddate)


@app.route('/getopenequalhigh')
def getOpenEqualHighList():
    return nseDataMethods.getOpenEqualHighList()


@app.route('/getopenequalhigh/<companysymbol>/<startdate>/<enddate>')
def getSingleOpenEqualHigh(companysymbol, startdate, enddate):
    return nseDataMethods.getOpenEqualHigh(companysymbol, startdate, enddate)


@app.route('/getopenequallow')
def getOpenEqualLowList():
    return nseDataMethods.getOpenEqualLowList()


@app.route('/getopenequallow/<companysymbol>/<startdate>/<enddate>')
def getSingleOpenEqualLow(companysymbol, startdate, enddate):
    return nseDataMethods.getOpenEqualLow(companysymbol, startdate, enddate)


if __name__ == '__main__':
    app.run(debug=True)
