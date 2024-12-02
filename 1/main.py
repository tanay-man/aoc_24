def process_ip(file_name):
    with open(file_name) as f:
        data = f.read()
    data = data.split('\n')
    col_1 , col_2 = [], []
    for ele in data:
        split_ls = ele.split()
        col_1.append(split_ls[0])
        col_2.append(split_ls[1])
    col_1.sort()
    col_2.sort()
    return col_1, col_2

def get_diff(col_1, col_2):
    diff = 0
    for i in range(len(col_1)):
        diff = diff + abs(int(col_1[i]) - int(col_2[i]))
    return diff

def get_similarity(col_1, col_2):
    p = 0
    score = 0
    col_1 = dict.fromkeys(col_1)
    for ele , val in col_1.items():
        while int(ele) >= int(col_2[p]):
            if p >= len(col_2):
                break
            if int(ele) == int(col_2[p]):
                score = score + int(col_2[p])
            p = p + 1
        if p >= len(col_2):
            break
    return score

def main():
    col_1 , col_2 = process_ip('ip_1.txt')
    diff = get_diff(col_1, col_2)
    print("Diff = ", diff)
    score = get_similarity(col_1, col_2)
    print("Score = ", score)

main()