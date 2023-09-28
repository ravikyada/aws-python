import boto3
import botocore
import os

# Initialize the S3 client
aws_access_key_id = 'AWSACESSKEY'
aws_secret_access_key = 'AWSSECRETACESSKEY' 
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# List of image object keys you want to download
image_keys_to_download = [
"sta10/maths/chapter10.pdf",
"sta11/science/biology/chapter08.pdf",
"data/sta10/class11/scientists/pythagoras"
]

# Destination directory where the images will be downloaded
destination_base_directory = "~/s3-download-class"

# Loop through the list of image keys and download each image while preserving folder structure
for image_key in image_keys_to_download:
    try:
        # Extract the folder structure from the image key
        folder_structure = os.path.dirname(image_key)

        # Create the destination directory including the folder structure
        destination_directory = os.path.join(destination_base_directory, folder_structure)

        # Make sure the destination directory exists
        os.makedirs(destination_directory, exist_ok=True)

        # Get the object from S3 and save it locally while preserving folder structure
        local_file_path = os.path.join(destination_directory, os.path.basename(image_key))
        s3.download_file('class-10-data', image_key, local_file_path) #Add your S3 Bucket name here.
        print(f"Downloaded {image_key}")
    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found. Make sure you have configured your credentials.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print(f"Image {image_key} not found in the S3 bucket.")
        else:
            print(f"Error downloading {image_key}: {e}")

print("Download process completed.")


