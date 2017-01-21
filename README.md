# analytics

## get_stock_data

### example
```bash
python get_stock_data.py '7203' '2017-01-01' '2017-01-21'

code        date        open        close       high       low
7203        2017-01-01  6000        6500        6600       5900
7203        2017-01-02  6000        6500        6600       5900
...
```

### input
- 証券コード
- 開始日
- 終了日

### output
- 指定した証券コードについての開始日から終了日の終値情報
    - データフレーム形式

### internal logic
- Yahooファイナンスをスクレイピング
