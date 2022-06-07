from fileinput import close
from logging import exception
from playwright.sync_api import sync_playwright
import csv
import re


def property_url(context, url):
    try:
        property = {}
        company_name = ''
        address = ''
        phone = ''
        mail = ''
        website = ''
        services_text = []
        services_html = ''
        # with open('property_data.csv', 'w', newline='') as outcsv:
        #     writer = csv.writer(outcsv)
        #     writer.writerow(['Company Name', 'Address', 'Phone','Mail','Services Text','Services Html','PageUrl'])
        tab = context.new_page()
        tab.goto(url)
        property['url'] = url
        
        # tab.wait_for_timeout(2000)
        
        close_button = tab.query_selector('div.ccc-content--dark > button.ccc-link.ccc-tabbable ')
        if close_button:
            close_button.click()
            
        property_data = tab.query_selector('div.main-content > div.container > div.row > div.col-xs-12.col-md-6 > div.member-directory-detail > .details')

        company_selector = property_data.query_selector('h6')
        if company_selector:
            company_name =  company_selector.inner_text()   # save into csv later
            print('company_name : ',company_name)
            property['company_name'] = company_name
        
        p_tags = property_data.query_selector_all('p')

        try:
            website_selector = p_tags[1]
            if website_selector:
                website_link = website_selector.query_selector('a')
                if website_link:
                    website = website_link.get_attribute('href')
                    print('website :',website)
                    property['website'] = website
        except:
            website = ''
            print('website :',website)
            property['website'] = website
            
   
            
        details  = property_data.query_selector('p').inner_text()
        print('Details : ',details)
        
        if details:
            data = details.split("\n")
            print('Data : ',data)
            try:
                address = data[0]
                print('Address :',address)
                property['address'] = address
                
            except:
                address = ''
                print('Address :',address)
                property['address'] = address
            
            # try:
            #     if data[1][0].isdigit() and data[1][-1].isdigit():
            #         phone = data[1]
            #         print('phone :',phone)
            #         property['phone'] = phone
            #     else:        
            #         mail = data[1]
            #         print('mail :',mail)
            #         property['mail'] = mail
            # except Exception as e:
            #     mail = ''
            #     print('mail :',mail)
            #     property['mail'] = mail
            
            # try:
            #     phone = data[2]
            #     print('phone :',phone)
            #     property['phone'] = phone
            # except:
            #     phone = ''
            #     print('phone :',phone)
            #     property['phone'] = phone
            
            try:
                
                mail_data = data[1]
                result = re.findall('@',mail_data)
                
                if result:
                    property['mail'] = mail_data
                    print('mail :',mail_data)
                else:
                    if re.search("^\d", data[1][0]) and re.search("\d$", data[1][-1]) is not None:
                    # if data[1][0].isdigit() and data[1][-1].isdigit():
                        phone = data[1]
                        print('phone :',phone)
                        property['phone'] = phone
            except:
                mail = ''
                print('mail :',mail)
                property['mail'] = mail
                
            if len(data) >= 3:
                try:
                    phone = data[2]
                    print('phone :',phone)
                    property['phone'] = phone
                except:
                    phone = ''
                    print('phone :',phone)
                    property['phone'] = phone
            
                
        services_html_slector = tab.query_selector('div.main-content > div.container > div.row > div.col-xs-12.col-md-6 ')
        if services_html_slector:
            services_html = services_html_slector.inner_html()
            property['services_html'] = services_html
            
        property_data = tab.query_selector_all('div.main-content > div.container > div.row > div.col-xs-12.col-md-6 > div > .panel-body > ul > li')
        if property_data:
        # services_text_html
            
            for data in property_data:
                value = data.inner_text()
                if value:
                    services_text.append(value)
        property['services_text'] = services_text
                # if data[1]:
                #     mail = data[1]
                #     print('mail :',mail)
                # if data[2]:
                #     phone = data[2]
                #     print('phone :',phone)

        tab.close()
        print('<---------------------------------------------------------->')
        return property
    # mail_selector = property_data.query_selector('p > a')
    # if mail_selector:
    #     mail = mail_selector.get_attribute('href')
    except Exception as e:
        print("Error")
        

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=True)
    # page = browser.new_context()
    # page = browser.new_page()
    context = browser.new_context()
    # page = browser.new_page()
    page = context.new_page()
    page.goto("file:///C:/Users/GNG/Desktop/Projects/Scrape/propertymark.html", wait_until="domcontentloaded")
    
    li_data = page.query_selector_all('div.member-item > div.member-item-detail > h6.member-name')
    with open('property_data.csv', 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Company Name', 'Address', 'Phone','Mail','Website' ,'Services Text','Services Html','PageUrl'])

    url_list = []
    index = 0
    for data in li_data:
        
        url_selector = data.query_selector('a')
        if url_selector:
            url = url_selector.get_attribute('href')
            # print('url : ', url)
            # print('Name : ', url_selector.inner_text())

            if url in url_list:
                continue
            url_list.append(url)
            # page1 = context.new_page()
    
            # page1.goto(url)
            data =property_url(context, url)
            
            try:
                company_name = data['company_name']
            except:
                company_name = ''
                
            try:
                address = data['address']
            except:
                address = ''

            try:
                phone = data['phone']
            except:
                phone = ''

            try:
                mail = data['mail']
            except:
                mail = ''
            
            try:
                website = data['website']
            except:
                website = ''
            
            try:
                services_text = data['services_text']
            except:
                services_text = []
                
            try:
                services_html = data['services_html']
            except:
                services_html = ''
                
            try:
                page_url = data['url']
            except:
                page_url = ''
                
                
            with open('property_data.csv', 'a', newline='') as outcsv:
                writer = csv.writer(outcsv)
                writer.writerow([company_name, address, phone, mail,website , services_text, services_html, page_url])
        index = index + 1
        print('index : ',index)
            
    browser.close()