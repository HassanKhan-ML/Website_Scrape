from playwright.sync_api import sync_playwright


def property_page(page , url):
    
    pass

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    
    context = browser.new_context()
    
    # page = browser.new_page()
    page = context.new_page()
   

    page.goto("file:///C:/Users/GNG/Desktop/Projects/Scrape/propertymark.html" , wait_until = "domcontentloaded")
    
    
    # li_data = page.query_selector_all('ul.groups-members-list__results-list > li')
    li_data = page.query_selector_all('div.member-item > div.member-item-detail > .member-name')
    
    url_list = ['https://www.propertymark.co.uk/company/uk-property-pot-ltd-2.html']
    for data in li_data:
        
        property_url = data.query_selector('a')
        # print(property_url.inner_text())
        
        if property_url :
            url = property_url.get_attribute('href')
            if url in url_list:
                continue
            url_list.append(url)
            
            # property_page(page, url)
            
            # with page.context.expect_page() as tab:
            #     page.click("url")
            
            page_one = context.new_page()
            page_one.goto(url)
            
            page_one.close()
             
            # page1  = browser.new_page()

            # page1.goto(url)
            
            # page1.close()
                
            
            
            
            

            
        
            # print('url :',url)
            
    browser.close()