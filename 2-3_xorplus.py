S = input()
big_number = int(S[0])

for i in range(0, len(S)-2) :
	if int(S[i]) == 0 or int(S[i]) == 1 :
		big_number += int(S[i+1])

	else :
		big_number *= int(S[i+1])
		#print(big_number)

if S[len(S)-1] == '0' or S[len(S)-1] == '1' :
	big_number += int(S[len(S)-1])
else :
    big_number *= int(S[len(S)-1])  

print(big_number)