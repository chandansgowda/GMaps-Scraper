from selenium import webdriver

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

urls = ["https://g.page/suyoghospitalmysore?share",]
BusinessScraper = GoogleMapScraper()
for url in urls:
    BusinessScraper.get_business_info(url)
print(BusinessScraper.business_info)