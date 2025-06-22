import boto3
import os
import time

ssm = boto3.client('ssm')
s3 = boto3.client('s3')

INSTANCE_ID = os.environ['i-088bd4f45a3c32779']
BUCKET_NAME = os.environ['ec2-daily-backups-kaiden']
FILE_PATH = "/var/log/syslog"
S3_KEY = "backups/syslog.txt"

def lambda_handler(event, context):
    print(f"Running command on instance {INSTANCE_ID}")

    response = ssm.send_command(
        InstanceIds=[INSTANCE_ID],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': [f'cat {FILE_PATH}']},
    )

    command_id = response['Command']['CommandId']
    time.sleep(2)  # Wait for command to run

    output = ssm.get_command_invocation(
        CommandId=command_id,
        InstanceId=INSTANCE_ID
    )

    if output['Status'] == 'Success':
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=S3_KEY,
            Body=output['StandardOutputContent']
        )
        return {"status": "File uploaded"}
    else:
        return {"status": "Command failed", "details": output}
