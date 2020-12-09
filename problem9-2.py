data = [int(i.strip()) for i in open("input9.txt", "r").readlines()]
find = 25918798
check = 0
for i in range(len(data)):
  if check == find:
    break
  for j in range(i, len(data)):
    check = sum(data[i:j])
    if check >= find:
      break

print(check, min(data[i:j])+max(data[i:j]))
