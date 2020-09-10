from selenium import webdriver
import csv
import re
import time

def main():
    Chromedriver_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    # make sure it runs at the backend
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(Chromedriver_path, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(6)
    driver.get("https://admissions.msu.edu/academics/default.aspx")
    time.sleep(1)
    
    # print('file for pages created')
    print("-----------------------------")
    print("get page info from msu.edu...")
    print("-----------------------------")
    text_file = open("Pages.txt", "w", encoding="utf-8")
    links=[]
    for link in driver.find_elements_by_xpath("//*[@href]"):
        url = link.get_attribute('href')
        print(url)
        links.append(url)
    print("number of links fetched: ", len(links))

    raw_data=[]
    # test multiple pages
    print("----------------------------")
    print("fetch data from each page...")
    print("----------------------------")
    for link in links:
        driver.get(link)
        print("current page: ", link)
        raw_info = driver.find_elements_by_xpath('//*[@id="standard-content-page"]')
        for data in raw_info:
            raw_data.append(data.text)
            print("write data to txt file...")
            text_file.write(data.text)
            print(data.text)
    print(len(raw_data))

    # # test one page
    # print("links: ")
    # print(links[23])
    # driver.get(links[23])
    #
    # raw_info = driver.find_elements_by_xpath('//*[@id="standard-content-page"]')
    # for data in raw_info:
    #     raw_data.append(data.text)

    # print("write data to txt file...")
    # for data in raw_data:
    #     # csv_f.writerow(data)
    #     print(data)
    #     text_file.write(data)

    text_file.close()

    #
    # first = raw_data[0]
    # csv_f.writerow(first)
    driver.quit()


    ## for testing on one page
    # view_page_path = 'https://www.imooc.com/course/coursescore/id/9?page=9'
    # driver.get(view_page_path)
    # get_user_info(driver)
    # print(raw_data)
    # print(len(raw_data))
    #to_file()


if __name__ == '__main__':
  main()
