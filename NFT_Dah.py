import streamlit as st
import os
import pyodbc
import tempfile
import io
	
st.subheader("Dataset")
data_file=st.file_uploader("Upload MDB",type=["mdb"])
conn=""
if data_file is not None:

	file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
	st.write(file_details)
	
def getFirstCol(name):
	return cursor.columns(table=name).fetchall()[0].column_name


def getLastCol(name):
	return cursor.columns(table=name).fetchall()[-1].column_name


def getVuserTable():
	for row in Getrows(): 
		if getLastCol(row) =="Event Name" and getFirstCol(row)=='Minimum':
			return cursor.execute(f'SELECT*FROM {row}')
def Getrows():
	arr=[]
	for row in cursor.tables():
        	#print(row[2])
		if 'T7' in row[2]:
        		arr.append(row[2])
	return arr

#file = io.StringIO(data_file)
for row in data_file:
	st.write(row.decode('UTF-8').strip())
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+data_file.name+';')
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+data_file.name+';')
#conn=pyodbc.connect(data_file)
#cursor = conn.cursor()
getVuserTable()



