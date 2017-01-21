from lib import args
from lib import Instrument as inst


if __name__ == '__main__':
    (code, from_date, to_date) = args.get_arguments()

    instrument = inst.Instrument(code)
    instrument.get_historical_price(from_date, to_date)

    # print_historical_price(hist_price)
