import boto3

# Prompt user for EC2 instance parameters
image_id = input("Enter the AMI Image ID: ")
instance_type = input("Enter the Instance Type (e.g., t2.micro): ")
key_name = input("Enter the Key Pair Name: ")
security_group = input("Enter the Security Group ID: ")
subnet_id = input("Enter the Subnet ID (optional, press Enter to skip): ")
tag_name = input("Enter a Name tag for the instance: ")

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
    ] # type: ignore
}
if subnet_id:
    params['SubnetId'] = subnet_id

# Launch EC2 instance
try:
    response = ec2.run_instances(**params)
    instance_id = response['Instances'][0]['InstanceId']
    architecture = response['Instances'][0].get('Architecture', 'N/A')
    print(f"EC2 Instance created with ID: {instance_id}")
    print(f"Architecture: {architecture}")
except Exception as e:
    print(f"Error creating EC2 instance: {e}")
