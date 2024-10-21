from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# opens a Chrome driver
my_driver = webdriver.Chrome()
# variable to make our chrome driver to wait 10 second so the element we are looking for will appear
wait_for_elemnts = WebDriverWait(my_driver, 10)



# get url of humanity
url = my_driver.get("https://incapsula.humanity.com/app/")

#inserts my credentials FYI not secure
my_driver.find_element(by="id", value="email").send_keys("")
my_driver.find_element(by="id", value="password").send_keys("")

#clicks the login button
my_driver.find_element(by="name", value="login").click()
# waits until the desired element loads up on the web
go_to_my_shifts = wait_for_elemnts.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"topMenu\"]/li[2]")))

# clicks  the shift plannig window
my_driver.find_element(by="xpath", value="//*[@id=\"topMenu\"]/li[2]").click()



sleep(10)

