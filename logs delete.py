import boto3
import datetime

# Connect to S3
s3 = boto3.client("s3")

# Upload the log file to S3
with open("logs.txt", "rb") as file:
    s3.upload_fileobj(file, "log-bucket", "logs/logs.txt")

# Get the log file's creation time
log_file = s3.head_object(Bucket="log-bucket", Key="logs/logs.txt")

file_creation_time = log_file["LastModified"]

time_difference = datetime.datetime.now(datetime.timezone.utc) - file_creation_time

if time_difference.total_seconds() > 24 * 60 * 60:
    # Delete the log file from S3
    s3.delete_object(Bucket="log-bucket", Key="logs/logs.txt")
