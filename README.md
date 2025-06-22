# Scheduled Lambda Maintenance Job (Log Archival)

This project demonstrates a scheduled AWS Lambda function used for basic server maintenance. The Lambda connects to an EC2 instance using AWS Systems Manager (SSM), retrieves a system log file (`/var/log/syslog`), and uploads it to an S3 bucket. The function is triggered daily via an EventBridge rule.

## Features

- AWS Lambda
- Amazon EventBridge (CloudWatch Events)
- SSM (Systems Manager)
- Amazon S3
- CloudWatch Logs
- Python (Boto3)

## Skills Demonstrated

- Event-driven automation
- IAM Role management
- Remote command execution
- S3 and Lambda integration
- Python scripting for AWS

## Further Automation

This project could also be implemented using CloudFormation to deploy the Lambda function, schedule, and permissions automatically. The same logic can be extended to rotate logs, run patch commands, or copy daily backups.

## Environment Variables

- `i-088bd4f45a3c32779` – The target EC2 instance ID
- `ec2-daily-backups-kaiden` – S3 bucket for uploaded logs
