import pymysql
import pymysql.cursors
conn=pymysql.connect(host='localhost',user='root',password='12345678',db='mohan')
a=conn.cursor()
sql='select max(id) from nametable;'

k=raw_input()
b=str(k)
c=a.execute(sql)

d=a.fetchone()[0]+1

print(b)
sql1 = 'INSERT INTO nametable(id,name,no) VALUES (7,b, 20);'
p=a.execute(sql1)
# conn.commit()
print(p)
 #a.execute("""INSERT INTO nametable (id, name, no) VALUES ("%d", "%s", "%d");""" % (b, singh,5))
#k=int(Id)
            #a.execute('select name from nametable where id=%s',(k))
            #print(a.fetchone())
            #name1=str(a.fetchone()[0])
