from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Edge('C:\\Users\\Bambalow28\\Desktop\\edgedriver')
browser.get('https://www.supremenewyork.com/shop/all/shirts')

item = browser.find_element_by_link_text('Light Purple')
item.click()

browser.implicitly_wait(15)
getSize = Select(browser.find_element_by_id('s'))
getSize.select_by_visible_text('Large')

add = browser.find_elements_by_xpath("//input[@name='commit' and @value='add to cart']")[0]
add.click()

checkout = browser.find_element_by_xpath("//*[@id='cart']/a[2]")
checkout.click()

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

agreeTerms = browser.find_element_by_xpath("//*[@id='cart-cc']/fieldset/p[2]/label")
agreeTerms.click()

processPayment = browser.find_elements_by_xpath("//input[@name='commit' and @value='process payment']")[0]
processPayment.click()





