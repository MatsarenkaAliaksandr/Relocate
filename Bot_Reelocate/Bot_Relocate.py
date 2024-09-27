import requests
import telebot
import json
from telebot import types


bot = telebot.TeleBot('7484203784:AAGB8lf8qSwGq9wlObdxyDr1xt-qM_qD17c')
API = "http://134.17.16.177/api/v1/country"
country = ['Poland', 'United States', 'France', 'Germany']
countries = ['Польша', 'США', 'Франция', 'Германия', 'Вернуться в главное меню']
keyboard = ['Переезд', 'Путешествие', 'Образование', 'Работа', 'Список стран', 'Перейти на сайт', 'Соц сети']
keyboard_next: list[str] = ['Интернет', 'Проживание', 'Погода', 'Перейти на сайт', 'Вернуться в главное меню']
keyboard_second = ['Экология', 'Медицина', 'Заработная плата', 'Доступность жилья', 'Перейти на сайт', 'Вернуться в главное меню']
keyboard_education = ['Платное', 'Бесплатное', 'Перейти на сайт', 'Вернуться в главное меню']
social_network = ['Facebook', 'Instagram', 'Tiktok', 'Youtube', 'Вернуться в главное меню']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*keyboard)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Выберите что вас интересует или перейди на сайт".format(message.from_user), reply_markup=markup)

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*keyboard)
    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Образование"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_education)
        bot.send_message(message.chat.id, text="Что для вас важно?".format(message.from_user),
                         reply_markup=markup)

    elif(message.text == "Список стран"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*countries)
        bot.send_message(message.chat.id, text="Выберите страну".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Вернуться в главное меню"):
        main_menu(message)

    elif (message.text == "Соц сети"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*social_network)
        bot.send_message(message.chat.id, text="Для перехода нажмите на кнопку нужной соц сети!", reply_markup=markup)

    elif (message.text == 'Facebook'):
        bot.send_message(message.chat.id, '<i><b>https://www.facebook.com/people/Relocate-app/100093585577937</b></i>', parse_mode='html')

    elif (message.text == 'Instagram'):
        bot.send_message(message.chat.id, '<i><b>https://www.instagram.com/relocateapp</b></i>', parse_mode='html')

    elif (message.text == 'Tiktok'):
        bot.send_message(message.chat.id, '<i><b>https://www.tiktok.com/@relocateapp</b></i>', parse_mode='html')

    elif (message.text == 'Youtube'):
        bot.send_message(message.chat.id, '<i><b>https://www.youtube.com/@relocateapp</b></i>', parse_mode='html')

    elif (message.text == "Платное"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_education)

        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if data["education"]["freeEducation"] == 1:
                description_country = data['attribute']["description"]
                level_education = data['education']['educationIndexDescription']
                free_education = data['education']["freeEducation"]
                purchase_of_education = data['education']["purchaseOfEducationDescription"]
                language = data['attribute']["officialLanguage"]
                photo = open(i+'.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Язык: {language}\n"
                                                       f"Уровень образования: {level_education}\n"
                                                       f"Платное образование: {free_education}\n"
                                                       f"Стоимость образования: {purchase_of_education}\n", reply_markup=markup)
            else:
                return
        bot.send_message(message.chat.id, text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                                 reply_markup=markup)

    elif (message.text == "Бесплатное"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_education)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if data["education"]["freeEducation"] == 1:
                description_country = data['attribute']["description"]
                education_index = data['education']['educationIndex']
                education_index_description = data['education']['educationIndexDescription']
                free_education = data['education']["freeEducation"]
                language = data['attribute']["officialLanguage"]
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Язык: {language}\n"
                                                       f"Индекс образования: {education_index}\n"
                                                       f"Индекс образования(описание): {education_index_description}\n"
                                                       f"Бесплатное образование: {free_education}\n",
                               reply_markup=markup)
            else:
                return
        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Переезд"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_second)
        bot.send_message(message.chat.id, text="Что для вас важно?".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Экология"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_second)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if int(data["climat"]["climaticConditionsDescription"]) >= 1:
                description_country = data['attribute']["description"]
                pollution_level = data['climat']['pollutionLevel']
                climatic_conditions_description = data['climat']["climaticConditionsDescription"]
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Уровень загрязнения: {pollution_level}\n"
                                                       f"Особенности климатических условий: {climatic_conditions_description}\n",
                               reply_markup=markup)
            else:
                return
        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)


    elif (message.text == "Медицина"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_second)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if int(data["medicine"]["medicineIndex"]) >= 1:
                description_country = data['attribute']["description"]
                medicine_index = data['medicine']['medicineIndex']
                medicine_index_description = data['medicine']['medicineIndexDescription']
                free_medicine = data['medicine']['freeMedicine']
                free_medicine_description = data['medicine']['freeMedicineDescription']
                purchase_of_medicine = data['medicine']['purchaseOfMedicine']
                purchase_of_medicine_description = data['medicine']['purchaseOfMedicineDescription']
                availability_of_medicine = data['medicine']['availabilityOfMedicine']
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Индекс доступности и качества медицинской помощи: {medicine_index}\n"
                                                       f"Описание: {medicine_index_description}\n"
                                                       f"Бесплатная медицина: {free_medicine}\n"
                                                       f"Описание: {free_medicine_description}\n"
                                                       f"Платная медицина: {purchase_of_medicine}\n"
                                                       f"Описание: {purchase_of_medicine_description}\n"
                                                        f"Доступность медицины: {availability_of_medicine}",
                               reply_markup=markup)
            else:
                return
        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Заработная плата"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_second)
        description = []
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            description.append(int(data["job"]["medianSalary"]['usd']))
        d = description.index(max(description))
        res = requests.get(f"http://134.17.16.177/api/v1/country/{country[d]}")
        data = json.loads(res.text)
        description_country = data['attribute']["description"]
        unemployment_index = data['job']['unemploymentIndex']
        median_salary = data["job"]["medianSalary"]['usd']
        median_salary_description = data["job"]["medianSalaryDescription"]
        average_salary_description = data["job"]["averageSalaryDescription"]
        unemployment = data["job"]["unemploymentBenefit"]
        unemployment_benefit_description = data["job"]["unemploymentBenefitDescription"]
        salary_by_industry = data['job']['salaryByIndustry']
        photo = open(country[d] + '.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                               f"Индекс безработицы: {unemployment_index}\n"
                                               f"Средняя зарплата(описание): {average_salary_description}\n"
                                               f"Средняя медианная зарплата: {median_salary}\n"
                                               f"Описание: {median_salary_description}\n"
                                               f"Размер пособий по безработице: {unemployment}\n"
                                               f"Описание: {unemployment_benefit_description}\n"
                                                f"Средняя медианная зарплата по отраслям: {salary_by_industry}",
                        reply_markup=markup)

    elif (message.text == "Работа"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard)
        description = []
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            description.append(int(data["attribute"]["averageSalary"]['usd']))
        d = description.index(max(description))
        res = requests.get(f"http://134.17.16.177/api/v1/country/{country[d]}")
        data = json.loads(res.text)
        description_country = data['attribute']["description"]
        median_salary = data["job"]["medianSalary"]['usd']
        median_salary_description = data["job"]["medianSalaryDescription"]
        average_salary_description = data["job"]["averageSalaryDescription"]
        unemployment = data["job"]["unemploymentBenefit"]['usd']
        average_salar = data["attribute"]["averageSalary"]['usd']
        unemploymen_benefit_description = data["job"]["unemploymentBenefitDescription"]
        photo = open(country[d] + '.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                               f"Средняя зарплата: {average_salar}\n"
                                               f"Описание: {average_salary_description}\n"
                                               f"Медианная зарплата: {median_salary}\n"
                                               f"Описание: {median_salary_description}\n"
                                               f"Размер пособий по безработице: {unemployment}\n"
                                               f"Описание: {unemploymen_benefit_description}\n",
                       reply_markup=markup)

    elif (message.text == "Путешествие"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_next)
        bot.send_message(message.chat.id, text="Что для вас важно?".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Интернет"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_next)
        description = []
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            description.append(int(data["internet"]["internetPenetrationRate"]))
        d = description.index(max(description))
        res = requests.get(f"http://134.17.16.177/api/v1/country/{country[d]}")
        data = json.loads(res.text)
        opisanie = data['attribute']["description"]
        internet_penetration_rate = data['internet']['internetPenetrationRate']
        price_per_100Mbps = data['internet']["pricePer100Mbps"]['usd']
        territory_coverage = data['internet']["territoryCoverage"]
        connection_quality = data['internet']['connectionQuality']
        photo = open(country[d] + '.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, f"{opisanie} \n"
                                               f"Уровень проникновения интернета: {internet_penetration_rate}\n"
                                               f"Средняя цена за 100 Мбит/c: {price_per_100Mbps}\n"
                                               f"Покрытие территории: {territory_coverage}\n"
                                                f"Качество соединения: {connection_quality}\n", reply_markup=markup)

    elif (message.text == "Доступность жилья"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_next)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if int(data["housing"]["housingAffordabilityIndex"]) > 1:
                description_country = data['attribute']["description"]
                housing_afford_ability_index = data['housing']['housingAffordabilityIndex']
                price_per_sq_mRegion = data['housing']["pricePerSqMRegion"]['usd']
                price_per_sq_mCapital = data['housing']['pricePerSqMCapital']['usd']
                price_per_sq_m_description = data['housing']['pricePerSqMDescription']
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Индекс доступности жилья: {housing_afford_ability_index}\n"
                                                       f"Цена за кв. м. в регионе: {price_per_sq_mRegion}\n"
                                                       f"Цена за кв. м. в столице: {price_per_sq_mCapital}\n"
                                                       f"Цена за кв. м. в столице(описание): {price_per_sq_m_description}\n",
                               reply_markup=markup)

        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Проживание"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_next)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if int(data["housing"]["housingAffordabilityIndex"]) < 4:
                description_country = data['attribute']["description"]
                housing_afford_ability_index = data['housing']['housingAffordabilityIndex']
                rent_two_room_apartment_capital = data['housing']["rentTwoRoomApartmentCapital"]['usd']
                rent_two_room_apartment_region = data['housing']['rentTwoRoomApartmentRegion']['usd']
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Индекс доступности жилья: {housing_afford_ability_index}\n"
                                                       f"Цена за аренду двухкомантной квартиры в столице: {rent_two_room_apartment_capital}\n"
                                                       f"Цена за аренду двухкомантной квартиры в регионе: {rent_two_room_apartment_region}\n",
                               reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Погода"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*keyboard_next)
        for i in country:
            res = requests.get(f"http://134.17.16.177/api/v1/country/{i}")
            data = json.loads(res.text)
            if int(data["climat"]["averageTemperatureInSummer"]) >= 1 and int(data["climat"]["averageTemperatureInWinter"]) >= -10:
                description_country = data['attribute']["description"]
                average_temperature_summer = data['climat']['averageTemperatureInSummer']
                average_temperature_winter = data['climat']["averageTemperatureInWinter"]
                climatic_conditions_description = data['climat']['climaticConditionsDescription']
                photo = open(i + '.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, f"{description_country} \n"
                                                       f"Средняя температура летом: {average_temperature_summer}\n"
                                                       f"Средняя температура зимой: {average_temperature_winter}\n"
                                                        f"Особенности климатических условий: {climatic_conditions_description}\n",
                               reply_markup=markup)
            else:
                return
        bot.send_message(message.chat.id,
                         text="Для более подробной информации перейдите на сайт.".format(message.from_user),
                         reply_markup=markup)

    elif (message.text == "Перейти на сайт"):
        bot.send_message(message.chat.id, '<i><b>https://dev.relocatein.eu/ru</b></i>', parse_mode='html')

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..введите /start")

bot.polling(non_stop=True, interval=0)
