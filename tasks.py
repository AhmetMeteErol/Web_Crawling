from celery import Celery
import crawl_data # defined function to get data

app = Celery('glassdollar', broker='redis://remote_host:6379/0')

@app.task
def crawl_enterprise(enterprise_url, query):
    # Crawl enterprise data
    return crawl_data.fetch_corporates_data(enterprise_url, query)