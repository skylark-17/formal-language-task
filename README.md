Жаворонков Никита Б05-023

Задача:
Даны α, буква x и натуральное число k. Вывести длину кратчайшего слова из языка L, содержащего префикс x^k.

У меня есть 2 массива, с помощью которых всё пересчитывается: 
  1) can_do_xk[i] - лежит ли слово x^i в языке L.
  2) min_len_prefix[i] - минимальное слово, лежащее в языке L, с префиксом x^i.

Я иду по регулярке и поддерживаю стек, элементы которого: object_stack. 
1) Когда появляется '+', нужно нужно взять минимумы для min_len_prefix и OR для can_do_xk[i]

2) При умножении немного сложнее. Всё зависит от левого слова: какой у него префикс достижим.
3) Во время звезды Клини, получается аналог задачи о рюкзаке с повторениями: нужно проверить, можно ли получить слово с префиксом x^i.

Для работы нужно заполнить поля info_class(через поток ввода или через файл) и запустить calculate(info_class). Результатом будет целое число или inf.

Покрытие 100%. HTML-ка лежит в htmlcov/index.html