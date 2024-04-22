from tasks import crawl_enterprise

if __name__ == '__main__':
    enterprise_urls = [
        'https://ranking.glassdollar.com/graphql'
        # Add more URLs as needed
    ]

    # Define your query
    query = '''
          {
            topRankedCorporates
            {
                name,
                description,
                logo_url,
                industry,
                hq_city,
                hq_country,
                website_url,
                linkedin_url,
                twitter_url,
                startup_partners_count,
                startup_partners
                  {
                    company_name,
                    logo,
                    city,
                    country,
                    website,
                    theme_gd
                  }
              }
          }
    '''  

    # Submit tasks for crawling enterprises
    for url in enterprise_urls:
        crawl_enterprise.delay(url, query)