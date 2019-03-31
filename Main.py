import sqlite3, pandas as pd, numpy as np,re
class VConnect:
    def __init__(self,connection):
        self.c=connection

    def disp_headers(self,my_table):
        q=self.c.execute("SELECT * FROM "+my_table)
        return [row[0] for row in list(q.description)]
    def save_csv(self,df,name):
        return df.to_csv(name+'.csv')
    def run_query(self,query,n):
        cur=self.c.execute(query)
        if "*" in query:
            tableName=re.findall(r'[f|F][r|R][o|O][m|M]\s*\n*\s*(\w+)',query)[0]
            names=self.disp_headers(tableName)
        else:
            portion=re.findall(r'((.*\n)*.*)[f|F][r|R][o|O][m|M]',query)
            try:
                sp=portion[0][0].split(',')
                names=[]
                for item in sp:
                    names.append(re.findall(r'(\w+\.?\w+)',item)[-1])
            except IndexError:
                names=re.findall(r'\s+(\w+)\s+\s*\n*\s*[f|F][r|R][o|O][m|M]',query)
        rows=cur.fetchall()
        rows_list=[]
        for row in rows:
            rows_list.append(list(row))
        query_array=np.asarray(rows_list)
        print("Query resulted in {} rows".format(len(rows)))
        df=pd.DataFrame(data=query_array)
        df.columns=names
        if n in ['all','All','ALL']:
            print("All rows are:".format(n))
            return df
        else:
            print("First {} rows are:".format(n))
            return df.head(n)
