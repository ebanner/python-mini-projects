import json

import boto3

secrets_client = boto3.client("secretsmanager")

def get_secret(secret_name, secret_key=None):
    response = secrets_client.get_secret_value(SecretId=secret_name)
    result = response['SecretString']
    secrets = json.loads(result)

    if secret_key:
        return secrets[secret_key]
    else:
        return secrets


password = get_secret('MySuperSecret', 'password')

print(password)

