import os
num= 1
chk = os.listdir("name")
for i in chk:
    if i.endswith(".pdf"):
        os.rename(f"name/{i}", f"name/{num}.pdf")
        num +=1
        # print(i)