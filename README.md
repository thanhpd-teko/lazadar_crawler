# lazada-scraper

Folked from https://github.com/talk2div/lazada-scraper

https://www.lazada.sg/ using scrapy

To scrape all the babies and toys section in lazada.sg using API :-

Go to laz.py and run the scrapper using 

scrapy crawl laz -o lazada_datasets.csv if you want in csv 

or 

scrapy crawl laz -o lazada_datasets.json if you want in json format

Once scraping done go to Lazada_API.txt file copy second url 
and replace with the one mentioned in the laz.py and run the crawler.

Similary, follow the steps for all the API URL.

Note : Replace URL in both the yield one for start request and another for pagination.
