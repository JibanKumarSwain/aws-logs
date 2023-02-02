# upload logs in s3 after 24h delete all logs help of python

# Here's a basic example of how to upload logs to Amazon S3 and delete them after 24 hours using the Boto3 library in Python:


import boto3
import datetime

# Connect to S3
s3 = boto3.client("s3")

# Upload the log file to S3
s3.upload_file("logs.txt", "log-bucket", "logs/logs.txt")

# Check if the file is older than 24 hours
file_creation_time = s3.head_object(Bucket="log-bucket", Key="logs/logs.txt")["LastModified"]
time_difference = datetime.datetime.now(datetime.timezone.utc) - file_creation_time

if time_difference.total_seconds() > 24 * 60 * 60:
    # Delete the log file from S3
    s3.delete_object(Bucket="log-bucket", Key="logs/logs.txt")





#This code example uploads a file named "logs.txt" to an S3 bucket named "log-bucket" in a folder named "logs". It then uses the head_object method to retrieve the LastModified time of the file and calculates the difference between the current time and the file creation time. If the difference is greater than 24 hours, the file is deleted using the delete_object method.

#Note: This is just a basic example and may not be suitable for all use cases. You should modify it to fit your specific requirements and test it thoroughly before using it in production.