def main():
    strand = input("What is the DNA strand? ")
       
    upper = _check_dnacodon(strand)
    lower = _reverse_upper(_check_dnacodon(strand))
    mRNA_upper = _DNA_transcription(_check_dnacodon(strand))
    mRNA_lower = _DNA_transcription_lower(_DNA_transcription(_check_dnacodon(strand)))
    if upper == None:
        print("No coden given!")
    elif upper[1] == False:
        print(upper[0])
    else:
        print(f"{upper} is the upper strand.")
    
    if lower == None:
        pass
    elif lower == False:
        print("Invalid upper strand!")
    else:
        print(f"{lower} is the lower strand.")

    if mRNA_upper == None:
        pass
    elif mRNA_upper == False:
        print("DNA can't be transcribed to mRNA!")
    else:
        print(f'{mRNA_upper} is the transcription of upper DNA strand')
    
    if mRNA_lower == None:
        pass
    elif mRNA_lower == False:
        print("DNA can't be transcribed to mRNA!")
    else:
        print(f'{mRNA_lower} is the transcription of lower DNA strand')
   
def _check_dnacodon(strand):
    if  not strand:
        return None
    else:
        for strands in strand:
            if strands not in ["A","T","C","G","a","t","c","g"]:
                return "These are not DNA codons", False
    return "".join(strand)


def _reverse_upper(_check_dnacodon):
    
    reverse_DNA_codon = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C",
        "a":"t",
        "t":"a",
        "c":"g",
        "g":"c",
        }
    x = _check_dnacodon
    
    if x == None:
        return None
    elif x[1] == False:
        return False
    else:
        strand = x
        new_strand = []
        for strands in strand:
            if strands in reverse_DNA_codon.keys():
                codon = reverse_DNA_codon[strands]
                new_strand.append(codon)
        return "".join(new_strand)
    
def _DNA_transcription(_check_dnacodon):
    transcription_DNA_codon = {
        "A":"U",
        "T":"A",
        "C":"G",
        "G":"C",
        "a":"u",
        "t":"a",
        "c":"g",
        "g":"c",
        }
    y = _check_dnacodon
    
    if y == None:
        return None
    elif y[1] == False:
        return False
    else:
        strand = y
        RNA_upper_strand = []
        for strands in strand:
            if strands in transcription_DNA_codon.keys():
                codon = transcription_DNA_codon[strands]
                RNA_upper_strand.append(codon)
        return "".join(RNA_upper_strand)

def _DNA_transcription_lower(_DNA_transcription):
    transcription_DNA_codon_lower = {
        "A":"U",
        "U":"A",
        "C":"G",
        "G":"C",
        "a":"u",
        "u":"a",
        "c":"g",
        "g":"c",
        }
    z = _DNA_transcription
    if z == None:
        return None 
    elif z == False:
        return False
    else:
        strand = z
        RNA_lower_strand = []
        for strands in strand:
            if strands in transcription_DNA_codon_lower.keys():
                codon = transcription_DNA_codon_lower[strands]
                RNA_lower_strand.append(codon)
        return "".join(RNA_lower_strand)

if __name__ == "__main__":
    main()