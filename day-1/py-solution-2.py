# lmao dont judge me, I had just finished writting 
# an engineering examination.

# def find_first_duplicate_frequency(array) :
#   with open('./dataset.txt', 'r') as dataset :
#     resulting_frequency = 0
#     for frequency in dataset.readlines() :
#       resulting_frequency += int(frequency[1:].rstrip())
#       if resulting_frequency in array :
#         print(resulting_frequency)
#         return resulting_frequency
#       else : array.append(resulting_frequency)
#   return False

# array = []
# while find_first_duplicate_frequency(array) is False:
#   find_first_duplicate_frequency(array)


def find_first_duplicate_frequency(array=[]) :
  with open('./dataset.txt', 'r') as dataset :
    resulting_frequency = 0
    for frequency in dataset.readlines() :
      resulting_frequency += int(frequency[1:].rstrip())
      if resulting_frequency in array :
        return resulting_frequency
      else : array.append(resulting_frequency)
  return find_first_duplicate_frequency(array)

print(find_first_duplicate_frequency([]))