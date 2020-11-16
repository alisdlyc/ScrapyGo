import json

content = ""
with open('cookies2_original.txt', 'r') as f:
    content += f.readline()
contents = content.split("; ")
results = []
for content in contents:
    content = content.split("=")
    content_dict = {}
    content_dict["name"], content_dict["value"] = content[0], content[1]
    results.append(content_dict)

with open('cookies2.txt', 'w') as f:
    f.write(json.dumps(results))
# print(contents)