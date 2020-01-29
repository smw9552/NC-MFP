from rdkit import Chem

class Structure_Matching_Coverage:

    def match_All_Scaffold_Smarts(self, Scaffold_FilePath, DB_qMol_Smarts):

        S_all_Smarts = []
        matched = []
        f = open(Scaffold_FilePath, "r")

        while True:
            line  = f.readline()
            if not line:break
            new_line = line.split("\t")
            S_all_Smarts.append(new_line[1])

        for ai in range (0, len(S_all_Smarts)):

            qMol = Chem.MolFromSmarts(DB_qMol_Smarts)

            if qMol.HasSubstructMatch(Chem.MolFromSmarts(S_all_Smarts[ai])):
                matched.append('1')
                break

        return len(matched)


