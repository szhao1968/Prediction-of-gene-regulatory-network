dic = {}
count = 0
c = 0
ss = []
file = open("TF-TF-tissue-skin.txt", "r")
for line in file:
    ss.append(line)
for s in ss:
    s = s.replace(' ', '')[:-2]
    list1 = s.split(":")
    if list1[0] not in dic:
        dic[list1[0]] = count
        count = count + 1
    if list1[1] not in dic:
        dic[list1[1]] = count
        count = count + 1


with open("TF-TF-tissue-skinnumbertrain.txt", "w") as f:
    for i  in range(0, 6608):
        s = ss[i].replace(' ', '')[:-2]
        list1 = s.split(":")
        f.write(str(dic[list1[0]]) + '\t' + str(dic[list1[1]] ) + '\n')

with open("TF-TF-tissue-skintest.txt", "w") as f:
    for i in range(6609, 7341):
        s = ss[i].replace(' ', '')[:-2]
        list1 = s.split(":")
        f.write(str(dic[list1[0]]) + '\t' + str(dic[list1[1]] ) + '\n')


dicttrain = {}
count1 = 1
count2 = 1
test = []
file = open("TF-TF-tissue-skintest.txt", "r")
for line in file:
    count1 = count1 + 1
    if line not in dicttrain:
        test.append(line)
        dicttrain[line] = count
        count2 = count2 + 1


dicttest = {}
count1 = 1
count2 = 1
train  = []
file = open("TF-TF-tissue-skinnumbertrain.txt", "r")
for line in file:
    count1 = count1 + 1
    if line not in dicttest:
        train.append(line)
        dicttest[line] = count
        count2 = count2 + 1
with open("tissue-skintest.txt", "w") as f:
    for s in test:
        s.split('\n')[0].split('\t')[0],s.split('\n')[0].split('\t')[1]
        f.write(s.split('\n')[0].split('\t')[0] + '\t' + s.split('\n')[0].split('\t')[1] + '\n')


with open("tissue-skintrain.txt", "w") as f:
    for s in train:
        s.split('\n')[0].split('\t')[0],s.split('\n')[0].split('\t')[1]
        f.write(s.split('\n')[0].split('\t')[0] + '\t' + s.split('\n')[0].split('\t')[1] + '\n')
