def concate_list_items(items):
    output = ''
    for item in items:
        output += f'{item} '
        #output += str(item)
    return output


print(concate_list_items(['vineet', 'scored', 98.5, 'out', 'of', 100]))