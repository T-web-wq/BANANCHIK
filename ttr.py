import streamlit as LP


def FINIK(password):
    count_specsymbol = 0
    count_the_capital = 0
    count_lowersece = 0
    for symbol in password:
        if symbol in '!@#$%^&*()_*"№;:?<\=/|':
            count_specsymbol += 1
        if symbol in 'йцукенгшщзхъфывапролджэячсмитьбюё':
            count_lowersece += 1
        if symbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            count_the_capital +=1

    if len(password) <= 5:
     LP.text('не менее 5 символов')
    elif len(password) >= 10:
     LP.text('Не более 10 символов ')
    elif 0 < count_lowersece+count_the_capital:
     LP.text('нельзя русскиий ')
    else:
     LP.text('ваш пароль успешно создан ')

LP.markdown("<h1 style='text-align: center; color: green;'>Password game</h1>", unsafe_allow_html=True)
LP.markdown("<p style='text-align: center; color: black;'>""I am here to help you to create the strongest password in the world</p>", unsafe_allow_html=True)
pas = LP.text_input('введите пароль',value='',type="password")
#FINIK(pas)
if pas == '100572833':
    LP.text('ваш пароль успешно введён')
else:
    LP.text('ваш пароль не подходит')








