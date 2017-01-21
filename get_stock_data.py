if __name__ == '__main__':
    (code, from_date, to_date) = get_arguments()
    hist_price = fetch_historical_price(code, from_date, to_date)
    print_historical_price(hist_price)
