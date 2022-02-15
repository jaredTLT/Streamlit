import streamlit as st
import os

def main():
	
	st.subheader("Dataset")
	data_file=st.file_uploader("Upload MDB",type=["mdb"])
		
	if data_file is not None:

		file_details = {"filename":data_file.name, "filetype":data_file.type,
                            "filesize":data_file.size}
		st.write(file_details)
	def Getrows():
 		arr=[]
		for row in cursor.tables():
        	#print(row[2])
       			if 'T7' in row[2]:
            			arr.append(row[2])
    				return arr
	def getFirstCol(name):
		return cursor.columns(table=name).fetchall()[0].column_name


	def getLastCol(name):
	   	return cursor.columns(table=name).fetchall()[-1].column_name


	def getVuserTable():
		for row in Getrows(): 
			if getLastCol(row) =="Event Name" and getFirstCol(row)=='Minimum':
		    	#print(f'SELECT * FROM {row}')
		    	return cursor.execute(f'SELECT*FROM {row}')

	conn=pyodbc.connect(data_file)
	cursor = conn.cursor()
	getVuserTable()

if __name__ == '__main__':
	main()
