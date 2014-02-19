import gdata.docs.data
import gdata.docs.client
import gdata.docs.service
import gdata.spreadsheet.service
import re, os
import socket
import logging
import atom.service
import gdata.service
import gdata.spreadsheet
import gdata.spreadsheet.text_db

username        = 'YOUR_EMAIL'
password        = 'PASSWORD'
doc_name        = 'NAME_OF_FILE'
column_title      = 'COLUMN_TITLE' 

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

col = -1

for cell in cells:
    if cell.content.text == column_title:
        col = cell.cell.col
    if cell.cell.col == col:
        print cell.content.text

