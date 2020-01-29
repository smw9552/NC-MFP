import itertools
from NC_MFP_Algorithm.Preprocessing_step import Preprocessing
from NC_MFP_Algorithm.Scaffold_matching_step import Scaffold_Matching
from NC_MFP_Algorithm.Fragment_list_generation_step import Fragment_List_Generation
from NC_MFP_Algorithm.SFCP_assigning_step import SFCP_Assigning
from NC_MFP_Algorithm.Fragment_identifying_step import Fragment_identifying
from NC_MFP_Algorithm.Fingerprint_representation_step import Fingerprint_representation

# coding: utf-8
# Input: Smarts of query compound (.txt)
# Output: NC-MFP bit string (.txt)

# NC-MFP calculation algorithm #
# An Example set for the NC-MFP calculation: 20 query compounds in NPASS DB
# ('Data/QueryMols_NC_MFP_Algorithm_TestSet.txt')

# Define classes
Step_1 = Preprocessing()
Step_2 = Scaffold_Matching()
Step_3 = Fragment_List_Generation()
Step_4 = SFCP_Assigning()
Step_5 = Fragment_identifying()
Step_6 = Fingerprint_representation()

# Read Query Mols data
Query_FilePath = ('Data/QueryMols_NC_MFP_Algorithm_TestSet.txt')
#Query_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\QueryMols_NC_MFP_Algorithm_TestSet.txt'

# Read All Scaffolds data
All_Scaffold_FilePath = ('Data/All_Optimized_Scaffold_List.txt')
#All_Scaffold_FilePath = 'C:\\Users\\Seomyungwon\\NC-MFP\\Data\\All_Optimized_Scaffold_List.txt'

# Write NC-MFP file
OutputFilePath = ('FilePath/OutPutFileName.txt')
OutputFileName = ('OutputFile name.txt')
#OutputFilePath = 'C:\\Users\\Seomyungwon\\Desktop\\Python_Test\\'
#OutputFileName = 'Test_Output.txt'

## NC-MFP algorithm steps ##

# [1] Preprocessing (Mol set) #
# Hydrogens of query compounds were added previously.
# Molecular weight (MW) and Molecular formula (MF) were calculated previously.
qMols_Smarts = Step_1.get_Query_Mols_Smarts(Query_FilePath)

# All fragments generation #
Final_all_Fragment_List = []
Final_all_Fragment_Dic = []

for qMol_Smart in qMols_Smarts:
    Final_all_Fragment_List.append(Step_3.generate_all_Fragment_List(All_Scaffold_FilePath, qMol_Smart))

# merge list
Final_all_Fragment_List = list(itertools.chain(*Final_all_Fragment_List))
# remove duplicated elements in list
Final_all_Fragment_List = list(set(Final_all_Fragment_List))
print(str('All fragments: ') + str(len(Final_all_Fragment_List)))

Final_all_Fragment_Dic = Step_3.generate_all_Fragment_Dictionary(Final_all_Fragment_List)
print("Query compounds: " + str(len(qMols_Smarts)))


Final_all_NC_MFP_Info = []
for ai in range (0, len(qMols_Smarts)):

    print("Input mol: " + str(ai+1))

    try:
        # [2] Scaffold matching step #
        Final_all_Scaffold_Match_List = []
        Final_all_Scaffold_Match_List.append(Step_2.match_All_Scaffold_Smarts(All_Scaffold_FilePath, qMols_Smarts[ai]))

        # Merge scaffold lists
        Final_all_Scaffold_Match_List = list(itertools.chain(*Final_all_Scaffold_Match_List))
        Final_all_Scaffold_Match_List = list(set(Final_all_Scaffold_Match_List))

    except IndexError as e:
        print(e)

    try:
        # [3] Fragment list generation & [4] Scaffold-Fragment Connection List(SFCP) assigning step #
        Final_all_SFCP_List = []
        Final_all_SFCP_List.append(Step_4.assign_All_SFCP_Smarts(All_Scaffold_FilePath, qMols_Smarts[ai]))
        Final_all_SFCP_List = list(itertools.chain(*Final_all_SFCP_List))

    except IndexError as e:
        print(e)

    try:
        # [5] Fragment identifying step #
        Final_qMol_Fragment_List = []
        Final_qMol_Fragment_List.append(Step_5.identify_Fragment_Smarts(All_Scaffold_FilePath, qMols_Smarts[ai], Final_all_Fragment_Dic))
        Final_qMol_Fragment_List = list(itertools.chain(*Final_qMol_Fragment_List))

        # merge NC-MFP info
        merge = Final_all_Scaffold_Match_List + Final_all_SFCP_List + Final_qMol_Fragment_List

        Final_all_NC_MFP_Info.append(merge)

    except IndexError as e:
        print(e)

try:
    # [6] Fingerprint representation step #
    # Get all NC-MFP label
    Final_all_NC_MFP_Label = []
    Final_all_NC_MFP_Label = Step_6.get_all_NC_MFP_Label(Final_all_NC_MFP_Info)

except IndexError as e:
    print(e)

try:
    # Get all NC-MFP Bit String
    Final_Bitstring = Step_6.get_qMol_NC_MFP_Value_Idx(Final_all_NC_MFP_Info, Final_all_NC_MFP_Label)

except IndexError as e:
    print(e)

try:
    # Write NC-MFP Bit String file (.txt)
    Step_6.represent_NC_MFP(OutputFilePath, OutputFileName, Final_Bitstring)
except IndexError as e:
    print(e)