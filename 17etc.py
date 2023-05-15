import re
import json
x = '{"name":"Tom","age":40,"gender":"male"}'
p = json.loads(x)
print(p, type(p), p["age"])
x1 = json.dumps(p)
print(x1, type(x1))

txt = "Apple under the tree"
k = re.search("^Apple", txt)
if k:
    print("match")
else:
    print("not match")
