import json
from re import search
import xlrd
import os
import csv
import copy

import xmlrpc.client

url = 'https://enero-technical-training-16-0-odoo-academy-7134304.dev.odoo.com/'
db = 'enero-technical-training-16-0-odoo-academy-7134304'
username = 'admin'
password = 'admin'

EXCEL_DIR = 'sample.xlsx'
SHEET_NAME = 'Courses'
CURR_ROW_FILE = os.getcwd() + '/data.json'
PROBLEM_ROWS_FILE = os.getcwd() + '/issues.csv'

memo_courses = []

def main():

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    print('after uid')
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    print(uid)
    print(models)
    execute_kw = execute_factory(models, db, uid, password)

    workbook = xlrd.open_workbook(EXCEL_DIR)
    sheet = workbook.sheet_by_name(SHEET_NAME)
    num_courses = sheet.nrows

    print('Opened Excel File Successfully')
    print(num_courses)
    
    fields = [r.value for r in sheet.row(0)if r.value != '']
    print(fields)
    course_start_row = get_current_row(CURR_ROW_FILE)
    course_vals = []
    
    for i in range(course_start_row, num_courses):
        try:
            if (i+1) % 10 == 0 and i != course_start_row :
                print(course_vals)
                create_course_records(execute_kw, course_vals[-10:])
                save_current_row(CURR_ROW_FILE, {'course_start_row': i})
                print(f'Imported course for {i}/{num_courses} courses')
            
            raw_vals = [r.value for r in sheet.row(i)]
            course_vals.append(format_course_record(execute_kw, fields, raw_vals, i))

        except Exception as e:
            print(str(e))
            print(f'problematic row: {i}')
            save_problem_rows(PROBLEM_ROWS_FILE, i)
            continue

    
    return

def format_course_record(execute_kw, fields, vals, index):
    vals_dict = {}
    vals_dict['index'] = index
    for i, field in enumerate(fields):
        vals[i] = str(vals[i])

        if vals[i].isspace() or vals[i] == '':
            continue
        if field == 'External ID':
            continue
        elif field == 'level':
            if vals[i] == 'Beginner':
                vals_dict['level'] = 'beginner'
            elif vals[i] == 'Intermediate':
                vals_dict['level'] = 'intermediate'
            elif vals[i] == 'Advanced':
                vals_dict['level'] = 'advanced'
        else:
            vals_dict[field] = vals[i]

    if all(val == '' or val.isspace() for val, __ in vals_dict.items()):
        return {}

    return vals_dict

def create_course_records(execute_kw, vals):
    recs_to_create = []
    recs_to_write = []
    for val_dict in vals:
        courses = search_existing_course(val_dict.get('name'))
        print(courses)

        if courses:
            recs_to_write.append((courses.get('id'), val_dict))
        else:
            recs_to_create.append(val_dict)
    try:
        for rec in recs_to_create:
            del rec['index']
        execute_kw('academy.course', 'create', [recs_to_create])
        
        for rec_id, rec in recs_to_write:
            del rec['index']
            try:
                execute_kw('academy.course', 'write', [int(rec_id), rec])
            except Exception as e:
                print(str(e))
                print(rec_id)
    except Exception as e:
        print(str(e))

def search_existing_course(name):
    index = next((i for i, record in enumerate(memo_courses) if record.get('name') == name), False)
    return memo_course[index] if index else None

def get_current_row(filename):
    with open(filename) as f:
        data = json.load(f)
        return data.get('course_start_row', 1)
    
def save_current_row(filename, new_data):
    with open(filename, 'r+') as f:
        data = json.load(f)
        f.seek(0)
        data.update(new_data)
        json.dump(data, f)

def save_problem_rows(filename, i):
    with open(filename, 'a') as f:
        f.write(str(i) + ',')

        
def execute_factory(models, db, uid, password):
    def execute(model_name, function, domain, options={}):
        return models.execute_kw(db, uid, password, model_name, function, domain, options)
    return execute

if __name__ == '__main__':
    main()