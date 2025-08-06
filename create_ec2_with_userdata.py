import boto3

# Prompt user for EC2 instance parameters
image_id = input("Enter the AMI Image ID: ")
instance_type = input("Enter the Instance Type (e.g., t2.micro): ")
key_name = input("Enter the Key Pair Name: ")
security_group = input("Enter the Security Group ID: ")
subnet_id = input("Enter the Subnet ID (optional, press Enter to skip): ")
tag_name = input("Enter a Name tag for the instance: ")

print("Enter the User Data script (multi-line, end with a line containing only END) or path to a file:")
user_data_lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    user_data_lines.append(line)
user_data = "\n".join(user_data_lines)

# If user_data is a file path, read its contents
import os
if len(user_data_lines) == 1 and os.path.isfile(user_data):
    with open(user_data, 'r') as f:
        user_data = f.read()

# Create EC2 client
ec2 = boto3.client('ec2')

# Build parameters for run_instances
params = {
    'ImageId': image_id,
    'InstanceType': instance_type,
    'KeyName': key_name,
    'SecurityGroupIds': [security_group],
    'MinCount': 1,
    'MaxCount': 1,
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': tag_name}
            ]
        }
    ],
    'UserData': user_data
}
if subnet_id:
    params['SubnetId'] = subnet_id

# Launch EC2 instance
try:
    response = ec2.run_instances(**params)
    instance_id = response['Instances'][0]['InstanceId']
    architecture = response['Instances'][0].get('Architecture', 'N/A')
    publicip = response['Instances'][0].get('PublicIpAddress', 'N/A')
    privateip = response['Instances'][0].get('PrivateIpAddress', 'N/A')
    tag_specifications = response['Instances'][0].get('Tags', [])
    security_groups = response['Instances'][0].get('SecurityGroups', [])
    print(f"EC2 Instance created with ID: {instance_id}")
    print(f"Architecture: {architecture}")
    print(f"Public IP Address: {publicip}")
    print(f"Private IP Address: {privateip}")
    print(f"Tag Specifications: {tag_specifications}")
    print(f"Security Groups: {security_groups}")
except Exception as e:
    print(f"Error creating EC2 instance: {e}")
