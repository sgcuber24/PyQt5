# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 20:28:48 2018

@author: G Sriram
"""

import mysql.connector

def addStudent(a):
  mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="students"
  )
  
  mycursor = mydb.cursor()
  
  mycursor.execute("CREATE DATABASE IF NOT EXISTS students")
  
  mycursor.execute("CREATE TABLE IF NOT EXISTS STUDLIST(NAME VARCHAR(100), REG_NO VARCHAR(10) PRIMARY KEY, PH_NO VARCHAR(10), EMAIL VARCHAR(200))")

  sql="INSERT INTO STUDLIST(NAME, REG_NO, PH_NO, EMAIL) VALUES(%s, %s, %s, %s)"
  mycursor.execute(sql,a)
  mydb.commit()

def searchStudent(reg_no):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="students"
  )
  mycursor = mydb.cursor()
  sql="SELECT NAME, PH_NO, EMAIL FROM STUDLIST WHERE REG_NO = %s"
  mycursor.execute(sql,(reg_no,))
  for x in mycursor:
    return x

def modifyStudent(reg_no,a):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="students"
  )
  
  mycursor = mydb.cursor()

  sql="UPDATE STUDLIST SET NAME=%s, REG_NO=%s, PH_NO=%s, EMAIL=%s WHERE REG_NO=%s"
  mycursor.execute(sql,(a+[reg_no]))
  mydb.commit()
  
def deleteStudent(reg_no):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toor",
  database="students"
  )
  
  mycursor = mydb.cursor()

  sql="DELETE FROM STUDLIST WHERE REG_NO=%s"
  mycursor.execute(sql,(reg_no,))
  mydb.commit()
      
