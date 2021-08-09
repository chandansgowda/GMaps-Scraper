from selenium import webdriver
import pandas as pd
import xlsxwriter


class GoogleMapScraper:

    def __init__(self):
        self.PATH = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.business_list = []
        self.business_info = {}
        self.business_info["name"] = "NA"
        self.business_info["rating"] = "NA"
        self.business_info["reviews_count"] = "NA"
        self.business_info["address"] = "NA"
        self.business_info["contact"] = "NA"
        self.business_info["website"] = "NA"

    def get_business_info(self, url):
        self.driver.get(url)
        # Parse data out of the page
        self.business_info["name"] = self.driver.find_element_by_class_name("x3AX1-LfntMc-header-title-title").text
        self.business_info["rating"] = self.driver.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d").text
        self.business_info["reviews_count"] = self.driver.find_element_by_class_name("widget-pane-link").text
        self.business_info["address"] = self.driver.find_elements_by_class_name("QSFF4-text")[0].text
        self.business_info["contact"] = self.driver.find_elements_by_class_name("QSFF4-text")[1].text
        self.business_info["website"] = self.driver.find_elements_by_class_name("QSFF4-text")[2].text
        #add business info to business list
        self.business_list.append(self.business_info)

def create_xlsx_file (file_path: str, headers: dict, items: list):
    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        worksheet.write_row(row=0, col=0, data=headers.values())
        header_keys = list(headers.keys())
        for index, item in enumerate(items):
            row = map(lambda field_id: item.get(field_id, ''), header_keys)
            worksheet.write_row(row=index + 1, col=0, data=row)

df = pd.read_excel('Book1.xlsx',) # can also index sheet by name or fetch all sheets
# urls = df['A'].tolist()
urls = ["https://g.page/suyoghospitalmysore?share",]
BusinessScraper = GoogleMapScraper()
for url in urls:
    BusinessScraper.get_business_info(url)
print(BusinessScraper.business_info)

headers = {'name': 'Name', 'rating': 'Rating', 'reviews_count': 'Reviews Count', 'address': 'Address', 'contact': 'COVID-19 info · medisync.org', 'website': 'website'}

create_xlsx_file ("scraped_data.xlsx", headers , BusinessScraper.business_info)