import requests

proteins = []
with open("PF04034_reduced.fasta", "r") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip("\n").startswith(">"):
            numba = line.find("(")
            numbb = line.find(")")
            proteins.append(line[numba+1:numbb])

for i in range(len(proteins)):
    protein = proteins[i]
    URL = f"https://alphafold.ebi.ac.uk/files/AF-{protein}-F1-model_v3.cif"
    tmp = requests.get(URL)
    open(f"cif/AF-{protein}-F1-model_v3.cif", "wb").write(tmp.content)