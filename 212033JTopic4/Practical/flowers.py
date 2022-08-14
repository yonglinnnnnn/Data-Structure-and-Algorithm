# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def front_H(flowers):
    # Put each word into the h_list or the other_list
    h_list = []
    other_list = []

    for f in flowers:
        if f.startswith('H'):
            h_list.append(f)
        else:
            other_list.append(f)
    return sorted(h_list) + sorted(other_list)


input_list = ['Bougainvillea', 'Orchids',
              'Hibiscus', 'Frangipani', 'Honeysuckle']
list2 = []

print(f'Provided list: {input_list}')
final = front_H(input_list)
print(final)


# enhancement: shortening of code
def sortflower(theSeq):
    return sorted([x for x in theSeq if x.lower().startswith('h')]) + sorted(
        [x for x in theSeq if not x.lower().startswith('h')])


print('enhancement: shortening of code')
print(sortflower(['Bougainvillea', 'Orchids',
                  'Hibiscus', 'Frangipani', 'Honeysuckle']))

print('enhancement #2: shortening of code using functional programming')
print(list(sorted(filter(lambda x: x.lower().startswith('h'), input_list))) + list(
    sorted(filter(lambda x: not x.lower().startswith('h'), input_list))))
