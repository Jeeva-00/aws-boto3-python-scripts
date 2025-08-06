import boto3

# Prompt user for EC2 instance parameters
key_name = input("Enter the Key Pair Name: ")
key_format = input("Enter the Key Format (PEM or PPK, default PEM): ") or "PEM"
key_type = input("Enter the Key Type (RSA or ED25519, default RSA): ") or "RSA"

ec2_client = boto3.client("ec2")

# Build parameters for create_key_pair

params = {
    'KeyName': key_name,
    'KeyFormat': key_format.lower(),
    'KeyType': key_type.lower()
}
# Create EC2 key pair
try:
    response = ec2_client.create_key_pair(**params)
    key_material = response['KeyMaterial']
    print(f"Key Pair created successfully with name: {key_name}")    
except Exception as e:
    print(f"Failed to create Key Pair: {e}")

