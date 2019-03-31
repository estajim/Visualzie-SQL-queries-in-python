from Main import VConnect
import sqlite3
conn=sqlite3.connect('chinook.db')
c=conn.cursor()
q1='''SELECT invoice_items.Quantity From tracks 
inner join invoice_items on tracks.Trackid=invoice_items.Trackid where tracks.Unitprice > 0.00001'''
q2='''SELECT distinct genres.Name, tracks.Unitprice from tracks inner join genres on genres.GenreId=tracks.GenreId
order by tracks.Unitprice desc'''
q3='''
SELECT genres.Name,AVG(Milliseconds)
FROM
tracks
INNER JOIN genres
ON
genres.GenreId=tracks.GenreId
GROUP BY genres.Name
HAVING
COUNT(tracks.Name)>100
ORDER BY Milliseconds DESC
'''

estajim=VConnect(c)
print(estajim.run_query(q1,3))
print(estajim.run_query(q2,5))
print(estajim.run_query(q3,5))
