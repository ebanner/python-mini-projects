import boto3

s3_client = boto3.client('s3')


def put(key, value, bucket='storage9'):
    s3_client.put_object(Bucket=bucket, Key=key, Body=value)


def get(key, bucket='storage9'):
    object = s3_client.get_object(Bucket=bucket, Key=key)
    value = object['Body'].read().decode('utf-8')
    return value


if __name__ == '__main__':
    put('foo', 'bar')
    value = get('foo')
    print(value)

