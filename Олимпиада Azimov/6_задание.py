speakers = ['0000a0000n00000t0000o000n',
            'a6n6t6n',
            'gylfole',
            'anton666',
            'ant0n',]
for i in range(len(speakers)):
    if ('a' in speakers[i] and 't' in speakers[i] and 'o' in speakers[i] and speakers[i].count('n') >= 2):
        print(i + 1, end=' ')