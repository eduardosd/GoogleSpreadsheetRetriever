import gdata.spreadsheet.service
import re, os
import gdata.service
import gdata.spreadsheet
import gdata.spreadsheet.text_db

def printCells(title, cells):
    col = -1
    for cell in cells:
        if cell.content.text == title:
            col = cell.cell.col
        if cell.cell.col == col:
            print cell.content.text    
    print
    return

username           = 'YOUR_EMAIL'
password           = 'PASSWORD'
doc_name           = 'YOUR_FILE_NAME'
column_title_list  = ['TITLE_OF_COLUMN1', 'TITLE_OF_COLUMN2']

gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = username
gd_client.password = password
gd_client.source = 'com.spreadsheet'
gd_client.ProgrammaticLogin()

q = gdata.spreadsheet.service.DocumentQuery()
q['title'] = doc_name
q['title-exact'] = 'true'
feed = gd_client.GetSpreadsheetsFeed(query=q)
spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

cells = gd_client.GetCellsFeed(spreadsheet_id, worksheet_id).entry

for column_title in column_title_list:
    printCells(column_title, cells)
