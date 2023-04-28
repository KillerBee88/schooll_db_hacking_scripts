# schooll_db_hacking_scripts
## Помощь Ивану Фролову в освоении хакинга
Скрипт имеет несколько функций для изменения плохих оценок, удаления замечаний ученика, добавления похвалы ученику

## Описание функций:

1.```create_commendation```- создает похвалу ученику

2.```remove_chastisements```- удаляет все замечания ученика

3.```fix_marks```- исправляет все двойки и тройки на пятерки

### Для запуска скрипта потребуется скачать скрипт ```hacking_scripts.py``` в корневую папку.

Далее импортировать функции в shell командой ```from hacking_scripts import ***```, где вместо звездочек нужно указать название функции:

```create_commendation```

```remove_chastisements```

```fix_marks```

Затем прописать функцию в терминале с указанием фамилии и имени ученика, а в случае с функцией ```create_commendation```- еще и название предмета.

Например:

```create_commendation('Фролов Иван', 'Музыка')```

```remove_chastisements('Фролов Иван')```

```fix_marks('Фролов Иван')```

