import boto3
import sys
from datetime import datetime

# Configuration
REPO_NAME = "devops-project-app"
REGION = "ca-central-1"
KEEP = 5

def cleanup_ecr():
    print(f"🧹 Starting ECR cleanup for repository: {REPO_NAME}")
    print(f"📦 Keeping {KEEP} most recent images")

    # Connect to ECR
    ecr = boto3.client('ecr', region_name=REGION)

    # Get all images
    response = ecr.describe_images(repositoryName=REPO_NAME)
    images = response['imageDetails']

    print(f"📊 Total images found: {len(images)}")

    if len(images) <= KEEP:
        print("✅ Nothing to clean up — image count is within limit")
        return

    # Sort by date oldest first
    images.sort(key=lambda x: x['imagePushedAt'])

    # Get images to delete
    images_to_delete = images[:len(images) - KEEP]

    print(f"🗑️  Deleting {len(images_to_delete)} old images...")

    # Delete old images
    image_ids = [{'imageDigest': img['imageDigest']} for img in images_to_delete]

    ecr.batch_delete_image(
        repositoryName=REPO_NAME,
        imageIds=image_ids
    )

    print(f"✅ Cleanup complete!")
    print(f"📦 Images remaining: {KEEP}")
    print("\n🗑️  Deleted images:")
    for img in images_to_delete:
        pushed_at = img['imagePushedAt'].strftime("%Y-%m-%d %H:%M:%S")
        print(f"  - {img['imageDigest'][:20]}... pushed at {pushed_at}")

if __name__ == "__main__":
    cleanup_ecr()