import image_scraper  #image_scraper.scrape_images(URL)










url = str(input("URL="))
lang=str(input('lang='))

tagval=len(url.split("/"))
image_scraper.scrape_images(url) -s ./raw/