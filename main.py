customers = ["Иван", "Мария", "Иван", "Алексей", "Мария", "Елена"]
branch1 = {"Война и мир", "Преступление и наказание", "Мастер и Маргарита"}
branch2 = {"Война и мир", "Анна Каренина", "Мастер и Маргарита"}
branch3 = {"Война и мир", "Мастер и Маргарита", "Идиот"}
USER_STRING = '# Вы работаете редактором, и вам нужно определить, насколько разнообразен словарный запас автора в его тексте.'
"# Для этого необходимо слов Слов слов подсчитать количество уникальных слов в предоставленном фрагменте текста."
"# Вводится одна строка, состоящая вы из слов, разделённых пробелами."
"# Найдите и выведите количество уникальных слов."
USER_STRING_2 = ('The biggest room in the apartment is the living room. This is where we watch TV in the evening, '
                 'my little brother plays videogames there. My parents’ room is also big, and they have their own TV. '
                 'If my brother or I, want to watch something they do not watch, they might let us use the living '
                 'room TV and watch their favorite show in their room. They love police procedurals, I like fantasy '
                 'series, and my brother likes cartoons. My brother has a small room. There is a big closet full of '
                 'toys and Lego there. My room is not big either, I have a computer desk. This is where I do my '
                 'homework.')
text = "Задачи на программирование развивают аналитическое мышление."
text_2 = "Программирование — это искусство. Искусство требует времени и усилий."
word1 = "листо"
word2 = "стило"
text_3 = "Федеральная служба безопасности"


def task_1 (customers):
    unique_customers = []
    for i in customers:
        if i not in unique_customers:
            unique_customers.append(i)
    return unique_customers


def task_2(b1, b2, b3):
    return b1 & b2 & b3


def task_3(user_string):
    for i in range(33, 48):
        user_string = user_string.replace(chr(i), '')
    words_list = set(user_string.strip().lower().split(' '))
    return len(words_list)


def task_4(user_string):
    user_string = user_string.lower()
    for i in range(97, 123):
        print(chr(i), end='\t')
        print(user_string.count(chr(i)))


def task_5(user_string):
    words_list = user_string.split(' ')
    print(words_list)
    for index, word in enumerate(words_list):
        words_list[index] = word[::-1]
    return words_list


def task_6(user_test):
    words_list = user_test.split(' ')
    longest_word = 0
    flag = 0
    for index, word in enumerate(words_list):
        if len(word) > longest_word:
            longest_word = len(word)
            flag = index
    return words_list[flag]


def task_7(user_text):
    words_list = task_3(user_text)
    return words_list


def task_8(word1, word2):
    set_1 = set(word1)
    set_2 = set(word2)
    if len(set_1 & set_2) == len(set_1):
        return True
    else:
        False


def task_9(user_text):
    words_list = user_text.split(' ')
    abbr_ = ''
    for word in words_list:
        abbr_ = abbr_ + word.upper()[0]
    return abbr_

print(task_1(customers))
print(task_2(branch1, branch2, branch3))
print(task_3(USER_STRING))
# task_4(USER_STRING_2)
print(task_5('Слово другое слово а это не очень слово'))
print(task_6(text))
print(task_7(text_2))
print(task_8(word1, word2))
print(task_9(text_3))


