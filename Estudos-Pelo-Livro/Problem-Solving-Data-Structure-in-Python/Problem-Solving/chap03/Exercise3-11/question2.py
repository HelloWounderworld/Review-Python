# Devise an experiment to verify that get item and set item are O(1) for dictionaries.

def getItemDic(dictionary, key):
    return dictionary.get(key)

def getItemDic2(dictionary, key):
    return dictionary[key]

def setItemDic(dictionary, key, item):
    dictionary[key] = item

def setItemDic(dictionary, key, item):
    dictionary.__setitem__(key, item)
