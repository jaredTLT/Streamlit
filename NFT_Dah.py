import streamlit as st
import os
import pyodbc

def main():
	
	st.subheader("Dataset")
	data_file=st.file_uploader("Upload MDB",type=["mdb"])
		
	if data_file is not None:

		file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
		conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+data_file.name)
		cursor = conn.cursor()
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

	#conn=pyodbc.connect(data_file)
	getVuserTable()

if __name__ == '__main__':
	main()

