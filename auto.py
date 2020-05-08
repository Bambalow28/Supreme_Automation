"""   SUPREME WEBSITE AUTOMATION   """
"""   PROGRAMMED USING SELENIUM & PYTHON   """

"""   IMPORT WEB DRIVER & SELECT   """
from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""   ASSIGN DRIVER PATH 'edgedriver' to 'browser' VARIABLE AND OPEN SPECIFIED WEBSITE USING GET()    """
browser = webdriver.Edge('C:\\Users\\Bambalow28\\Desktop\\edgedriver')
browser.get('https://www.supremenewyork.com/shop/all/shirts')

"""   FIND ELEMENT IN THE BROWSER AND CLICK   """
item = browser.find_element_by_link_text('Light Purple')
item.click()

"""   GIVE BROWSER A 15ms WAIT TIME   """
browser.implicitly_wait(15)

"""   GET 'ID' ELEMENT OF SIZE DROPDOWN MENU AND SELECT SIZE USING TEXT   """
getSize = Select(browser.find_element_by_id('s'))
getSize.select_by_visible_text('Large')

"""   USING XPATH TO FIND AND CLICK THE 'ADD TO CART' BUTTON   """
"""   ADD TO CART BUTTON IS NOT A REAL BUTTON THUS NEEDING XPATH   """
add = browser.find_elements_by_xpath("//input[@name='commit' and @value='add to cart']")[0]
add.click()

"""   FIND CHECKOUT 'BUTTON' USING XPATH   """
"""   SAME CONDITION AS 'ADD TO CART'   """
checkout = browser.find_element_by_xpath("//*[@id='cart']/a[2]")
checkout.click()

"""   INPUT INFORMATION   """
"""   FIND ELEMENT BY ID THEN SEND KEYS TO INPUT DATA   """
fullName = browser.find_element_by_id('order_billing_name')
fullName.send_keys('Joshua Alanis')

orderEmail = browser.find_element_by_id('order_email')
orderEmail.send_keys('joshalanis28@gmail.com')

cellNum = browser.find_element_by_id('order_tel')
cellNum.send_keys('226-979-7607')

orderAddress = browser.find_element_by_id('bo')
orderAddress.send_keys('261 Elmira Rd. South')

selectCountry = Select(browser.find_element_by_id('order_billing_country'))
selectCountry.select_by_visible_text('CANADA')

orderZip = browser.find_element_by_id('order_billing_zip')
orderZip.send_keys('N1K 1P9')

orderCity = browser.find_element_by_id('order_billing_city')
orderCity.send_keys('Guelph')

selectState = Select(browser.find_element_by_id('order_billing_state'))
selectState.select_by_visible_text('ON')

cardNum = browser.find_element_by_id('rnsnckrn')
cardNum.send_keys('1234567890123456')

selectMonth = Select(browser.find_element_by_id('credit_card_month'))
selectMonth.select_by_visible_text('08')

selectYear = Select(browser.find_element_by_id('credit_card_year'))
selectYear.select_by_visible_text('2024')

cardCVV = browser.find_element_by_id('orcer')
cardCVV.send_keys('128')

"""   FIND ELEMENT OF CHECKBOX AND CLICK(CHECK)   """
agreeTerms = browser.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p[2]/label")
agreeTerms.click()

"""   FIND 'PROCESS PAYMENT' ELEMENT THEN CLICK TO FINISH   """
processPayment = browser.find_elements_by_xpath("//input[@name='commit' and @value='process payment']")[0]
processPayment.click()

browser.close()

"""   END OF CODE   """



