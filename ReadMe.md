# Code smells - Homework 22
### Работа взята у Вадима Владимирова, вот его GitHub:
[Vadim Vladimirov - GitHub](https://github.com/cestxvcdim)

### Code smell в функции main:
Длина функции main() может быть уменьшена, 
разбив ее на более мелкие функции с конкретной ответственностью. 
Так же нужна документация.
#### Бывший код:
```python
from classes.store import Store
from classes.shop import Shop
from classes.request import Request
from utils import load_script, load_log


def main():
    store = Store({
        "миндаль": 16,
        "шоколадки": 23,
        "велосипеды": 7
    })
    shop = Shop({
        "шоколадки": 6,
        "велосипеды": 2,
        "торты": 1
    })

    print(load_script("greetings"))
    print(load_script("inst"))
    print(load_script("action1"))
    print(load_script("action1/req"))
    print(load_script("action2"))
    print(load_script("action2/req"))
    print(load_script("store/state"))
    print(store.get_items())
    print(load_script("shop/state"))
    print(shop.get_items())
    print(load_script("for/end"))
    print(load_script("start"))

    while True:
        req = input().lower()
        if req == "завершить":
            print(load_script("end"))
            break
        print(load_log("check/req"))
        request = Request(req)
        try:
            if not request.is_incorrect(shop, store):
                print(f'{load_log("info/req")}\n{request}')
        except ValueError:
            print(load_log('req/error'))
            continue
        if request.to == 'магазин':
            shop.add(request.product, request.amount)
            store.remove(request.product, request.amount)
        elif request.to == 'склад':
            store.add(request.product, request.amount)
            shop.remove(request.product, request.amount)
        else:
            print(load_log('loc/error'))
            continue

        print(load_script("store/state"))
        print(store.get_items())
        print(load_script("shop/state"))
        print(shop.get_items())


if __name__ == "__main__":
    main()
```

#### Исправленный код:
```python
from classes.store import Store
from classes.shop import Shop
from classes.request import Request
from utils import load_script, load_log


def initialize_store() -> Store:
    """
    Инициализирует объект класса Store с начальным набором товаров.
    :return: Объект класса Store
    """
    return Store({
        "миндаль": 16,
        "шоколадки": 23,
        "велосипеды": 7
    })


def initialize_shop() -> Shop:
    """
    Инициализирует объект класса Shop с начальным набором товаров.
    :return: Объект класса Shop
    """
    return Shop({
        "шоколадки": 6,
        "велосипеды": 2,
        "торты": 1
    })


def process_request(request: Request, shop: Shop, store: Store) -> None:
    """
    Обрабатывает запрос и выполняет соответствующие операции с объектами классов Shop и Store.
    :param request: Объект класса Request, содержащий информацию о запросе
    :param shop: Объект класса Shop
    :param store: Объект класса Store
    """
    if request.to == 'магазин':
        shop.add(request.product, request.amount)
        store.remove(request.product, request.amount)
    elif request.to == 'склад':
        store.add(request.product, request.amount)
        shop.remove(request.product, request.amount)
    else:
        print(load_log('loc/error'))


def main_loop(shop: Shop, store: Store) -> None:
    """
    Цикл обработки запросов.
    :param shop: Объект класса Shop
    :param store: Объект класса Store
    """
    while True:
        try:
            req = input().lower()
            if req == "завершить":
                print(load_script("end"))
                break
            print(load_log("check/req"))
            request = Request(req)
            if request.is_incorrect(shop, store):
                print(load_log('req/error'))
            else:
                print(f'{load_log("info/req")}\n{request}')
                process_request(request, shop, store)
                print(load_script("store/state"))
                print(store.get_items())
                print(load_script("shop/state"))
                print(shop.get_items())
        except ValueError:
            print(load_log('req/error'))


def main() -> None:
    """
    Запускает программу.
    """
    try:
        shop = initialize_shop()
        store = initialize_store()
        print(load_script("greetings"))
        print(load_script("inst"))
        print(load_script("action1"))
        print(load_script("action1/req"))
        print(load_script("action2"))
        print(load_script("action2/req"))
        print(load_script("store/state"))
        print(store.get_items())
        print(load_script("shop/state"))
        print(shop.get_items())
        print(load_script("for/end"))
        print(load_script("start"))
        main_loop(shop, store)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
```

## Завершение:

Я считаю, что код, который я предложил, 
имеет более четкую структуру и более читабелен, 
так как разделяет логику на более мелкие функции 
с определенной ответственностью и использует обработку 
исключений для предотвращения возможных сбоев в работе программы.
Так же все скрипты можно вывести тоже в отдельную функцию, но это не так принципиально.

Код, который предоставил Вадим, может быть труднее понять и поддерживать
в долгосрочной перспективе, так как все действия сосредоточены в функции main, 
и отсутствует обработка исключений, которая может привести к неожиданным ошибкам. 
Однако, этот код может быть более простым в реализации для некоторых людей, и если код 
выполняет требуемую функциональность и не вызывает проблем, то он может быть приемлемым.

Тем не менее, в целом, лучшей практикой является разделение логики на более 
мелкие и понятные функции и обработка возможных ошибок, чтобы код был более 
устойчивым и легче поддерживаемым.

Так же все классы Вадима были выполнены верно, и там небыли найдены неприятные запахи!)


