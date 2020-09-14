import os
import csv
import sys

def trim(result_file, row):
    if len(row[1])<=0:
        return
    #row[1] = trim_jquery(row[1])
    try:
        if row[1][0] == '\"':
            row[1] = row[1][1:]
            row[1] = row[1][:-1]
    except:
        print(row)
        exit(-1)

    if isEnglishOrKorean(row[1]):
        if len(row[1]) < 140:
            result_file.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\n')
            return True
    return False

def trim_jquery(input_s):
    if 'jQuery' in input_s:
        line = input_s.split('jQuery')

        underbar_count=True
        for c in line[1]:
            if c.isdigit():
                line[1] = line[1][1:]
            elif c == '_' and underbar_count:
                line[1] = line[1][1:]
                underbar_count = False
            else:
                break
        input_s = line[0] + line[1]
    return input_s


def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count+=1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count+=1

    if k_count+e_count == 0:
        return False
    elif k_count/(k_count+e_count)>=0.8:
        return True
    else:
        return False

if(__name__=="__main__"):
    result = '19_trim.txt'
    tran = '19_review.txt'

    try:
        result_file = open(result,'w')
    except:
        result_file = creat(result,644)

    with open(tran,encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for line in reader:
            if trim(result_file,line):
                counter+=1
    result_file.close()

