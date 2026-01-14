import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-3")


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        # just instances with prod tag
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        try:
            new_snapshot = ec2_client.create_snapshot(
                VolumeId=volume['VolumeId']
            )
            print(new_snapshot)
        except Exception as ex:
            print(f"ERROR/ {ex} in {volume['VolumeId']}")

schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()
