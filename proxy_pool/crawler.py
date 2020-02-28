import json

from pyquery import PyQuery as pq

from .util import get_page


class ProxyMetaclass(type):
    def __new__(cls,name,bases,attrs):
        count=0
        attrs['__CrawlFunc__']=[]
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count+=1
        attrs['__CrawlFuncCount__']=count
        return type.__new__(cls,name,bases,attrs)

class Crawler(object,metaclass=ProxyMetaclass):
    def get_proxies(self,callback):
        proxies=[]
        for proxy in eval("self.{}()".format(callback)):
            print('Succeded getting the proxy : ',proxy)
            proxies.append(proxy)
        return proxies

    # Func should be named like "crawl_..."
    def crawl_daili66(self,page_count=10):
        """
        Get the proxy from www.66ip.cn
        """
        print('Start the crawler.......')
        start_url='http://www.66ip.cn/{}.html'
        urls=[start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('Crawling: ',url)
            html=get_page(url,encoding='gb2312')
            
            if html:
                doc=pq(html)
                trs=doc('.container div div:first-child table tr:gt(0)').items()
                for tr in trs:
                    ip=tr.find('td:nth-child(1)').text()
                    port=tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip,port])



    
    
