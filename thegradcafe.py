#Read thegradcafe.csv and write a json file of gpa, gre scores and application \
#results weighted by school ranking.
#Data downloaded from https://github.com/evansrjames/gradcafe-admissions-data.
import csv
import json
import pandas

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

gpa=[]
v=[]
q=[]
w=[]
p=[]
schools=[]
decision=[]
result=[]
new_results=[]
with open("ranking.json", "r") as rank:
    rank_dic=json.load(rank)
with open('thegradcafe.csv', mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if is_float(row[6])==True:
            school=row[0].split("(")[0].strip()           
            for same_school in list(rank_dic.values()):
                if row[3].strip()=="Accepted" and school in same_school:
                    no=list(rank_dic.values()).index(same_school)
                    rank=int(list(rank_dic.keys())[no].split("-")[0])
                    if float(row[6])<=5.0 and float(row[6])>=2.0:
                        gpa.append((float(row[6])-2.00)/2.00)
                    else:
                        gpa.append(0)
                    if int(row[7])<=170 and int(row[7])>=130:
                        v.append((int(row[7])-130)/40)
                    else:
                        v.append(0)
                    if int(row[8])<=170 and int(row[8])>=130:
                        q.append((int(row[8])-130)/170)
                    else:
                        q.append(0)
                    if float(row[9])<=6.0 and float(row[9])>=0:
                        w.append(float(row[9])/6.0)
                    else:
                        w.append(0)
                    if row[10][-3:]!="n/a" and int(row[10][-3:])>=200:
                        p.append((int(row[10][-3:])-200)/790)
                    else:
                        p.append(0)
                    schools.append(school)
                    decision.append(row[3].strip())
                    result.append(100-rank)
                    break
                elif row[3].strip()=="Interview" and school in same_school:
                    no=list(rank_dic.values()).index(same_school)
                    rank=int(list(rank_dic.keys())[no].split("-")[0])
                    if float(row[6])<=5.0 and float(row[6])>=2.0:
                        gpa.append((float(row[6])-2.00)/2.00)
                    else:
                        gpa.append(0)
                    if int(row[7])<=170 and int(row[7])>=130:
                        v.append((int(row[7])-130)/40)
                    else:
                        v.append(0)
                    if int(row[8])<=170 and int(row[8])>=130:
                        q.append((int(row[8])-130)/170)
                    else:
                        q.append(0)
                    if float(row[9])<=6.0 and float(row[9])>=0:
                        w.append(float(row[9])/6.0)
                    else:
                        w.append(0)
                    if row[10][-3:]!="n/a" and int(row[10][-3:])>=200:
                        p.append((int(row[10][-3:])-200)/790)
                    else:
                        p.append(0)
                    schools.append(school)
                    decision.append(row[3].strip())
                    result.append(50-rank/2)
                    break
                elif row[3].strip()=="Wait listed" and school in same_school:
                    no=list(rank_dic.values()).index(same_school)
                    rank=int(list(rank_dic.keys())[no].split("-")[0])
                    if float(row[6])<=5.0 and float(row[6])>=2.0:
                        gpa.append((float(row[6])-2.00)/2.00)
                    else:
                        gpa.append(0)
                    if int(row[7])<=170 and int(row[7])>=130:
                        v.append((int(row[7])-130)/40)
                    else:
                        v.append(0)
                    if int(row[8])<=170 and int(row[8])>=130:
                        q.append((int(row[8])-130)/170)
                    else:
                        q.append(0)
                    if float(row[9])<=6.0 and float(row[9])>=0:
                        w.append(float(row[9])/6.0)
                    else:
                        w.append(0)
                    if row[10][-3:]!="n/a" and int(row[10][-3:])>=200:
                        p.append((int(row[10][-3:])-200)/790)
                    else:
                        p.append(0)
                    schools.append(school)
                    decision.append(row[3].strip())
                    result.append(25-rank/4)
                    break
                elif (row[3].strip()=="Rejected" and school in same_school) or\
                     (row[3].strip()=="Other" and school in same_school):
                    no=list(rank_dic.values()).index(same_school)
                    rank=int(list(rank_dic.keys())[no].split("-")[0])
                    if float(row[6])<=5.0 and float(row[6])>=2.0:
                        gpa.append((float(row[6])-2.00)/2.00)
                    else:
                        gpa.append(0)
                    if int(row[7])<=170 and int(row[7])>=130:
                        v.append((int(row[7])-130)/40)
                    else:
                        v.append(0)
                    if int(row[8])<=170 and int(row[8])>=130:
                        q.append((int(row[8])-130)/170)
                    else:
                        q.append(0)
                    if float(row[9])<=6.0 and float(row[9])>=0:
                        w.append(float(row[9])/6.0)
                    else:
                        w.append(0)
                    if row[10][-3:]!="n/a" and int(row[10][-3:])>=200:
                        p.append((int(row[10][-3:])-200)/790)
                    else:
                        p.append(0)
                    schools.append(school)
                    decision.append(row[3].strip())
                    result.append(10-rank/10)
                    break
print(len(gpa))
print(len(v))
print(len(q))
print(len(w))
print(len(p))
print(len(schools))
print(len(decision))
print(len(result))
list1=[gpa, v, q, w, p, schools, decision, result]
with open("thegradcafe.json", "w") as nf:
    json.dump(list1, nf, indent=4)
