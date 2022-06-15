# Boto

1. [What is this?](#What-is-this?)
2. [How to install?](#How-to-install?)
3. [How to use it?](#How-to-use-it?)
    1. [Development](#Development)
    2. [Usage](#Usage)
4. [References](#References)

## What is this?

It's used to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon
Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.

## How to install?

```shell
pip install boto3
```

_Tips:_ Think to add it in your **requirements.txt** file

## How to use it?

### Authentication

To be able to contact AWS services, we must be authenticated with the corresponding credentials.

This can be done through the module parameters, example:

```python
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
)
```

Or with the environment variables, example:

- __AWS_ACCESS_KEY_ID__ - The access key for your AWS account.
- __AWS_SECRET_ACCESS_KEY__ - The secret key for your AWS account.
- __AWS_SESSION_TOKEN__ - The session key for your AWS account. This is only needed when you are using temporary
  credentials. The AWS_SECURITY_TOKEN environment variable can also be used, but is only supported for backwards
  compatibility purposes. AWS_SESSION_TOKEN is supported by multiple AWS SDKs besides python.

To ease the next steps this course will be based on the environment variables.

### Development

Import the module

```python 
import boto3
```

Load the considered resource or client depending on the need

```python
ec2_resource = boto3.resource('ec2')
rds_client = boto3.client('rds')
```

Integrate it in your code

```python
ec2_resource.get_instance_id()
rds_client.get_instance_id()
```

### Usage

### Write the following script to manipulate S3 file

```python
import json
import boto3


class S3(object):
    """
    Provide S3 file functions
    """

    def __init__(self, bucket_name: str):
        """
        object setup
        :param str bucket_name: the bucket where the file must be stored
        """
        self.bucket_name = bucket_name
        self.s3_resource = boto3.resource('s3')

    def get(self, file_name: str):
        """
        get s3 file data
        :param str file_name: the filename to get content
        :return: none instead if issue
        """
        return self.s3_resource.Object(self.bucket_name, file_name).get()['Body'].read()

    def update(self, file_name: str, data: dict):
        """
        update s3 file content
        :param str file_name: the filename to update
        :param dict data: the data to record in the file
        :return: none instead if issue
        """
        try:
            if 'bound method' in str(data['data']['results']):
                data['data'].pop('results')
        except Exception:
            pass
        return self.s3_resource.Object(self.bucket_name, file_name).put(Body=(bytes(json.dumps(data).encode('UTF-8'))))

    def delete(self, file_name: str):
        """
        delete s3 file
        :param str file_name: the filename to delete
        :return: none instead if issue
        """
        return self.s3_resource.Object(self.bucket_name, file_name).delete()


if __name__ == '__main__':
    bucket_name = str("myBucket")
    file_name = str("hello.json")
    file_data = dict({"message": "Hello!"})
    
    # Class instance
    s3 = S3(bucket_name=bucket_name)

    # Execute the functions of the S3 class
    print('Create file', s3.update(file_name, file_data))
    print('Get file content', s3.get(file_name))
    print('Delete file', s3.delete(file_name))
```

And execute it

## References

- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html