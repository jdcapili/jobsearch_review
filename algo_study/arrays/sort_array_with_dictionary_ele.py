# inputArray = [{
#   origin: "BOS",
#   destination: "JFK"
# },
# {
#   origin: "LA",
#   destination: "PEK"
# },
# {
#   origin: "JFK",
#   destination: "LA"
# }]

iterate through input, create dest set and dictionary(O(n))
dest {JFK,PEK,LA}
{BOS:JFK, LA:PEK, JFK:LA}


find key not in dest


while(len(res) != len(input)):
    res.append([{origin: key, destination: dictionary[key]}])
    key = dictionary[key]

return res


if val not in dictionary: last iten



#  output = [{
#    origin: "BOS",
#    destination: "JFK"
#  },
#  {
#    origin: "JFK",
#    destination: "LA"
#  },
#  {
#    origin: "LA",
#    destination: "PEK"
#  }]


