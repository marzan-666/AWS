'''import boto3
s3 = boto3.client('s3')
s3.upload_file('/Users/marzan666/Downloads/Amazon_Web_Services_Logo.svg.png', 'my-bucket-lego', 'aws-logo.png')
'''

import boto3

# Your bucket and file info
bucket_name = 'my-bucket-lego'
file_path = '/Users/marzan666/Downloads/hi.docx'  # Local file
s3_key = 'hi.docx'  # File name in S3

# Create S3 client
s3 = boto3.client('s3')

# Upload
try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"✅ File uploaded to https://{bucket_name}.s3.amazonaws.com/{s3_key}")
except Exception as e:
    print(f"❌ Upload failed: {e}")


'''python'''
