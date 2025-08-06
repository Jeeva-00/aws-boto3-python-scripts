import boto3

# Prompt user for IAM user parameters
user_name = input("Enter the IAM User Name: ")
user_policy = input("Enter the IAM User Policy (JSON format): ")
secret_access_key = input("Do you want to create a Secret Access Key for this user? (yes/no): ").strip().lower()

iam_client = boto3.client("iam")

# Create IAM user
try:
    response = iam_client.create_user(UserName=user_name)
    if user_policy:
        iam_client.put_user_policy(
            UserName=user_name,
            PolicyName=f"{user_name}_policy",
            PolicyDocument=user_policy
        )
    if secret_access_key == 'yes':
        access_key_response = iam_client.create_access_key(UserName=user_name)
        access_key_id = access_key_response['AccessKey']['AccessKeyId']
        secret_access_key_value = access_key_response['AccessKey']['SecretAccessKey']
        print(f"Access Key ID: {access_key_id}")
        print(f"Secret Access Key: {secret_access_key_value}")
    print(f"IAM User created successfully with name: {user_name}")
except Exception as e:
    print(f"Failed to create IAM User: {e}")
