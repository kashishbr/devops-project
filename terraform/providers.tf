terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.3.0"

  backend "s3" {
    bucket = "devops-project-tfstate-kashb"
    key    = "terraform.tfstate"
    region = "ca-central-1"
  }
}

provider "aws" {
  region = var.aws_region
}