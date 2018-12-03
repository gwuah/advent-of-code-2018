with open('./dataset.txt', 'r') as dataset :
  resulting_frequency = 0
  for frequency in dataset.readlines() :
    if frequency[0] == '+' :
      resulting_frequency += int(frequency[1:].rstrip())
    elif frequency[0] == '-' :
      resulting_frequency -= int(frequency[1:].rstrip())
  print(resulting_frequency)