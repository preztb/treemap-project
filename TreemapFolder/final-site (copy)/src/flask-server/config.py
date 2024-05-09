API_KEY=open("api.txt").read()

import config as cfg
from eodhd import APIClient
import json
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

sector = ['Consumer Defensive', 'Financial Services',
          'Healthcare', 'Industrials', 'Technology', 'Basic Materials',
           'Energy',  'Communication Services', 'Consumer Cyclical',
           'Utilities', 'Real Estate']



#download stocks from market
@app.route(f"/api/downloads", methods=['GET'])
def allStocks():
    api = APIClient(cfg.API_KEY)

    df_symbols = api.get_exchange_symbols('US')
    df_symbols = df_symbols[df_symbols["Exchange"] == "NASDAQ"]
    df_symbols = df_symbols[df_symbols["Type"] == "Common Stock"]
    df_symbols = df_symbols[['Code']] + '.US'

    tickers = df_symbols['Code'].tolist()
    #prints list of symbols

    results = []
    for ticker in tickers:
        print(f"Prcoessing : {ticker}")
        json_data = api.get_fundamentals_data(ticker)

        result = {}
        result['Ticker'] = ticker
        result['Sector'] = json_data['General']['Sector']
        result['MarketCapitalization'] = json_data['Highlights']['MarketCapitalization']
        print(result)

        results.append(result)
        print('Length: ', len(results))

    with open('data.json', 'w') as file:
        json.dump(results, file, indent=4)

    df = pd.DataFrame(results)
    df.to_csv('data.csv', index=False)
    print(df)


    
    


#read datafile and create top 10 stocks for selected division
def readCSV(sector):

    df = pd.read_csv("data.csv")
    df_technology = df[df["Sector"] == sector]
    df_technology = df_technology.dropna(subset=["MarketCapitalization"])
    df_technology["MarketCapitalization"] = df_technology["MarketCapitalization"]

    df_technology_top10 = df_technology.nlargest(10, 'MarketCapitalization')
    df_technology_top10["Percentage"] = (df_technology_top10[
        "MarketCapitalization"] /
          (df_technology_top10["MarketCapitalization"].sum()) * 100).round(5)
    

    df_technology_top10.drop(columns=['Sector', 'MarketCapitalization'], inplace=True)
    df_technology_top10.rename(columns={"Ticker": "name", "Percentage": "value"}, inplace=True)
    df_technology_top10["children"] = None
    print(df_technology_top10)

    df_technology_top10.to_csv("content/technology_top10.csv", index=False)
    with open("content/technology_top10.json", "w") as file:
       df_technology_top10.to_json(file, orient="records")
    
    return jsonify({
    'Sector': sector})

   
#technology
@app.route(f"/api/{sector[4]}", methods=['GET'])
def selectSectorT():
    readCSV(sector[4])

#energy
@app.route(f"/api/{sector[6]}", methods=['GET'])
def selectSectorE():
    readCSV(sector[6])

#real estate
@app.route(f"/api/{sector[10]}", methods=['GET'])
def selectSectorR():
    readCSV(sector[10])

#consumer defensive
@app.route(f"/api/{sector[0]}", methods=['GET'])
def selectSectorCD():
    readCSV(sector[0])

#finance
@app.route(f"/api/{sector[1]}", methods=['GET'])
def selectSectorF():
    readCSV(sector[1])  

#healthcare
@app.route(f"/api/{sector[2]}", methods=['GET'])
def selectSectorH():
    readCSV(sector[2])  

#industrials
@app.route(f"/api/{sector[3]}", methods=['GET'])
def selectSectorI():
    readCSV(sector[3])

#basic materials
@app.route(f"/api/{sector[5]}", methods=['GET'])
def selectSectorB():
    readCSV(sector[5])

#communication service
@app.route(f"/api/{sector[7]}", methods=['GET'])
def selectSectorCS():
    readCSV(sector[7])

#consumer cyclical
@app.route(f"/api/{sector[8]}", methods=['GET'])
def selectSectorCC():
    readCSV(sector[8])

#utlities
@app.route(f"/api/{sector[9]}", methods=['GET'])
def selectSectorU():
    readCSV(sector[9])





    







#return data from technology sector

    



def start_flask_server():
    app.run(debug=True, port=8080)







    



if __name__ == '__main__':

    
    start_flask_server()
    


    

