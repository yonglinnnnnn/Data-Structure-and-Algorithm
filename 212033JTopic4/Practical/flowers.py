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

print(f'Provided list: {input_list}')
final = front_H(input_list)
print(final)
