f=open("complete.csv","r")
dict={}
for lines in f:
    data= lines.strip("\n").split((","))
    state=data[1]
    confirmed=data[4]
    death=data[5]
    recovery=data[6]

    if (state not in dict):
        dict[state] = {"state": state, "confirmed": confirmed, "death": death,"recovery":recovery}


def fetchData(**kwargs):
    id=kwargs["state"]
    if (state not in dict):
        print("state not exist")
    else:
        dict[state] = {"state": state, "confirmed": confirmed, "death": death,"recovery":recovery}
        print(dict[state]["confirmed"])

        if "param" in kwargs:
            val=kwargs["param"]
            print(dict[state][val])
fetchData(state="kerala",param="confirmed")
print("confirmed",confirmed)
def fetchData2(**kwargs):
    id=kwargs["state"]
    if (state not in dict):
        print("state not exist")
    else:
        print(dict[state]["death"])

        if "param" in kwargs:
            val=kwargs["param"]
            print(dict[state][val])
fetchData2(state="kerala",param="death")
print("death",death)
def fetchData3(**kwargs):
    id=kwargs["state"]
    if (state not in dict):
        print("state not exist")
    else:
        print(dict[state]["recovery"])
        if "param" in kwargs:
            val=kwargs["param"]
            print(dict[state][val])
fetchData3(state="kerala",param="recovery")
print("recovery",recovery)





