import itertools

from Accuracy_of_Classification.Structure_matching import Structure_Matching_Classification

# coding: utf-8
# Input: Smarts of scaffolds & Smarts of representative query compounds in DNP (.txt)
# Output: The result of accuracy of classification

#Define class
Class_matching = Structure_Matching_Classification()

# Calculationof accuracy of classification #
# An exmaple set for the calculation: Flavonoid class compounds
# (Data/QueryMols_Accuracy_of_Classification_Flavonoid_class.txt)

# Read data files
Scaffold_Lv0_FilePath = ('Data/Scaffold_List_Lv0.txt')
Scaffold_Lv1_FilePath = ('Data/Scaffold_List_Lv1.txt')
Scaffold_Lv2_FilePath = ('Data/Scaffold_List_Lv2.txt')
Scaffold_Lv3_FilePath = ('Data/Scaffold_List_Lv3.txt')
Re_qMol_FilePath = '(Data/QueryMols_Accuracy_of_Classification_Flavonoid_class.txt)'

#Scaffold_Lv0_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv0.txt'
#Scaffold_Lv1_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv1.txt'
#Scaffold_Lv2_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv2.txt'
#Scaffold_Lv3_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\Scaffold_List_Lv3.txt'
#Re_qMol_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\QueryMols_Accuracy_of_Classification_Flavonoid_class.txt'

# DNP 16 classes list
DNP_List = ['ANP','Alk','Ape','Bfu','Bpy','Car','Fla','Lig','Oxy','PANP','Pke','Ppy','SANP','Ste','Tan','Ter']

# The number of representative compounds
Num_Re_qMols = [31, 303, 13, 11, 15, 30, 19, 20, 12, 13, 12, 6, 18, 17, 21, 141]

# Read representative qMol files
f = open(Re_qMol_FilePath, 'r')
Re_qMols_Smarts = []

while True:
    line = f.readline()
    if not line:break
    new_line = line.split("\t")
    Re_qMols_Smarts.append(new_line[1])

Matched_Lv0_classes = []
Matched_Lv1_classes = []
Matched_Lv2_classes = []
Matched_Lv3_classes = []


# Calculation of accuarcy of classification (Scaffold_Lv0)
for ai in range (0, len(Re_qMols_Smarts)):
    Matched_Lv0_classes.append(Class_matching.match_All_Scaffold_Smarts(Scaffold_Lv0_FilePath, Re_qMols_Smarts[ai]))

Matched_Lv0_classes = list(itertools.chain(*Matched_Lv0_classes))

Matched_Lv0_proportion = []
for bi in range (0, len(DNP_List)):

    Matched_Lv0_proportion.append(round(Matched_Lv0_classes.count(DNP_List[bi])/Num_Re_qMols[bi],3))

# Result of accuracy of classification (Scaffold_Lv0)
print("Matched_Lv0_proportion")
print(DNP_List)
print(Matched_Lv0_proportion)
print("")


# Calculation of accuarcy of classification (Scaffold_Lv1)
for ai in range (0, len(Re_qMols_Smarts)):
    Matched_Lv1_classes.append(Class_matching.match_All_Scaffold_Smarts(Scaffold_Lv1_FilePath, Re_qMols_Smarts[ai]))

Matched_Lv1_classes = list(itertools.chain(*Matched_Lv1_classes))

Matched_Lv1_proportion = []
for bi in range (0, len(DNP_List)):

    Matched_Lv1_proportion.append(round(Matched_Lv1_classes.count(DNP_List[bi])/Num_Re_qMols[bi],3))

# Result of accuracy of classification (Scaffold_Lv1)
print("Matched_Lv1_proportion")
print(DNP_List)
print(Matched_Lv1_proportion)
print("")

# Calculation of accuarcy of classification (Scaffold_Lv2)
for ai in range (0, len(Re_qMols_Smarts)):
    Matched_Lv2_classes.append(Class_matching.match_All_Scaffold_Smarts(Scaffold_Lv2_FilePath, Re_qMols_Smarts[ai]))

Matched_Lv2_classes = list(itertools.chain(*Matched_Lv2_classes))

Matched_Lv2_proportion = []
for bi in range (0, len(DNP_List)):

    Matched_Lv2_proportion.append(round(Matched_Lv2_classes.count(DNP_List[bi])/Num_Re_qMols[bi],3))

# Result of accuracy of classification (Scaffold_Lv2)
print("Matched_Lv2_proportion")
print(DNP_List)
print(Matched_Lv2_proportion)
print("")


# Calculation of accuarcy of classification (Scaffold_Lv3)
for ai in range (0, len(Re_qMols_Smarts)):
    Matched_Lv3_classes.append(Class_matching.match_All_Scaffold_Smarts(Scaffold_Lv3_FilePath, Re_qMols_Smarts[ai]))

Matched_Lv3_classes = list(itertools.chain(*Matched_Lv3_classes))

Matched_Lv3_proportion = []
for bi in range (0, len(DNP_List)):

    Matched_Lv3_proportion.append(round(Matched_Lv3_classes.count(DNP_List[bi])/Num_Re_qMols[bi],3))

#Result of accuracy of classification (Scaffold_Lv3)
print("Matched_Lv3_proportion")
print(DNP_List)
print(Matched_Lv3_proportion)


