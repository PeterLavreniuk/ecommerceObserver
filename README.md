# ecommerceObserver
Initinal commit

Парсер продуктов с ozon.ru, надо запилить еще парсинг citilink, накатить на малинку и пускай крутиться.

## запилено:
- запрос страницы продукта
- парсинг необходимых полей - название/цена/цена со скидкой/цена до скидки
- сохранение в базу (ну как базу TinyDb использую - по факту жЫрный json файл)
- построение отчета (pandas)

## что надо допилить:
- файл с настройками
- запуск по шедулу, раз в день/два/неделю
- отправка отчетов на личную почту по шедулу, раз в день/два/неделю
- добавить еще ситилинк


