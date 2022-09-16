import gzip
from collections import defaultdict
from datetime import datetime
import os
import copy
import time
import datetime
import json
import pandas as pd


def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)


countU = defaultdict(lambda: 0)
countP = defaultdict(lambda: 0)
line = 0

DATASET = 'h_and_m_transaction_data_processed'
data_name = "/Users/sankalpapharande/Documents/2nd Semester/Applied ML/AML Project/transactions_train.csv"


if not os.path.isdir('./'+DATASET):
    os.mkdir('./'+DATASET)
train_file = './'+DATASET+'/train.txt'
valid_file = './'+DATASET+'/valid.txt'
test_file = './'+DATASET+'/test.txt'
imap_file = './'+DATASET+'/imap.json'
umap_file = './'+DATASET+'/umap.json'

data_file = './'+DATASET+'.txt'

transaction_data = pd.read_csv(data_name)
transaction_data = transaction_data.reset_index()

count = 0
for index, one_interaction in transaction_data.iterrows():
    rev = one_interaction['customer_id']
    asin = one_interaction['article_id']
    # time_stamp = time.mktime(datetime.datetime.strptime(one_interaction['t_dat'], "%Y-%m-%d").timetuple())
    # time_stamp = float(time_stamp)
    countU[rev] += 1
    countP[asin] += 1
    count += 1
    if count % 10000 == 0:
        print("Rows computed: {}".format(count))

usermap = dict()
usernum = 1
itemmap = dict()
itemnum = 1
User = dict()


for index, one_interaction in transaction_data.iterrows():
    rev = one_interaction['customer_id']
    asin = one_interaction['article_id']
    time_stamp = time.mktime(datetime.datetime.strptime(one_interaction['t_dat'], "%Y-%m-%d").timetuple())
    time_stamp = float(time_stamp)
    if countU[rev] < 5 or countP[asin] < 5:
        continue

    if rev in usermap:
        userid = usermap[rev]
    else:
        userid = usernum
        usermap[rev] = userid
        User[userid] = []
        usernum += 1
    if asin in itemmap:
        itemid = itemmap[asin]
    else:
        itemid = itemnum
        itemmap[asin] = itemid
        itemnum += 1
    User[userid].append([itemid, time_stamp])
# sort reviews in User according to time


with open(imap_file, 'w') as f:
    json.dump(itemmap, f)

with open(umap_file, 'w') as f:
    json.dump(usermap, f)

for userid in User.keys():
    User[userid].sort(key=lambda x: x[1])


user_train = {}
user_valid = {}
user_test = {}
for user in User:
    nfeedback = len(User[user])
    if nfeedback < 3:
        user_train[user] = User[user]
        user_valid[user] = []
        user_test[user] = []
    else:
        user_train[user] = User[user][:-2]
        user_valid[user] = []
        user_valid[user].append(User[user][-2])
        user_test[user] = []
        user_test[user].append(User[user][-1])



print(usernum, itemnum)

def writetofile(data, dfile):
    with open(dfile, 'w') as f:
        for u, ilist in sorted(data.items()):
            for i, t in ilist:
                f.write(str(u) + '\t'+ str(i) + '\t' + str(t) + "\n")

def writetofile_v2(data, dfile):
    with open(dfile, 'w') as f:
        for u, ilist in sorted(data.items()):
            f.write(str(u))
            for i, t in ilist:
                f.write(' '+ str(i))
            f.write("\n")

#writetofile(user_train, train_file)
#writetofile(user_valid, valid_file)
#writetofile(user_test, test_file)

writetofile_v2(User, data_file)


num_instances = sum([len(ilist) for _, ilist in User.items()])
print('total user: ', len(User))
print('total instances: ', num_instances)
print('avg length: ', num_instances / len(User))
print('total items: ', itemnum)
print('density: ', num_instances / (len(User) * itemnum))
print('valid #users: ', len(user_valid))
numvalid_instances = sum([len(ilist) for _, ilist in user_valid.items()])
print('valid instances: ', numvalid_instances)
numtest_instances = sum([len(ilist) for _, ilist in user_test.items()])
print('test #users: ', len(user_test))
print('test instances: ', numtest_instances)