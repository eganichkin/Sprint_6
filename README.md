## Sprint_6

### Cписок реализованных тестов:

1. test_cross_over_from_yandex_logo
    > **Проверка: если нажать на логотип Яндекса, в новом окне открывается страница Дзена.**
    >>    На главной странице ищем и нажимаем на логити Яндекса, проверяем, что в новом окне
          через редирект откроется главная страница Дзена. 
2. test_cross_over_from_scooter_logo
    > **Проверка: если нажать на логотип Самоката, происходит переход на главную страницу сайта**
    >>    На странице оформления заказа нажимаем на логитип "Самокат",
          проверяем, что происходит переход на главную страницу.    

3. test_questions_list_select_number_question_check_correct_of_answer
    > **Проверка текста вопросов в выпадающем списке раздела «Вопросы о важном»**
    >> На главной странице сайта ищем вопрос под номером и проверяем, что ниже
       представленный ответ на него совпадает с ожидаемым результатом. 
       Тест запускается с параметризацией передающей для каждого из 8-ми вопросов соответствуещий
       номер и ожидаемый ответ.  
4. test_create_order_by_top_button_check_completion_status
    > **Проверка позитивного сценария процесса создания заказа по нажатию на верхнюю кнопку "Заказать"**
    >> На главной странице сайта нажимаем на верхнюю кнопку "Заказать", в форме заполнения
       информации по заказу вводим корректную информацию, сохраняем  и проверяем, что заказ оформлен.   
5. test_create_order_by_low_button_check_completion_status
    > **Проверка позитивного сценария процесса создания заказа по нажатию на нижнюю кнопку "Заказать"**
    >> На главной странице сайта нажимаем на нижнюю кнопку "Заказать", в форме заполнения
       информации по заказу вводим корректную информацию, сохраняем  и проверяем, что заказ оформлен.