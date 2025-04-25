
# 📦 AWS S3 File Upload Task

This guide will walk you through opening an AWS account, uploading a file to S3 manually, and uploading a file using Python.  
**Task due: 04/17**

---

## ✅ Step-by-Step Instructions

1. **Create an AWS Account**  
   Go to [https://aws.amazon.com](https://aws.amazon.com) and sign up. Complete the registration process and log in to the AWS Management Console.

2. **Install AWS CLI**  
   If you’re on macOS, run:  
   ```bash
   brew install awscli
   ```  
   On Windows, download from: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

3. **Configure AWS CLI**  
   In your terminal, run:  
   ```bash
   aws configure
   ```  
   Enter your:
   - **AWS Access Key ID**
   - **AWS Secret Access Key**
   - **Default region name** (e.g., `us-east-1`)
   - **Output format** (press Enter to use `json`)  
   You can generate your credentials here:  
   IAM → Users → `lego-user` → **Security credentials** → **Create access key**

4. **Create an S3 Bucket**  
   - In the AWS Console, go to the **S3** service
   - Click **"Create bucket"**
   - Set a unique bucket name, like `my-bucket-lego`
   - Leave default settings and click **"Create bucket"**

5. **Upload a File Manually to S3**
   - Open the bucket
   - Click **"Upload"**
   - Click **"Add files"** and choose something like `hello.docx`
   - Click **"Upload"**

6. **Give Your IAM User Permission to Upload**
   - Go to **IAM → Users → lego-user**
   - Click **"Add permissions"**
   - Choose **"Attach policies directly"**
   - Search and attach `AmazonS3FullAccess`  
   (or see step 10 to use a custom policy for tighter access)

7. **Install Boto3 in Your Python Project**
   ```bash
   pip install boto3
   ```

8. **Create Python Script for Uploading**

   Create a file called `main.py` and paste:

   ```python
   import boto3

   bucket_name = 'my-bucket-lego'
   file_path = '/Users/marzan666/Downloads/hello.docx'
   s3_key = 'hello.docx'  # What it will be called in the bucket

   s3 = boto3.client('s3')

   try:
       s3.upload_file(file_path, bucket_name, s3_key)
       print(f"✅ File uploaded to https://{bucket_name}.s3.amazonaws.com/{s3_key}")
   except Exception as e:
       print(f"❌ Upload failed: {e}")
   ```

9. **Run the Script**
   ```bash
   python main.py
   ```  
   If the upload succeeds, you’ll see a success message with the file URL. If there's a permission error, check that the correct IAM policy is attached.

10. **(Optional) Use a Custom Inline IAM Policy**
   If you prefer to limit access to just this bucket (instead of full access), use this policy instead:

   - Go to **IAM → Users → lego-user → Add inline policy**
   - Choose the **JSON** tab
   - Paste:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "s3:PutObject",
           "s3:GetObject",
           "s3:ListBucket"
         ],
         "Resource": [
           "arn:aws:s3:::my-bucket-lego",
           "arn:aws:s3:::my-bucket-lego/*"
         ]
       }
     ]
   }
   ```

   - Click **Next**, name the policy (e.g., `S3UploadOnly`), and save.

---
