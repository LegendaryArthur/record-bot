from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
import datebase

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Направление').add('Оставить заявку')
napravlenie_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Коммерческий дизайн')
zayavka_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Готов')
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


class StartState(StatesGroup):
    wait_command = State()
    wait_napravlenie = State()
class ZayavkaState(StatesGroup):
    wait_FIO = State()
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

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await datebase.db_start()
    await message.answer('Привет, здесь ты можешь оставить заявку на обучение в "Octopus" и узнать о всех направлениях, которые у нас есть.', reply_markup=start_keyboard)
    await StartState.wait_command.set()


@dp.message_handler(state=StartState.wait_command)
async def napravlenie(message: types.Message, state: FSMContext):
    if message.text == "Направление":
        await message.answer("Информацию о каком направлении вы хотите узнать?", reply_markup=napravlenie_keyboard)
        await StartState.wait_napravlenie.set()
    elif message.text == "Оставить заявку":
        await message.answer('Заполни анкету и попади в команжу "OCTOPUS"! \n Для начала напишите ФИО')
        await state.finish()
        await ZayavkaState.wait_FIO.set()

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
    await message.answer("В какой школе вы обучаетесь?", reply_markup=schools_keyboard)
    await ZayavkaState.wait_School.set()

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
    await message.answer("Уровень владения компьютером (1 - Что такое компьютер? 10 - Генний):", reply_markup=lvlpc_keyboard)
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
    await message.answer("Спасибо за оставленную заявку:)", reply_markup=None)








# @dp.message_handler(Text(equals='Оставить заявку'))
# async def zayavka(message: types.Message):
#     await message.answer('Здравствуйте готовы ли вы заполнить анкету чтобы попасть в команду "OCTOPUS"', reply_markup=zayavka_keyboard)
#

@dp.message_handler(content_types=['text'])
async def answer(message: types.Message):
    await message.reply('Я не понимаю вас')

if __name__ == '__main__':
    executor.start_polling(dp)