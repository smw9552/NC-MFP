from collections import OrderedDict
import itertools


class Fingerprint_representation:

    def get_all_NC_MFP_Label(self, Final_all_NC_MFP_Info):

        Final_all_NC_MFP_Label = []

        Final_NC_MFP_BitString = list(itertools.chain(*Final_all_NC_MFP_Info))

        for ai in range (0, len(Final_NC_MFP_BitString)):
            Final_all_NC_MFP_Label.append(Final_NC_MFP_BitString[ai])

        Final_all_NC_MFP_Label = list(OrderedDict.fromkeys(Final_all_NC_MFP_Label))
        Final_all_NC_MFP_Label.sort()

        return Final_all_NC_MFP_Label


    def get_qMol_NC_MFP_Value(self, Final_all_NC_MFP_Info, Final_all_NC_MFP_Label):

        Final_qMol_NC_MFP_Value = []
        Final_qMOl_NC_MFP_Value_String = ""

        for i in range (0, len(Final_all_NC_MFP_Label)):
            Final_qMOl_NC_MFP_Value_String = Final_qMOl_NC_MFP_Value_String  + str(Final_all_NC_MFP_Label[i]) + "\t"
        Final_qMOl_NC_MFP_Value_String  = Final_qMOl_NC_MFP_Value_String + "\n"

        for qMol_NC_MFP_Info in Final_all_NC_MFP_Info:
            for ai in range(0, len(Final_all_NC_MFP_Label)):

                if qMol_NC_MFP_Info.__contains__(Final_all_NC_MFP_Label[ai]):
                    Final_qMol_NC_MFP_Value.append('1')
                else:
                    Final_qMol_NC_MFP_Value.append('0')

            for bi in range(0, len(Final_qMol_NC_MFP_Value)):
                Final_qMOl_NC_MFP_Value_String = Final_qMOl_NC_MFP_Value_String + str(Final_qMol_NC_MFP_Value[bi]) + "\t"
            Final_qMOl_NC_MFP_Value_String  = Final_qMOl_NC_MFP_Value_String + "\n"

            #Initialize
            Final_qMol_NC_MFP_Value = []

        return Final_qMOl_NC_MFP_Value_String

    def represent_NC_MFP(self, OutputFilePath, OutputFileName, Final_BitString):

        file = open(OutputFilePath + OutputFileName, 'w')

        file.write(Final_BitString)
        file.close()


    def get_qMol_NC_MFP_Value_Idx(self, Final_all_NC_MFP_Info, Final_all_NC_MFP_Label):

        Final_qMol_NC_MFP_Value = []
        Final_qMOl_NC_MFP_Value_String = ""

        for i in range (0, len(Final_all_NC_MFP_Label)):
            Final_qMOl_NC_MFP_Value_String = Final_qMOl_NC_MFP_Value_String + str(Final_all_NC_MFP_Label[i]) + "\t"
        Final_qMOl_NC_MFP_Value_String  = Final_qMOl_NC_MFP_Value_String + str('NC-MFP_BitString') + "\n"

        for Info in range (0, len(Final_all_NC_MFP_Info)):
            for ai in range(0, len(Final_all_NC_MFP_Label)):

                if Final_all_NC_MFP_Info[Info].__contains__(Final_all_NC_MFP_Label[ai]):
                    Final_qMol_NC_MFP_Value.append('1')
                else:
                    Final_qMol_NC_MFP_Value.append('0')

            for bi in range(0, len(Final_qMol_NC_MFP_Value)):
                Final_qMOl_NC_MFP_Value_String = Final_qMOl_NC_MFP_Value_String + str(Final_qMol_NC_MFP_Value[bi]) + "\t"
            Final_qMOl_NC_MFP_Value_String  = Final_qMOl_NC_MFP_Value_String + str('QueryMol_')+ str(Info+1) + "\n"

            #Initialize
            Final_qMol_NC_MFP_Value = []

        return Final_qMOl_NC_MFP_Value_String