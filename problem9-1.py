data = [int(i.strip()) for i in open("input9.txt", "r").readlines()]

for i in range(25, len(data)):
  previous = data[i-25:i]
  results = [(element, data[i]-element) for element in previous if data[i]-element in previous and data[i] != 2*element]
  if len(results) == 0:
    break
print(data[i])
