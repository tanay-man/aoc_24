def process_ip(file_name):
    with open(file_name) as f:
        data = f.read()
    data = [ele.split() for ele in data.split('\n')]
    return data

def get_safe(data):
    safe = []

    for li in data:
        increasing = int(li[1]) > int(li[0])

        for i in range(len(li)-1):
            diff = abs(int(li[i]) - int(li[i + 1]))
            if not (0 < diff < 4) or (int(li[i+1]) > int(li[i])) != increasing:
                safe.append(0)
                break
        print(li)
        safe.append(1)
    print(safe.count(1))
    return safe

def main():
    data = process_ip('ip_2.txt')
    get_safe(data)

main()