API_KEY=open('api.txt').read()

import config as cfg
from eodhd import APIClient
import json
import pandas as pd



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



def readCSV():

    df = pd.read_csv("data.csv")
    df_technology = df[df["Sector"] == "Technology"]
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
    with open("TreemapFolder/final-site/src/assets/technology_top10.json", "w") as file:
       df_technology_top10.to_json(file, orient="records")


    

def main():
    readCSV()



if __name__ == '__main__':
    main()

