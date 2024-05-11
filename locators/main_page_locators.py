from selenium.webdriver.common.by import By

class MainPageLocators:
    # вопрос 1 "Сколько это стоит? и как оплатить?"
    cost_question_button = (By.ID, 'accordion__heading-0')
    # ответ на 1 вопрос
    cost_answer_text = (By.XPATH, '//div[@id = "accordion__panel-0"]/p')
    # вопрос 2 "Хочу сразу несколько самокатов! Так можно?"
    several_scooters_question_button = (By.ID, 'accordion__heading-1')
    # ответ на 2 вопрос
    several_scooters_answer_text = (By.XPATH, '//div[@id = "accordion__panel-1"]/p')
    # вопрос 3 "Как рассчитывается время аренды?"
    rental_time_question_button = (By.ID, 'accordion__heading-2')
    # ответ на 3 вопрос
    rental_time_answer_text = (By.XPATH, '//div[@id = "accordion__panel-2"]/p')
    # вопрос 4 "Можно ли заказать самокат прямо на сегодня?"
    today_rent_question_button = (By.ID, 'accordion__heading-3')
    # ответ на 4 вопрос
    today_rent_answer_text = (By.XPATH, '//div[@id = "accordion__panel-3"]/p')
    # вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?"
    question_extend_order_button = (By.ID, 'accordion__heading-4')
    # ответ на 5 вопрос
    answer_extend_order_text = (By.XPATH, '//div[@id = "accordion__panel-4"]/p')
    # вопрос 6 "Вы привозите зарядку вместе с самокатом?"
    charge_question_button = (By.ID, 'accordion__heading-5')
    # ответ на 6 вопрос
    charge_answer_text = (By.XPATH, '//div[@id = "accordion__panel-5"]/p')
    # вопрос 7 "Можно ли отменить заказ?"
    question_cancellation_of_order_button = (By.ID, 'accordion__heading-6')
    # ответ на 7 вопрос
    answer_cancellation_of_order_text = (By.XPATH, '//div[@id = "accordion__panel-6"]/p')
    # вопрос 8 "Я жизу за МКАДом, привезёте?"
    mkad_question_button = (By.ID, 'accordion__heading-7')
    # ответ на 8 вопрос
    mkad_answer_text = (By.XPATH, '//div[@id = "accordion__panel-7"]/p')
    # кнопка "Заказать" в хедере сайте
    header_order_button = (By.CLASS_NAME, 'Button_Button__ra12g')
    # кнопка "Заказать" в центре сайта
    center_order_button = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')
    # лого "Яндекс" в хедере сайта
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')