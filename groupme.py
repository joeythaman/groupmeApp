import requests

accessToken = "sbnIa4uhbyrFzvRKOT5DupNlXXbyJOeOgrmEh0gs"

resp = requests.get("https://api.groupme.com/v3/groups?token=" + accessToken)
print(resp.status_code)
data = resp.json()["response"]
print(data)

groupname = "West Lag CS 109 😍"

IDtoNAME = {}
NAMEtoID = {}
groupId = 0
for i in data:
    print(i["name"])
    if (i["name"] == groupname):
        groupId = i["group_id"]
        print(i)
        for j in i["members"]:
            print(j)
            NAMEtoID[j["nickname"]] = j["user_id"]
            IDtoNAME[j["user_id"]] = j["nickname"]

print("")
newRequest = "https://api.groupme.com/v3/groups/" + str(groupId) + "/messages?token=" + accessToken
resp = requests.get(newRequest)
print(resp)
print(resp.json())
messages = resp.json()["response"]["messages"]
likes = {}
print(IDtoNAME)
for i in NAMEtoID:
    likes[i] = {}
print("")
for i in messages:
    print("")
    print(i)
    print(i["text"])
    for j in i["favorited_by"]:
        jName = IDtoNAME[j]
        if jName not in likes[i["name"]]:
            likes[i["name"]][jName] = 0
        likes[i["name"]][jName] += 1
print(likes)