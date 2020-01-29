from DB_coverage.Stucture_matching import Structure_Matching_Coverage

# coding: utf-8
# Input: Smarts of scaffolds & Smarts of query compounds in DB (.txt)
# Output: The result of DB coverage calculation

# Define class
DB_matching = Structure_Matching_Coverage()

# DB coverage calculation #
# An example set for the DB coverage calculation: Specs DB
# (Data/QueryMols_DB_coverage_Specs.txt)

# Read data files
Scaffold_Lv0_FilePath = ('Data/Scaffold_List_Lv0.txt')
Scaffold_Lv1_FilePath = ('Data/Scaffold_List_Lv1.txt')
Scaffold_Lv2_FilePath = ('Data/Scaffold_List_Lv2.txt')
Scaffold_Lv3_FilePath = ('Data/Scaffold_List_Lv3.txt')
DB_qMol_FilePath = '(Data/QueryMols_DB_coverage_Specs.txt)'

#Scaffold_Lv0_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv0.txt'
#Scaffold_Lv1_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv1.txt'
#Scaffold_Lv2_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv2.txt'
#Scaffold_Lv3_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv3.txt'
#DB_qMol_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\QueryMols_DB_coverage_Specs.txt'

# Read qMol files
f = open(DB_qMol_FilePath , "r")
DB_qMols_Smarts = []

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    DB_qMols_Smarts.append(new_line[1])

# Count DB qMols
DB_qMol_count = len(DB_qMols_Smarts)
print(DB_qMol_count)
match_Lv0_count = 0
match_Lv1_count = 0
match_Lv2_count = 0
match_Lv3_count = 0
print('read DB_qMols')

# Calculate DB coverage (Scaffold_Lv0)
for ai in range (0, len(DB_qMols_Smarts)):
    try:
        match_Lv0_count = match_Lv0_count + DB_matching.match_All_Scaffold_Smarts(Scaffold_Lv0_FilePath, DB_qMols_Smarts[ai])
    except AttributeError as e:
        print(e)
coverage_Lv0 = (match_Lv0_count/DB_qMol_count) * 100

# Result of DB coverage (Scaffold_Lv0)
print(str('Scaffold_Lv0 DB coverage'))
print(str(coverage_Lv0)+str('%'))
print("")

# Calculate DB coverage (Scaffold_Lv1)
for ai in range (0, len(DB_qMols_Smarts)):
    try:
        match_Lv1_count = match_Lv1_count + DB_matching.match_All_Scaffold_Smarts(Scaffold_Lv1_FilePath, DB_qMols_Smarts[ai])
    except AttributeError as e:
        print(e)
coverage_Lv1 = (match_Lv1_count/DB_qMol_count) * 100

# Result of DB coverage (Scaffold_Lv1)
print(str('Scaffold_Lv1 DB coverage'))
print(str(coverage_Lv1)+str('%'))
print("")

# Calculate DB coverage (Scaffold_Lv2)
for ai in range (0, len(DB_qMols_Smarts)):
    try:
        match_Lv2_count = match_Lv2_count + DB_matching.match_All_Scaffold_Smarts(Scaffold_Lv2_FilePath, DB_qMols_Smarts[ai])
    except AttributeError as e:
        print(e)
coverage_Lv2 = (match_Lv2_count/DB_qMol_count) * 100

# Result of DB coverage (Scaffold_Lv2)
print(str('Scaffold Lv2 DB coverage'))
print(str(coverage_Lv2)+str('%'))
print("")

# Calculate DB coverage (Scaffold_Lv3)
for ai in range (0, len(DB_qMols_Smarts)):
    try:
        match_Lv3_count = match_Lv3_count + DB_matching.match_All_Scaffold_Smarts(Scaffold_Lv3_FilePath, DB_qMols_Smarts[ai])
        #print(match_Lv3_count)
    except AttributeError as e:
        print(e)
coverage_Lv3 = (match_Lv3_count/DB_qMol_count) * 100

# Result of DB coverage (Scaffold_Lv3)
print(str('Scaffold Lv3 DB coverage'))
print(str(coverage_Lv3)+str('%'))
print("")

