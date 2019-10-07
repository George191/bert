import pandas as pd

lines = pd.read_csv('Train_DataSet.csv', header=0, delimiter=',')
label = pd.read_csv('Train_DataSet_Label.csv', header=0, delimiter=',')

outfile = pd.merge(lines, label, how='left', left_on='id', right_on='id')

outfile = pd.DataFrame(outfile).sample(frac=1)

train = outfile[:6500]
dev = outfile[6500:]

train.to_csv('train.csv', index=False, encoding='utf-8')
dev.to_csv('dev.csv', index=False, encoding='utf-8')


