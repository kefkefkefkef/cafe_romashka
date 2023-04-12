import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


st.write("""
# Сумма заказа и чаевые нашего замечательного кафе


### Июнь 2021
Сегодня мы посмотрим на данные, которые удалось собрать нашим ребятам из маркетингового отдела за последний месяц работы.
Ниже - таблица с полными данными по основным показателям нашего кафе за июнь.
""")


tips = pd.read_csv('tips.csv')
tips = tips.drop(labels ='Unnamed: 0', axis= 1)
#tips.rename(columns={'total_bill': 'Общий чек', 'tip': "Чаевые", 'sex': 'Пол', ''})
st.dataframe(tips)

st.write("""
За 30 дней у нас побывало ***244!*** семьи, что довольно-таки немало для нашего небольшого кафе.
""")

fig1 , ax1 = plt.subplots()
sns.histplot(tips, x='total_bill', ax = ax1)
plt.ylabel('Количество заказов')
plt.xlabel('Сумма чека, $')
plt.title('Распределение размера заказа')
st.pyplot(fig1)

st.write("""
Самое первое, на что мы взглянем - это **сумма чека**. Это очень важный показатель для любого ресторана, и мы в данном случае - не исключение. \n
Чаще всего к нам заходят и оставляют в районе 15 долларов. Однако, средний чек у нас значительно выше. На графике хорошо видно смещение в сторону ***более высокой суммы чека***.

""")

from pandas.api.types import CategoricalDtype
days_of_week_order = CategoricalDtype(
    ['Thur', 'Fri', 'Sat', 'Sun'],
    ordered=True
)
tips['day'] = tips['day'].astype(days_of_week_order)
st.write("""
### Разбивка по дням недели
Взглянем на средние значения по кадому из дней:
""")
fig2, ax2 = plt.subplots()
sns.boxplot(tips, x='day', y='total_bill', palette='pastel', ax= ax2)
plt.ylabel('Общий чек, $')
plt.xlabel('День недели')
plt.title('Общий чек по дням недели')
st.pyplot(fig2)
st.write("""
Как Вы можете видеть, средний чек на выходных - **больше**. Это объясняется концом рабочей недели - люди к нам чаще приходят отдохнуть.
""")
fig5, ax5 = plt.subplots(2,2, sharey = True, sharex = True)
sns.scatterplot(data=tips.loc[tips['day'] == 'Thur'], x="total_bill", y="tip", hue="time", legend = False, palette=['#5f94ae', '#fbaba5'], ax= ax5[0,0]).set(title='Четверг')
sns.scatterplot(data=tips.loc[tips['day'] == 'Fri'], x="total_bill", y="tip", hue="time", legend = 'full', palette=['#5f94ae', '#fbaba5'], ax= ax5[0,1]).set(title='Пятница')
sns.scatterplot(data=tips.loc[tips['day'] == 'Sat'], x="total_bill", y="tip", hue="time", legend = False, palette=['#5f94ae', '#fbaba5'], ax= ax5[1,0]).set(title='Суббота')
sns.scatterplot(data=tips.loc[tips['day'] == 'Sun'], x="total_bill", y="tip", hue="time", legend = False, palette=['#5f94ae', '#fbaba5'], ax= ax5[1,1]).set(title='Воскресенье')
ax5[0,0].set(xlabel = 'Общий чек, $', ylabel = 'Чаевые, $')
ax5[0,1].set(xlabel = 'Общий чек, $', ylabel = 'Чаевые, $')
ax5[1,0].set(xlabel = 'Общий чек, $', ylabel = 'Чаевые, $')
ax5[1,1].set(xlabel = 'Общий чек, $', ylabel = 'Чаевые, $')
plt.tight_layout()
st.pyplot(fig5)
st.write("""
На выходных выше не только средний чек, но и **значительно растет число гостей**. В пятницу почему-то успех имеют лишь ланчи. В остальные дни - люди **чаще приходят вечером**. \n
В субботу **больше крупных заказов**, а люди  более склонны оставлять щедрые чаевые.
""")
         
st.write("""
### Демография
""")
fig7, ax7 = plt.subplots()
hue_order1 = ['Male', 'Female']
sns.barplot(tips.groupby(['day', 'sex'], as_index=False).agg({'total_bill': 'mean'}), x='day', y='total_bill', hue='sex', hue_order=hue_order1, palette=['navy', 'fuchsia'], ax= ax7)
plt.title('Размер общего чека для женщин и мужчин')
plt.ylabel('Общий чек, $')
plt.xlabel('День недели')
st.pyplot(fig7)

st.write("""
Заметна разница в среднем чеке между полами в пользу мужчин. Но если на буднях женщины склонны платить существенно меньше, чем мужчины,\n
 то **на выходных** - **разницы практически нет**.
""")



#tips_by_sex = tips.groupby(['day', 'sex'], as_index=False).agg({'tip':'mean'})
fig3, ax3 = plt.subplots()

sns.scatterplot(tips, x='total_bill', y='tip', hue='sex', hue_order=hue_order1, palette=['teal', 'violet'], ax = ax3)
plt.title('Чаевые от женщин и мужчин')
plt.ylabel('Чаевые, $')
plt.xlabel('Общий чек, $')
st.pyplot(fig3)
st.write("""
Что касается чаевых, то мужчины чаще оказываются более щедрыми. Существует негативная тенденция - оба пола чаще склонны **сэкономить на чаевых**. Даже заказав большое количество позиций, их чаевые могут ограничиться 6 долларами - это все точки в нижней правой части графика.
""")


# fig4, ax4 = plt.subplots()
# sns.boxplot(tips, x='day', y='total_bill', hue='time', ax=ax4)
# st.pyplot(fig4)

