# Scrapy Lottery

This is a sample project that explores scrapy by developing a web crawler that scrapes information from the Brazilian lottery site. The base web site used was https://www.sorteonline.com.br/lotofacil/resultados and the crawler can be tweaked to collect all the lottery numbers, amount of winners and prize paided to each winner. It also can find the lottery date and place.

To run the crawler you just need to run:

``
scrapy crawl lotofacil -o data.json``

The application will collect all results and save them in a structured json file. It will contain a list of result objects like the one bellow:

```json
{
    "lottery_11_winners_cash": ["R$4,00"],
    "lottery_15_winners": ["4", ""], 
    "lottery_12_winners_cash": ["R$8,00"], 
    "lottery_14_winners_cash": ["R$1.613,43"], 
    "lottery_13_winners": ["23223"], 
    "lottery_13_winners_cash": ["R$20,00"], 
    "lottery_result_numbers": ["02", "03", "06", "08", "10", "12", "13", "16", "17", "18", "19", "20", "21", "22", "24"], 
    "lottery_12_winners": ["279085"], 
    "lottery_number": ["1625"], 
    "lottery_11_winners": ["1511596"], 
    "lottery_15_winners_cash": ["R$1.359.356,69"], 
    "lottery_14_winners": ["581"], 
    "lottery_date": ["16/02/2018", "Caminh\u00e3o da Sorte em VINHEDO, SP"]
}
```
