# E7.Write a Python Program to Translate a Message into Secret Code Language. Use the Rules Below to Translate Normal English into Secret Code Language.
# Coding:
# If:
# The Word Contains at Least 3 Characters, Remove the First Letter and Append it at the End. Now Append Three Random Characters at the Starting and the End.
# Else:
# Simply Reverse the String.
# Decoding:
# If:
# The Word Contains Less than 3 Characters, Reverse it.
# Else:
# Remove 3 Random Characters from Start and End. Now Remove the Last Letter and Append it to the Beginning.
# Your Program should Ask Whether you want to Code or Decode.
st = input("Enter Message : ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding : ")
coding = True if coding == "1" else False
if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "abc"
            r2 = "xyz"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))