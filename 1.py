from playwright.sync_api import sync_playwright
import csv
import re

e= 'rayabbeyvaluers.co.uk'

f = re.findall('@',e)

if f:
    print("thereee")
    
data = ['12','13','1233']

print(data[1])

# import re
# sample_str = "a107th version"
# # Check if String starts with a Number
# if re.search("^\d", sample_str) is not None:
#     print("The String '%s' starts with a number" % (sample_str))
# else:
#     print("The String '%s' does not starts with a number" % (sample_str))

import re
sample_str = "a107th version1"
# Check if String starts with a Number
if re.search("\d$", sample_str) and re.search("^\d", sample_str) is not None:
    print("The String '%s' starts with a number" % (sample_str))
else:
    print("The String '%s' does not starts with a number" % (sample_str))
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
    
#     page.goto('https://www.propertymark.co.uk/company/uk-property-pot-ltd-2.html')
    
#     # close_button = page.query_selector('div.ccc-content--dark > button.ccc-link.ccc-tabbable ')
#     # if close_button:
#     #     close_button.click()
#     Company_Name = ''
#     Address = ''
#     Phone = ''
#     Mail = ''
#     with open('property_data.csv', 'w', newline='') as outcsv:
#         writer = csv.writer(outcsv)
#         writer.writerow(['Company Name', 'Address', 'Phone','Mail','Services Text','Services Html'])
        
#     services_html = page.query_selector('div.main-content > div.container > div.row > div.col-xs-12.col-md-6 > div > .panel-body').inner_html()
#     property_data = page.query_selector_all('div.main-content > div.container > div.row > div.col-xs-12.col-md-6 > div > .panel-body > ul > li')
#     # services_text_html
#     services_text = []
#     for data in property_data:
#         value = data.inner_text()
#         if value:
#             services_text.append(value)
            
#     with open('property_data.csv', 'a', newline='') as outcsv:
#             writer = csv.writer(outcsv)
#             writer.writerow([Company_Name, Address, Phone, Mail, services_text, services_html])