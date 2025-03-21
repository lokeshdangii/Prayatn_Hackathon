from flask import Flask, render_template, request, redirect, url_for, send_file
import mysql.connector
import random

# ---------------------------------------------------
def create_table(column_detail, table_name):

    # splitting column_detail by ","
    column_list = column_detail.split(",")

    # list to store the column details after splitting by ":"
    column_detail_list = []

    # splitting each column by ":" and storing in column_detail_list
    for column in column_list:
        s = column.split(":")
        column_detail_list.append(s)
    column_detail_list.append(['timestamp', 'timestamp'])

    # MySQL create table query
    query = f"CREATE TABLE {table_name} ("

    # iterating through the list of column details
    for column_info in column_detail_list:
        # Iterating through the inner list
        for detail in column_info:
            query += f" {detail}"
        if column_info != column_detail_list[-1]:
            query += ","

    # ending part of query
    query += ");"

    # returning the MySQL create table query
    return query
