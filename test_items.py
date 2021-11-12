import time

def test_button_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	
	browser.implicitly_wait(5)
	browser.get(link) 
	# ищем все элементы с классом добавления в корзину	
	button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
	
	# оставил тайм для проверки работы
	# time.sleep(10)

	# проверяем что количество найденных элементов больше 0
	assert button > 0, 'Отсутвует кнопка добавления в корзину'


