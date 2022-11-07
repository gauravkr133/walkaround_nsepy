from flask import Flask
import nseDataMethods

app = Flask(__name__)


@app.route('/getcompany')
def getallniftyfiftycompanies():
    return app.response_class(
        response=nseDataMethods.getallniftyfiftycompanies(),
        status=200,
        mimetype='application/json'
    )


@app.route('/getcompany/<companysymbol>')
def getCompanyDetails(companysymbol):
    return app.response_class(
        response=nseDataMethods.getCompanyDetails(companysymbol),
        status=200,
        mimetype='application/json'
    )


@app.route('/writestockdatatocsv/<startdate>/<enddate>')
def writeAllStocksDataToCsv(startdate, enddate):
    return app.response_class(
        response=nseDataMethods.writeStocksDataToCsv(startdate, enddate),
        status=200,
        mimetype='application/json'
    )


@app.route('/writestockdatatocsv/<companysymbol>/<startdate>/<enddate>')
def writeSingleStockDataToCsv(companysymbol, startdate, enddate):
    return app.response_class(
        response=nseDataMethods.writeSingleStockDataToCsv(companysymbol, startdate, enddate),
        status=200,
        mimetype='application/json'
    )


@app.route('/gethistorydata/<companysymbol>/<startdate>/<enddate>')
def getHistoryDataOfCompany(companysymbol, startdate, enddate):
    return app.response_class(
        response=nseDataMethods.getHistoryDataOfCompany(companysymbol, startdate, enddate),
        status=200,
        mimetype='application/json'
    )


@app.route('/getopenequalhigh')
def getOpenEqualHighList():
    return app.response_class(
        response=nseDataMethods.getOpenEqualHighList(),
        status=200,
        mimetype='application/json'
    )


@app.route('/getopenequalhigh/<companysymbol>/<startdate>/<enddate>')
def getSingleOpenEqualHigh(companysymbol, startdate, enddate):
    return app.response_class(
        response=nseDataMethods.getOpenEqualHigh(companysymbol, startdate, enddate),
        status=200,
        mimetype='application/json'
    )


@app.route('/getopenequallow')
def getOpenEqualLowList():
    return app.response_class(
        response=nseDataMethods.getOpenEqualLowList(),
        status=200,
        mimetype='application/json'
    )


@app.route('/getopenequallow/<companysymbol>/<startdate>/<enddate>')
def getSingleOpenEqualLow(companysymbol, startdate, enddate):
    return app.response_class(
        response=nseDataMethods.getOpenEqualLow(companysymbol, startdate, enddate),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
