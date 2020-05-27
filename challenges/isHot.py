is_hot = 'yes'
if isinstance(is_hot, str) and (is_hot == 'yes'):
    print("it's hot")
elif isinstance(is_hot, str) and (is_hot == 'no'):
    print("it's cold")
else:
    print('N/A')