from rdkit import Chem

class Structure_Matching_Classification:

    def match_All_Scaffold_Smarts(self, Scaffold_FilePath, Representative_qMol_Smarts):

        S_all_Smarts = []
        S_all_Classes = []
        Matched_Scaffolds = []

        f = open(Scaffold_FilePath, "r")

        while True:
            line = f.readline()
            if not line: break
            new_line = line.split("\t")
            S_all_Classes.append(new_line[0])
            S_all_Smarts.append(new_line[1])

        for ai in range (0, len(S_all_Smarts)):

            try:
                qMol = Chem.MolFromSmarts(Representative_qMol_Smarts)

                if qMol.HasSubstructMatch(Chem.MolFromSmarts(S_all_Smarts[ai])):
                    Matched_Scaffolds.append(str(S_all_Classes[ai])[0:3])

            except IndexError:()


        return Matched_Scaffolds