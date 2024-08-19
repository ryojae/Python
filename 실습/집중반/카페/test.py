f = open("구구단.txt", 'w')

print("\n")

for i in range(1, 10):
    for k in range(2, 10):
        print(f' {k:2d} *{i:2d} = {k*i:2d}', end='\t')
        # 파일에 기록할 문자열 포맷
        data = "%2d *%2d = %2d\t" % (k , i, k*i)
        # 파일에 기록
        f.write(data)
    print()
    # 파일에 줄바꿈 문자 기록
    f.write("\n")

f.close()
print("\n")
