import boto3

# Prompt user for EC2 security group parameters
group_name = input("Enter the Security Group Name: ")
group_description = input("Enter the Security Group Description: ")

vpc_id = input("Enter the VPC ID (optional, press Enter to skip): ")

# Create EC2 client
ec2_client = boto3.client('ec2')

# Build parameters for create_security_group
create_sg_params = {
    'GroupName': group_name,
    'Description': group_description
}

if vpc_id:
    create_sg_params['VpcId'] = vpc_id  

# Create EC2 security group
try:
    response = ec2_client.create_security_group(**create_sg_params)
    security_group_id = response['GroupId']
    print(f"Security Group created with ID: {security_group_id}")
    print(f"Security Group Name: {group_name}")
    print(f"Security Group Description: {group_description}")
except Exception as e:
    print(f"Failed to create Security Group: {e}")
    exit(1) 
