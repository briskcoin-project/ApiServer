import requests
def gen_p():
    response = requests.get("https://api.coinpaprika.com/v1/tickers/bkc-briskcoin", timeout=10)
    response.raise_for_status()
    data = response.json()
    gusd = round(float(data['quotes']['USD']['price']), 10)
    fname = "price.log"
    rtext = str(gusd)

    response2 = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin", timeout=10)
    response2.raise_for_status()
    data2 = response2.json()
    btc_price = float(data2['quotes']['USD']['price'])
    usd_amount = gusd
    btc_amount = usd_amount / btc_price
    formatted_btc_amount = f"{btc_amount:.10f}"
    
    if len(rtext) > 0:
        with open(fname, 'w') as file:
            file.write(rtext+","+formatted_btc_amount)
    else:
        print("Nothing to write — text is empty.")
        
if __name__ == "__main__":
    gen_p()