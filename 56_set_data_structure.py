# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope
# set does not support indexing
print(tags[0])

query_one = 'python' in tags
# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope
print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)

# set up a list of tags using curlies and listing key value paris like a list
# set requires that all elements are unique (not duplicates)
# set always guaranteed to have unique elements
# to query the set-check if python is in tags
# query doesn't give the element is it in there is what we ask 

# if you have to have a collection of items(elements)

# set is the merge of a list and dictionary syntax
# So if you ever have a situation where you need a data structure that looks a lot like a list but you can not allow for duplicates then a set might be a good pick for you.