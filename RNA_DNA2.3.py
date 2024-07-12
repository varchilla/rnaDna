rna_codon = {
'UUU': 'phe ', 'UUC': 'phe ', 'UUA': 'leu ', 'UUG': 'leu ', 'CUU': 'leu ',
'CUC': 'leu ', 'CUA': 'leu ', 'CUG': 'leu ', 'AUU': 'ile ', 'AUC': 'ile ',
'AUA': 'ile ', 'AUG': 'met ', 'GUU': 'val ', 'GUC': 'val ', 'GUA': 'val ',
'GUG': 'val ', 'UCU': 'ser ', 'UCC': 'ser ', 'UCA': 'ser ', 'UCG': 'ser ',
'CCU': 'pro ', 'CCC': 'pro ', 'CCA': 'pro ', 'CCG': 'pro ', 'ACU': 'thr ',
'ACC': 'thr ', 'ACA': 'thr ', 'ACG': 'thr ', 'UUU': 'phe ', 'GCU': 'ala ',
'GCC': 'ala ', 'GCA': 'ala ', 'GCG': 'ala ', 'UAU': 'lyr ', 'UAC': 'lyr ',
'CAU': 'his ', 'CAC': 'his ', 'CAA': 'gln ', 'CAG': 'gln ', 'AAU': 'asn ',
'AAC': 'asn ', 'AAA': 'lys ', 'AAG': 'lys ', 'GAU': 'asp ', 'GAC': 'asp ',
'GAA': 'glu ', 'GAG': 'glu ', 'UGU': 'cys ', 'UGC': 'cys ', 'CGU': 'arg ',
'CGC': 'arg ', 'CGA': 'arg ', 'CGG': 'arg ', 'AGU': 'ser ', 'AGC': 'ser ',
'AGA': 'arg ', 'AGG': 'arg ', 'GGU': 'gly ', 'GGC': 'gly ', 'GGA': 'gly ',
'GGG': 'gly '}

DNA2 = ''
RNA1 = []
RNA2 = []
RNA3 = []
start1=0
stop1=0
start2=0
stop2=0
star3=0
stop3=0

print('Привет! Я помогу тебе транскрибировать ДНК в РНК, а затем в цепочку аминокислот.')
DNA = input('Введи сюда цепь ДНК на английском языке:')
print('Вы ввели ДНК:',DNA)

for i in range(len(DNA)):
    if DNA[i] == 'T':
        DNA2 += 'A'
    elif DNA[i] == 'A':
        DNA2 += 'U'
    elif DNA[i] == 'G':
        DNA2 += 'C'
    elif DNA[i] == 'C':
        DNA2 +='G'
    else:
        print('Вы ввели неизвестный элемент. Просмотрите программу и возвращайтесь снова! Все написанное далее - неправда!!!')
        break

print('Полная цепь РНК:', DNA2)


for i in range(0, len(DNA2)):
    if DNA2[i:i+3] == "AUU" or DNA2[i:i+3] =="AUA" or DNA2[i:i+3] =="CUG" or DNA2[i:i+3] =="AUG":
        start1 = i
        break
        
for i in range(0, len(DNA2)):
    if DNA2[i:i+3] == "UAG" or DNA2[i:i+3] == "UGA" or DNA2[i:i+3] == "UAA":
        stop1 = i
        break
    
for i in range(stop1+3, len(DNA2)):
    if DNA2[i:i+3] == "AUU" or DNA2[i:i+3] =="AUA" or DNA2[i:i+3] =="CUG" or DNA2[i:i+3] =="AUG":
        start2 = i
        break
        
for i in range(stop1+3, len(DNA2),3):
    if DNA2[i:i+3] == "UAG" or DNA2[i:i+3] == "UGA" or DNA2[i:i+3] == "UAA":
        stop2 = i
        break

for i in range(stop2+3, len(DNA2),3):
    if DNA2[i:i+3] == "AUU" or DNA2[i:i+3] =="AUA" or DNA2[i:i+3] =="CUG" or DNA2[i:i+3] =="AUG":
        start3 = i
        break
        
for i in range(stop2+3, len(DNA2),3):
    if DNA2[i:i+3] == "UAG" or DNA2[i:i+3] == "UGA" or DNA2[i:i+3] == "UAA":
        stop3 = i
        break

RNA1.append(DNA2[start1:stop1+3])
print('РНК1 -', ''.join(RNA1))
RNA1_1=[]
x=str(RNA1)
for i in range(2,len(x)-2,3):
    RNA1_1.append(x[i:i+3])

RNA2.append(DNA2[start2:stop2+3])
print('РНК2 -',''.join(RNA2))
RNA1_2=[]
y=str(RNA2)
for i in range(2,len(y)-2,3):
    RNA1_2.append(y[i:i+3])

RNA3.append(DNA2[start3:stop3+3])
print('РНК3 -',''.join(RNA3))
RNA1_3=[]
z=str(RNA3)
for i in range(2,len(z)-2,3):
    RNA1_3.append(z[i:i+3])



print(RNA1_1)
print(RNA1_2)
print(RNA1_3)


protein_string = ""


for i in range(0, len(RNA1_1)-(3+len(RNA1_1)%3), 3):
    p=0
    while True:
        if RNA1_1[i] == rna_codon[p]:
            p += 1
    protein_string += rna_codon[RNA1_1[i:i+3]]
print("Protein String: ", protein_string)
