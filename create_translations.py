import xml.etree.ElementTree as ET

uz_dict = {
    'show': "Ko'rsatish",
    'quit': 'Chiqish',
    'original': 'Asl holatda',
    'no lock': "Qulflanmasin",
    'Notice': 'Bildirishnoma',
    'Hidden here!': 'Bu yerga yashirildi!',
    'Device server path': 'Qurilma server yo‘li',
    'Push file path': 'Fayllarni uzatish yo‘li',
    'Unlimited': 'Cheksiz',
    'Maximum FPS': 'Maksimal FPS',
    'Save': 'Saqlash',
    'Apply': 'Qo‘llash',
    'Cancel': 'Bekor qilish',
    'Language': 'Til',
    'Automatic': 'Avtomatik',
    'Window title': 'Oyna nomi',
    'Double click to connect:': 'Ulanish uchun ikki marta bosing:',
    'USB connect': 'USB orqali ulanish',
    'Wireless connect': 'Simsiz ulanish (Wi-Fi)',
    'Refresh devices': 'Qurilmalarni yangilash',
    'Stop service': 'Xizmatni to‘xtatish',
    'Start service': 'Xizmatni ishga tushirish',
    'Restart service': 'Qayta ishga tushirish',
    'device serial:': 'Qurilma seriya raqami:',
    'IP': 'IP manzil',
    'Port': 'Port',
    'bitrate:': 'Bitreyt:',
    'max size:': 'Maksimal o‘lcham:',
    'record format:': 'Yozib olish formati:',
    'record path:': 'Yozib olish yo‘li:',
    'select path': 'Yo‘lni tanlash',
    'lock orientation:': 'Orientatsiyani qulflash:',
    'stay awake': 'Kutish rejimiga o‘tmaslik',
    'show fps': 'FPS ko‘rsatish',
    'always on top': 'Doim ustida turish',
    'close screen': 'Telefon ekranini o‘chirish',
    'power': 'Quvvat',
    'volume up': 'Ovozni oshirish',
    'volume down': 'Ovozni pasaytirish',
    'app switch': 'Ilovalar ro‘yxati',
    'menu': 'Menyu',
    'home': 'Bosh sahifa',
    'return': 'Orqaga',
    'open screen': 'Ekranni yoqish',
    'expand notify': 'Bildirishnomalarni ochish',
    'collapse notify': 'Bildirishnomalarni yopish',
    'screen shot': 'Skrinshot',
    'copy to device': 'Qurilmaga nusxalash',
    'paste from device': 'Qurilmadan olish',
    'install app': 'Ilova o‘rnatish',
    'file transfer': 'Fayl uzatish',
    'Settings': 'Sozlamalar',
    'Configuration saved': 'Sozlamalar saqlandi',
    'Advanced Config': 'Kengaytirilgan sozlamalar',
    'Clear History': 'Tarixni tozalash',
    'General': 'Asosiy',
    'Display': 'Ekran',
    'Record': 'Yozib olish',
    'Keys': 'Tugmalar',
    'About': 'Dastur haqida'
}

ru_dict = {
    'show': 'Показать',
    'quit': 'Выход',
    'original': 'Оригинал',
    'no lock': 'Не блокировать',
    'Notice': 'Уведомление',
    'Hidden here!': 'Скрыто здесь!',
    'Device server path': 'Путь сервера на устройстве',
    'Push file path': 'Путь передачи файлов',
    'Unlimited': 'Без ограничений',
    'Maximum FPS': 'Максимальный FPS',
    'Save': 'Сохранить',
    'Apply': 'Применить',
    'Cancel': 'Отмена',
    'Language': 'Язык',
    'Automatic': 'Автоматически',
    'Window title': 'Заголовок окна',
    'Double click to connect:': 'Двойной клик для подключения:',
    'USB connect': 'Подключение по USB',
    'Wireless connect': 'Беспроводное подключение',
    'Refresh devices': 'Обновить устройства',
    'Stop service': 'Остановить службу',
    'Start service': 'Запустить службу',
    'Restart service': 'Перезапустить',
    'device serial:': 'Серийный номер устройства:',
    'IP': 'IP адрес',
    'Port': 'Порт',
    'bitrate:': 'Битрейт:',
    'max size:': 'Макс. размер:',
    'record format:': 'Формат записи:',
    'record path:': 'Путь записи:',
    'select path': 'Выбрать путь',
    'lock orientation:': 'Блокировка ориентации:',
    'stay awake': 'Не спать',
    'show fps': 'Показывать FPS',
    'always on top': 'Поверх всех окон',
    'close screen': 'Выключить экран',
    'power': 'Питание',
    'volume up': 'Громкость +',
    'volume down': 'Громкость -',
    'app switch': 'Список приложений',
    'menu': 'Меню',
    'home': 'Домой',
    'return': 'Назад',
    'open screen': 'Включить экран',
    'expand notify': 'Открыть уведомления',
    'collapse notify': 'Скрыть уведомления',
    'screen shot': 'Скриншот',
    'copy to device': 'Копировать на устройство',
    'paste from device': 'Вставить с устройства',
    'install app': 'Установить приложение',
    'file transfer': 'Передача файлов',
    'Settings': 'Настройки',
    'Configuration saved': 'Настройки сохранены',
    'Advanced Config': 'Расширенные настройки',
    'Clear History': 'Очистить историю',
    'General': 'Основные',
    'Display': 'Экран',
    'Record': 'Запись',
    'Keys': 'Клавиши',
    'About': 'О программе'
}

def generate_ts(source_file, target_file, lang_code, trans_dict):
    tree = ET.parse(source_file)
    root = tree.getroot()
    root.attrib['language'] = lang_code
    
    for msg in root.iter('message'):
        src = msg.find('source')
        trans = msg.find('translation')
        if src is not None and src.text in trans_dict:
            trans.text = trans_dict[src.text]
            if 'type' in trans.attrib:
                del trans.attrib['type']
                
    tree.write(target_file, encoding='utf-8', xml_declaration=True)
    print(f"Generated {target_file}")

SRC = '/Users/user10/Desktop/Projects/QtScrcpy/QtScrcpy/res/i18n/en_US.ts'
generate_ts(SRC, '/Users/user10/Desktop/Projects/QtScrcpy/QtScrcpy/res/i18n/uz_UZ.ts', 'uz_UZ', uz_dict)
generate_ts(SRC, '/Users/user10/Desktop/Projects/QtScrcpy/QtScrcpy/res/i18n/ru_RU.ts', 'ru_RU', ru_dict)
