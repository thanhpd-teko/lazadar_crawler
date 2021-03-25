# -*- coding: utf-8 -*-
import scrapy
import json
from fake_useragent import UserAgent
import sys

class LazSpider(scrapy.Spider):
    name = 'laz'
    allowed_domains = ['www.lazada.vn']
    ua = UserAgent()
    page = 1
    def start_requests(self):
        yield scrapy.Request(url=f'https://www.lazada.vn/xe-ghe-em-be/?ajax=true&page={self.page}&spm=a2o4n.10441748.cate_5.5.58f6567fCOXo3z',
                             callback=self.parse,
                             meta = {
                                 'dont_redirect': True,
                             },
                             headers={
                                 'User-Agent' : self.ua.random,
                                 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                 'accept-encoding' : 'gzip, deflate, br',
                                 'accept-language' : 'en-US,en;q=0.9',
                                 'cookie' : 'lzd_cid=1613fe47-a818-48a7-91f6-9317013af6cf; t_uid=1613fe47-a818-48a7-91f6-9317013af6cf; t_fv=1576163730864; hng=SG|en-SG|SGD|702; userLanguageML=en; cna=kUd5Fmh0qTcCASvxG4xEomnM; anon_uid=b2f2797c8977a345a31fade0e54a197b; _bl_uid=bIkea40R2hRvgm6h1vqObFCyneFd; cto_lwid=57821035-193a-457d-9202-18a20f6aafb7; _fbp=fb.1.1576163735263.218646330; _ga=GA1.2.403284105.1576163800; _gid=GA1.2.2128709850.1576163800; pdp_sfo=1; lzd_sid=10a0d4226a6eba30fc8fa351a1c09e1c; _tb_token_=e31e856e377e5; _m_h5_tk=c2b92a7a2fa48dbbfbb87296e3fe783e_1576221248093; _m_h5_tk_enc=c55b34df384dcd47a044d8550ed6f2f1; t_sid=YKfdSt3LvXpm1IJ5B0guWcThZP9D0iPs; utm_channel=NA; Hm_lvt_7cd4710f721b473263eed1f0840391b4=1576224224; Hm_lpvt_7cd4710f721b473263eed1f0840391b4=1576224224; JSESSIONID=E293E38C3B0F4135EFAE6E09224F64D0; l=dBTAP4FIqdGS98tCBOCwourza77tIIRASuPzaNbMi_5Zc6L6Rb_OkEbN6Fp6DAWf9-YB4HAa5Iy9-etlOj8fDLvkOJYXlxDc.; isg=BLGxbR7oSLN2x-SmWuAGRZ3ywD1LniUQXTeflZPGq3iXutEM2-7_4GOS3RZ5U71I'
                             },
                             dont_filter=True
                             )

    def parse(self, response):
        try:
            data = json.loads(response.body)
            for item in data.get('mods').get('listItems'):
                yield {
                    'NAME' : item.get('name'),
                    'productUrl' : item.get('productUrl'),
                    'imageUrl' : item.get('image'),
                    'originalPrice' : item.get('originalPrice'),
                    'DiscountedPrice' : item.get('price'),
                    'Discount' : item.get('discount'),
                    'ratingScore' : item.get('ratingScore'),
                    'review' : item.get('review'),
                    'description' : item.get('description'),
                    'categories' : item.get('categories'),
                    'itemId' : item.get('itemId'),
                    'page' : self.page
                }
        except TypeError:
            print("NO PAGE LEFT TO SCRAPE")
            sys.exit(0)
        except AttributeError:
            print("You are blocked on page number :",self.page)
            print("Press control + C to STOP or else continue.")
            print("Hint : uncomment PROXY_POOL and PROXY Download Middleware in settings.py")
        except Exception as e:
            print(e)
        self.page = self.page + 1
        yield scrapy.Request(url=f'https://www.lazada.vn/xe-ghe-em-be/?ajax=true&page={self.page}?spm=a2o4n.10441748.cate_5.5.58f6567fCOXo3z',
                             callback=self.parse,
                             meta = {
                                 'dont_redirect': True,
                             },
                             headers={
                                 'User-Agent' : self.ua.random,
                                 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                 'accept-encoding' : 'gzip, deflate, br',
                                 'accept-language' : 'en,vi;q=0.9',
                                 'cookie' : 'lzd_cid=1613fe47-a818-48a7-91f6-9317013af6cf; t_uid=1613fe47-a818-48a7-91f6-9317013af6cf; t_fv=1576163730864; hng=SG|en-SG|SGD|702; userLanguageML=en; cna=kUd5Fmh0qTcCASvxG4xEomnM; anon_uid=b2f2797c8977a345a31fade0e54a197b; _bl_uid=bIkea40R2hRvgm6h1vqObFCyneFd; cto_lwid=57821035-193a-457d-9202-18a20f6aafb7; _fbp=fb.1.1576163735263.218646330; _ga=GA1.2.403284105.1576163800; _gid=GA1.2.2128709850.1576163800; pdp_sfo=1; lzd_sid=10a0d4226a6eba30fc8fa351a1c09e1c; _tb_token_=e31e856e377e5; _m_h5_tk=c2b92a7a2fa48dbbfbb87296e3fe783e_1576221248093; _m_h5_tk_enc=c55b34df384dcd47a044d8550ed6f2f1; t_sid=YKfdSt3LvXpm1IJ5B0guWcThZP9D0iPs; utm_channel=NA; Hm_lvt_7cd4710f721b473263eed1f0840391b4=1576224224; Hm_lpvt_7cd4710f721b473263eed1f0840391b4=1576224224; JSESSIONID=E293E38C3B0F4135EFAE6E09224F64D0; l=dBTAP4FIqdGS98tCBOCwourza77tIIRASuPzaNbMi_5Zc6L6Rb_OkEbN6Fp6DAWf9-YB4HAa5Iy9-etlOj8fDLvkOJYXlxDc.; isg=BLGxbR7oSLN2x-SmWuAGRZ3ywD1LniUQXTeflZPGq3iXutEM2-7_4GOS3RZ5U71I'
                             },
                             dont_filter=True
                             )
