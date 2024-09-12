import boto3
import json

iam = boto3.client('iam')

response = iam.list_groups()
grpTotal = len(response["Groups"])

grpNames = []

i = 0
while i < len(response["Groups"]):
    if response["Groups"][i]["GroupName"] != "Admins":
        grpNames.append(response["Groups"][i]["GroupName"])
    i=i+1

for name in grpNames:
    response = iam.delete_group(
     GroupName= name
    )
"""
 response = flag.create_group(
    GroupName="DBA"

)

response = flag.create_group(
    GroupName="WebsiteAdmin"

)
response = flag.create_group(
    GroupName="ContentEditor"
)

"""