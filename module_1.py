from IPython.display import display
import pandas as pd
a = pd.read_csv('C:/python/movie_bd_v5.csv')

# 1. У какого фильма из списка самый большой бюджет?"
s1 = a['budget'].max()
d1 = a.loc[a.budget == s1]
display(d1['original_title'])

# 2.Какой из фильмов самый длительный (в минутах)?
s2 = a['runtime'].max()
d2 = a.loc[a.runtime == s2]
display(d2['original_title'])

# 3. Какой из фильмов самый короткий (в минутах)?
s3 = a['runtime'].min()
d3 = a.loc[a.runtime == s3]
display(d3['original_title'])

# 4. Какова средняя длительность фильмов?
d4 = a['runtime'].mean()
display(d4)

# 5. Каково медианное значение длительности фильмов?
d5 = a['runtime'].median()
display(d5)

# 6. Какой самый прибыльный фильм?
a6 = a.assign(profit = a.revenue - a.budget)
s6 = a6['profit'].max()
d6 = a6.loc[a6.profit == s6]
display(d6['original_title'])

#7. Какой фильм самый убыточный?
a7 = a.assign(profit = a.revenue - a.budget)
s7 = a7['profit'].min()
d7 = a7.loc[a7.profit == s7]
display(d7['original_title'])

# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
a8 = a.assign(profit = a.revenue - a.budget)
d8 = a8.loc[a8.profit > 0]
display(len(d8.index))

# 9. Какой фильм оказался самым кассовым в 2008 году?
a9 = a[a.release_year == 2008]
s9 = a9['revenue'].max()
d9 = a9.loc[a9.revenue == s9]
display(d9['original_title'])

# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
b = a[(a.release_year <= 2014) & (a.release_year >= 2012)]
a10 = b.assign(profit = a.revenue - a.budget)
s10 = a10['profit'].min()
d10 = a10.loc[a10.profit == s10]
display(d10['original_title'])

# 11. Какого жанра фильмов больше всего?"

s11 = a['genres'].value_counts()
display(s11.index[0])

# 12. Фильмы какого жанра чаще всего становятся прибыльными?
b = a.assign(profit = a.revenue - a.budget)
a12 = b[(b.profit > 0)]
s12 = a12['genres'].value_counts()
display(s12.index[0])

# 13. У какого режиссера самые большие суммарные кассовые сборы?
s13 = a.groupby(['director'])['revenue'].sum().sort_values(ascending=False)
display(s13.index[0])



# 14. Какой режиссер снял больше всего фильмов в стиле Action?"

a14 = a[a.genres == 'Action']
s14 = a14.groupby(['director'])['genres'].sum().sort_values(ascending=False)
display(s14.index[0])

# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?



# 18Самый убыточный фильм от Paramount Pictures?

b = a.assign(profit = a.revenue - a.budget)
a18 = b[b.production_companies == 'Paramount Pictures']
s18 = a18['profit'].min()
d18 = a18.loc[a18.profit == s18]
display(d18['original_title'])

# 19. Какой год стал самым успешным по суммарным кассовым сборам?
s19 = a.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False)
display(s19.index[0])

# 20. Какой год стал самым успешным по суммарным кассовым сборам?
b = a.assign(profit = a.revenue - a.budget)
a20 = b[b.production_companies == 'Warner Bros']
s20 = a20.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(a20)