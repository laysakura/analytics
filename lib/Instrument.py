class Instrument:
    def __init__(self, code):
        self._code = code

    def get_historical_price(self, from_date, to_date):
        html = self._get_html(from_date, to_date)
        # hist_price = parse_html(html)
        # return hist_price

    def get_fundamentals(self, from_date, to_date):
        # TODO future
        pass

    def _get_html(self, from_date, to_date):
        url = self._get_url(from_date, to_date)
        print(url)
        # TODO get html from url

    def _get_url(self, from_date, to_date):
        (sy, _sm, _sd) = from_date.split('-')
        (ey, _em, _ed) = to_date.split('-')

        sm = _sm if _sm[0] != '0' else _sm[1]
        sd = _sd if _sm[0] != '0' else _sd[1]

        em = _em if _em[0] != '0' else _em[1]
        ed = _ed if _em[0] != '0' else _ed[1]

        url = 'http://info.finance.yahoo.co.jp/history/?code=%s.T&sy=%s&sm=%s&sd=%s&ey=%s&em=%s&ed=%s&tm=d' % (self._code, sy, sm, sd, ey, em, ed)
        return url

