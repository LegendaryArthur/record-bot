from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile

import datebase
ADMIN_ID = 1295289083

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
import datetime

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Направление').add('Оставить заявку').add('Команда "OCTOPUS"')
napravlenie_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Коммерческий дизайн')
zayavka_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Готов')
nastavniki_keyboard = InlineKeyboardMarkup()
back_1 = InlineKeyboardMarkup(row_width=1)
btn_1 = InlineKeyboardButton(text='Назад', callback_data='start')
back_1.insert(btn_1)
nastavnikPetrov = InlineKeyboardButton('Петров Роман Ильич | Python', callback_data='PetrovRI')
nastavnikKorotki = InlineKeyboardButton('Короткий Сергей Андреевич | Unity', callback_data='ShortSA')
nastavnikMashkin = InlineKeyboardButton('Машкин Павел Юрьевич | Гейм - Дизайнер', callback_data='MashkinPY')
nastavnikGareinov = InlineKeyboardButton('Гарейнов Алексей', callback_data='GareinovA')
nastavnikAntonNI = InlineKeyboardButton('Савиновский Антон Николаевич | Гейм - Дизайнер', callback_data='SavinovskyAN')
nastavnikBaturovKS = InlineKeyboardButton('Батуров Константин Сергеевич | БПЛА ', callback_data='BaturovKS')
nastavnikTinkovaNV = InlineKeyboardButton('Тинькова Наталья Владимировна | 2D-художник', callback_data='TinkovaNV')
nastavnikSavinovskayaV = InlineKeyboardButton('Cавиноская Василина | Гейм - Дизайнер', callback_data='SavinovskayaV')
nastavnikFerrary = InlineKeyboardButton('Энцо Болетти | 3D-художник', callback_data='Ferrary')
nastavnikAntonA = InlineKeyboardButton('Адаменко Антон | 3D-художник', callback_data='AntonA')
nastavnikKosoukhov = InlineKeyboardButton('Косоухов Константин | как продать детский труд', callback_data='Kids')
nastavniki_keyboard.add(nastavnikPetrov)
nastavniki_keyboard.add(nastavnikKorotki)
nastavniki_keyboard.add(nastavnikMashkin)
nastavniki_keyboard.add(nastavnikGareinov)
nastavniki_keyboard.add(nastavnikAntonNI)
nastavniki_keyboard.add(nastavnikBaturovKS)
nastavniki_keyboard.add(nastavnikTinkovaNV)
nastavniki_keyboard.add(nastavnikSavinovskayaV)
nastavniki_keyboard.add(nastavnikFerrary)
nastavniki_keyboard.add(nastavnikAntonA)
nastavniki_keyboard.add(nastavnikKosoukhov)
napravlenie_keyboard.add('Wed-разработка')
napravlenie_keyboard.add('Unity')
napravlenie_keyboard.add('Python')
napravlenie_keyboard.add('БПЛА')
napravlenie_keyboard.add('Компьютерная грамотность')
napravlenie_keyboard.add('3D-моделирование')
napravlenie_keyboard.add('2D-моделирование')
schools_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add('МАОУ "Гимназия №1"').add('МАОУ "СОШ №2"').add('МАОУ "ООШ №3"').add('МАОУ "СОШ №4"').add('МАОУ "СОШ №5"')
otvet_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Да').add('Нет')
lvlpc_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5).add('1').add('2').add('3').add('4').add('5').add('6').add('7').add('8').add('9').add('10')
smena_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('В первую').add('Во вторую')
pravilno_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Да, всё правильно').add('Нет, не правильно')

class StartState(StatesGroup):
    wait_command = State()
    wait_napravlenie = State()
    wait_nastavniki = State()
class ZayavkaState(StatesGroup):
    wait_FIO = State()
    wait_Photo = State()
    wait_School = State()
    wait_Class = State()
    wait_Vozvrast = State()
    wait_Yspevaimoct = State()
    wait_NumberPhone = State()
    wait_ProvilSotSety = State()
    wait_Napravlenie1 = State()
    wait_Napravlenie2 = State()
    wait_SlyxiObOctopus = State()
    wait_KakayaSmena = State()
    wait_KakiyeKrushki = State()
    wait_KemStanesh = State()
    wait_LVLPC = State()
    wait_YchastieVProject = State()
    wait_TimeDZ = State()
    wait_Progress = State()
    wait_KakayaLichnoct = State()
    wait_Konec = State()
    wait_Confirmation = State()
    wait_Pravilno = State()
    wait_Nastavniki = State()
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await datebase.db_start()
    await message.answer('Привет, здесь ты можешь оставить заявку на обучение в "Octopus" и узнать о всех направлениях, которые у нас есть, а также ты можешь ознакомится с каждым наставником всех направлений.', reply_markup=start_keyboard)
    await StartState.wait_command.set()

@dp.message_handler(commands='id')
async def cmd_id(message: types.Message):
    await message.answer(message.chat.id)

@dp.message_handler(state=StartState.wait_command)
async def napravlenie(message: types.Message, state: FSMContext):
    if message.text == "Направление":
        await message.answer("Информацию о каком направлении вы хотите узнать?", reply_markup=napravlenie_keyboard)
        await StartState.wait_napravlenie.set()
    elif message.text == 'Команда "OCTOPUS"':
        await message.answer("О каком наставнике вы хотите узнать?", reply_markup=nastavniki_keyboard)
        await state.finish()
    elif message.text == "Оставить заявку":
        await message.answer('Заполни анкету и попади в команду "OCTOPUS"! \n Для начала напишите ФИО')
        await state.finish()
        await ZayavkaState.wait_FIO.set()

@dp.message_handler(commands="team_octopus")
async def cmd_octopus_team(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Команда октопус", callback_data="team_octopus "))

    await message.answer("Нажмите на кнопку, чтобы бот отправил информацию о Команде 'Octopus'", reply_markup=keyboard)

@dp.callback_query_handler(text="PetrovRI")
async def send_team_octopus(call: types.CallbackQuery,):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Роман Петров с очками.jpg'), caption=f"Наставник по Python:\nФИО: Петров Роман Ильич\n", reply_markup=None)
    await bot.send_message(call.from_user.id, 'Чтобы вернуться нажмите кнопку', reply_markup=back_1)


@dp.callback_query_handler(text="GareinovA")
async def send_team_octopus(call:types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Алексей Гарейнов с очками.jpg'), caption=f"")

@dp.callback_query_handler(text="SavinovskyAN")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Антон Савиновский.jpg'), caption=f"Наставник по направление 'Геймдизайн':\nФИО: Савиновский Антон Николаевич\n", reply_markup=None)



@dp.callback_query_handler(text="SavinovskayaV")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Василина Савиновская.jpg'), caption=f"Наставник по направление 'Геймдизайн':\nФИО: Савиновская Василина Николаевна\n", reply_markup=None)



@dp.callback_query_handler(text="BaturovKS")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Конастантин Батурин.jpg'), caption=f"Наставник по БПЛА:\nФИО: Батурин Константин\n", reply_markup=None)

@dp.callback_query_handler(text="Kids")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Константин Косоухов.jpg'), caption=f"Наставник по БПЛА:\nФИО: Косоухов Константин\n", reply_markup=None)

@dp.callback_query_handler(text="MashkinPY")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Павел Машкин.jpg'), caption=f"Наставник по направление 'Геймдизайн':\nФИО: Машкин Павел Юрьевич\n", reply_markup=None)

@dp.callback_query_handler(text="ShortSA")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Сергей Короткий с очками.jpg'), caption=f"Наставник по Unity:\nФИО: Короткий Сергей Андреевич\n", reply_markup=None)



@dp.callback_query_handler(text="Ferrary")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Энцо Феррари.jpg'), caption=f"Наставник по Unity:\nФИО: Короткий Сергей Андреевич\n", reply_markup=None)

@dp.callback_query_handler(text="AntonA")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Антон Адаменко.jpg'), caption=f"Наставник 3D-художников:\nФИО: Адаменко Антон \n", reply_markup=None)


@dp.callback_query_handler(text="TinkovaNV")
async def send_team_octopus(call: types.CallbackQuery):
    await bot.send_photo(call.message.chat.id, photo=InputFile(r'C:\PYTHON\projects\record-bot\photos\Наталья Тинькова.jpg'), caption=f"Наставник 2D-художников:\nФИО: Тинькова Наталья Владимировна\n", reply_markup=None)

@dp.message_handler(state=StartState.wait_napravlenie)
async def napravlenie_info(message: types.Message, state: FSMContext):
    if message.text == 'Коммерческий дизайн':
        await message.answer('На курсе "Коммерческий дизайн вы изучите:'
                             'Основы графического дизайна.'
                             'Принципы создания эффектных и запоминающихся рекламных кампаний.'
                             'Техники работы в ведущих графических редакторах."'
                             'Основы брендинга и маркетинга.'
                             'Как превратить творчество в прибылный бизнес.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()
    elif message.text == 'Wed-разработка':
        await message.answer('В этом образовательном курсе вы изучите:'
                             'Основы HTML, CSS и JavaScript – языки, на которых строится веб.'
                             'Основы работы с фреймворками и библиотеками, такими как React и Angular.'
                             'Понимание UX/UI дизайна для создания интуитивно понятных веб-страниц."'
                             'Введение в backend-разработку и базы данных.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()

    elif message.text == 'Unity':
        await message.answer('Чтобы стать профессиональным Unity-разработчиком, нужно изучить следующее:'
                             'Базовые манипуляции со сценой, объектами, assets и prefabs.'
                             'Векторы, проекции и математика для 3D графики.'
                             'Создание пользовательского интерфейса в игре."'
                             'Работа с материалами.'
                             'Модули физики для 2D и 3D.'
                             'Система анимации Mecanim.'
                             'Системы частиц.'
                             'Работа с аудио.'
                             'Работа с разными графическими пайплайнами.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()

    elif message.text == 'Python':
        await message.answer('В курсе по обучению языка програмирования на "Python" вы получите такие знания как:'
                             'Научитесь писать код на языке Python.'
                             'Сможете использовать фреймворк Django.'
                             'Будете создавать REST API.'
                             'А так же настраивать серверы.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()

    elif message.text == 'БПЛА':
        await message.answer('При обучении о БПЛА вы узнаете:'
                             'Устройства и принципы работы дронов.'
                             'Планы полётов по определенной территории.'
                             'Как пилотировать и программировать беспилотник, а также практическому взаимодействию с квадрокоптерами.'
                             'Как овладеть навыками анализа данных полученных с дрона в профессиональных программах.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()
    elif message.text == 'Компьютерная грамотность':
        await message.answer('Компьютерная грамотность научит вас:'
                             'Создавать интерфейсы сайтов.'
                             'Разрабатывать серверную часть сайтов.'
                             'Работать с базами данных.'
                             'Использовать фреймворки.'
                             'Использовать инструменты разработчика.'
                             'Работать в IT-команде.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()
    elif message.text == '3D-моделирование':
        await message.answer('Благодаря 3D-моделированию вы сумеете :'
                             'Узнаете, как работают разные типы 3D-принтеров.'
                             'Узнаете, как делать чертежи с правильной компоновкой деталей и научитесь выгодно презентовать их своим клиентам.'
                             'Освоите востребованный технический скилл: сможете анализировать готовые изделия и создавать их точные копии.'
                             'Научитесь готовить модель к печати, настраивать принтер, печатать качественные модели и быстро исправлять дефекты.'
                             'Освоите востребованную программу Компас 3D.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()
    elif message.text == '2D-моделирование':
        await message.answer('Благодаря 2D-моделированию вы сумеете :'
                             'Познакомитесь с базовыми понятиями света, цвета, композиции, анатомии и перспективы.'
                             'Научитесь работать с референсами и создавать правильные заготовки для будущих 2D-объектов.'
                             'Получите от экспертов лайфхаки, которые существенно упростят и ускорят работу .'
                             'Освоите тонкости работы в Photoshop, даже если до этого не работали в нём.'
                             'Нарисуете в разных стилях иконки, персонажей и иллюстрации на основе скетчей.')
        await message.answer("Для продолжения напишите команду /start")
        await state.finish()
@dp.message_handler(state=ZayavkaState.wait_FIO)
async def fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)

    await message.answer("Пришлите свою фотографию:", reply_markup=None)
    await ZayavkaState.wait_Photo.set()
@dp.message_handler(state=ZayavkaState.wait_Photo, content_types=['text', 'photo'])
async def photo(message: types.Message, state: FSMContext):
    if message.photo:
        await state.update_data(chat_id=message.chat.id)
        await state.update_data(username=message.from_user.username)
        await state.update_data(photo=message.photo[-1].file_id)
        await message.answer("В какой школе вы обучаетесь?", reply_markup=schools_keyboard)
        await ZayavkaState.wait_School.set()
    else:

        await message.answer('Отправьте свою фотографию')
@dp.message_handler(state=ZayavkaState.wait_School)
async def school(message: types.Message, state: FSMContext):
    await state.update_data(school=message.text)
    await message.answer("Ваш класс обучения:", reply_markup=None)
    await ZayavkaState.wait_Class.set()

@dp.message_handler(state=ZayavkaState.wait_Class)
async def class_(message: types.Message, state: FSMContext):
    await state.update_data(class_=message.text)
    await message.answer("Напишите свой возраст:", reply_markup=None)
    await ZayavkaState.wait_Vozvrast.set()

@dp.message_handler(state=ZayavkaState.wait_Vozvrast)
async def vozvrast(message: types.Message, state: FSMContext):
    await state.update_data(vozvrast=message.text)
    await message.answer("Какая у тебя успеваемость в школе?", reply_markup=None)
    await ZayavkaState.wait_Yspevaimoct.set()

@dp.message_handler(state=ZayavkaState.wait_Yspevaimoct)
async def numberphone(message: types.Message, state: FSMContext):
    await state.update_data(yspevaimoct=message.text)
    await message.answer("Введите номер телефона:", reply_markup=None)
    await ZayavkaState.wait_NumberPhone.set()

@dp.message_handler(state=ZayavkaState.wait_NumberPhone)
async def provilsotsety(message: types.Message, state: FSMContext):
    await state.update_data(NumberPhone=message.text)
    await message.answer("Оставьте ссылку своих сотсетей:", reply_markup=None)
    await ZayavkaState.wait_ProvilSotSety.set()

@dp.message_handler(state=ZayavkaState.wait_ProvilSotSety)
async def napravlenie1(message: types.Message, state: FSMContext):
    await state.update_data(provilSotSety=message.text)
    await message.answer("На какое направление хотел/ла бы пойти:", reply_markup=napravlenie_keyboard)
    await ZayavkaState.wait_Napravlenie1.set()

@dp.message_handler(state=ZayavkaState.wait_Napravlenie1)
async def napravlenie2(message: types.Message, state: FSMContext):
    await state.update_data(napravlenie1=message.text)
    await message.answer("Выберите другое направление, которое вам интересно:", reply_markup=napravlenie_keyboard)
    await ZayavkaState.wait_Napravlenie2.set()

@dp.message_handler(state=ZayavkaState.wait_Napravlenie2)
async def slyxioboctopus(message: types.Message, state: FSMContext):
    await state.update_data(napravlenie2=message.text)
    await message.answer("Слышал/ла когда-нибудь о проекте Octopus?", reply_markup=otvet_keyboard)
    await ZayavkaState.wait_SlyxiObOctopus.set()

@dp.message_handler(state=ZayavkaState.wait_SlyxiObOctopus)
async def kakayasmena(message: types.Message, state: FSMContext):
    await state.update_data(slyxiObOctopus=message.text)
    await message.answer("В какую смену учишься?", reply_markup=smena_keyboard)
    await ZayavkaState.wait_KakayaSmena.set()

@dp.message_handler(state=ZayavkaState.wait_KakayaSmena)
async def kakyekrushki(message: types.Message, state: FSMContext):
    await state.update_data(kakayasmena=message.text)
    await message.answer("Какие дополнительные объединения посещаешь и в какое время?", reply_markup=None)
    await ZayavkaState.wait_KakiyeKrushki.set()

@dp.message_handler(state=ZayavkaState.wait_KakiyeKrushki)
async def kemstanesh(message: types.Message, state: FSMContext):
    await state.update_data(kakiyekrushki=message.text)
    await message.answer("Кем ты хочешь стать?", reply_markup=None)
    await ZayavkaState.wait_KemStanesh.set()

@dp.message_handler(state=ZayavkaState.wait_KemStanesh)
async def lvlpc(message: types.Message, state: FSMContext):
    await state.update_data(kemstanesh=message.text)
    await message.answer("Уровень владения компьютером (1 - Что такое компьютер? 10 - Гений):", reply_markup=lvlpc_keyboard)
    await ZayavkaState.wait_LVLPC.set()

@dp.message_handler(state=ZayavkaState.wait_LVLPC)
async def ychastievproject(message: types.Message, state: FSMContext):
    await state.update_data(lvlpc=message.text)
    await message.answer("Участвовал/ла ли в каких-либо значимых проектах и конкурсах?", reply_markup=None)
    await ZayavkaState.wait_YchastieVProject.set()

@dp.message_handler(state=ZayavkaState.wait_YchastieVProject)
async def timedz(message: types.Message, state: FSMContext):
    await state.update_data(YchastieVProject=message.text)
    await message.answer("Сколько времени ты тратишь на выполнение домашнего задания?", reply_markup=None)
    await ZayavkaState.wait_TimeDZ.set()

@dp.message_handler(state=ZayavkaState.wait_TimeDZ)
async def progress(message: types.Message, state: FSMContext):
    await state.update_data(timedz=message.text)
    await message.answer("Коротко опишите, что вы считаете прогрессом?", reply_markup=None)
    await ZayavkaState.wait_Progress.set()

@dp.message_handler(state=ZayavkaState.wait_Progress)
async def kakayalichnoct(message: types.Message, state: FSMContext):
    await state.update_data(progress=message.text)
    await message.answer("Считаете ли вы себя уникальной личностью? Коротко аргументируйте ваш ответ:", reply_markup=None)
    await ZayavkaState.wait_KakayaLichnoct.set()

@dp.message_handler(state=ZayavkaState.wait_KakayaLichnoct)
async def konec(message: types.Message, state: FSMContext):
    await state.update_data(lichnost=message.text)

    data = await state.get_data()
    await ZayavkaState.wait_Confirmation.set()
    await bot.send_photo(data["chat_id"], photo=data['photo'], caption=f"Ваша заявка:\nФИО: {data['fio']}\nШКОЛА:{data['school']}\nКЛАСС:{data['class_']}\nВОЗРАСТ:{data['vozvrast']}\nУСПЕВАЕМОСТЬ:{data['yspevaimoct']}\nНОМЕР ТЕЛЕФОНА:{data['NumberPhone']}\nСОЦ.СЕТИ:{data['provilSotSety']}\nНАПРАВЛЕНИЕ 1:{data['napravlenie1']}\nНАПРАВЛЕНИЕ 2:{data['napravlenie2']}\nСЛЫШАЛ ЛИ ТЫ ОБ ОКТОПУСЕ:{data['slyxiObOctopus']}\nТВОЯ СМЕНА:{data['kakayasmena']}\nТВОИ ДОП.КРУЖКИ:{data['kakiyekrushki']}\nТОТ КЕМ ТЫ ХОЧЕШЬ СТАТЬ:{data['kemstanesh']}\nУРОВЕНЬ ВЛАДЕНИЯ КОМПЬЮТЕРОМ:{data['lvlpc']}\nТВОЁ УЧАСТИЕ В ПРОЕКТАХ:{data['YchastieVProject']}\nТВОЁ ЗАТРАЧЕННОЕ ВРЕМЯ НА ДОМАШКУ:{data['timedz']}\nМНЕНИЕ ЧТО ТАКОЕ ПРОГРЕСС:{data['progress']}\nУНИКАЛЬНАЯ ЛИЧНОСТЬ:{data['lichnost']}\n", reply_markup=None)
    await message.answer("Заявка заполнена, Проверьте всё ли правильно:", reply_markup=pravilno_keyboard)

    await ZayavkaState.wait_Confirmation.set()
@dp.message_handler(state=ZayavkaState.wait_Confirmation)
async def Confirmation(message: types.Message, state: FSMContext):
    if message.text == 'Да, всё правильно':

        date = datetime.datetime.now()
        data = await state.get_data()
        await datebase.add_zapis(date, data)
        await bot.send_photo(ADMIN_ID, photo=data['photo'], caption=f"Новая заявка:\nФИО: {data['fio']}\nШКОЛА:{data['school']}\nКЛАСС:{data['class_']}\nВОЗРАСТ:{data['vozvrast']}\nУСПЕВАЕМОСТЬ:{data['yspevaimoct']}\nНОМЕР ТЕЛЕФОНА:{data['NumberPhone']}\nСОЦ.СЕТИ:{data['provilSotSety']}\nНАПРАВЛЕНИЕ 1:{data['napravlenie1']}\nНАПРАВЛЕНИЕ 2:{data['napravlenie2']}\nСЛЫШАЛ ЛИ ТЫ ОБ ОКТОПУСЕ:{data['slyxiObOctopus']}\nТВОЯ СМЕНА:{data['kakayasmena']}\nТВОИ ДОП.КРУЖКИ:{data['kakiyekrushki']}\nТОТ КЕМ ТЫ ХОЧЕШЬ СТАТЬ:{data['kemstanesh']}\nУРОВЕНЬ ВЛАДЕНИЯ КОМПЬЮТЕРОМ:{data['lvlpc']}\nТВОЁ УЧАСТИЕ В ПРОЕКТАХ:{data['YchastieVProject']}\nТВОЁ ЗАТРАЧЕННОЕ ВРЕМЯ НА ДОМАШКУ:{data['timedz']}\nМНЕНИЕ ЧТО ТАКОЕ ПРОГРЕСС:{data['progress']}\nУНИКАЛЬНАЯ ЛИЧНОСТЬ:{data['lichnost']}\n", reply_markup=None)
        await state.finish()
    elif message.text == 'Нет, не правильно':
        await message.answer("Если вы обнаружили ошибки в своей заявке, пожалуйста заполните её занового нажав команду /start")




# @dp.message_handler(Text(equals='Оставить заявку'))
# async def zayavka(message: types.Message):
#     await message.answer('Здравствуйте готовы ли вы заполнить анкету чтобы попасть в команду "OCTOPUS"', reply_markup=zayavka_keyboard)
#

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)