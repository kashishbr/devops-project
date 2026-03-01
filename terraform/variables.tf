variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "ca-central-1"
}

variable "project_name" {
  description = "Name of the project, used to tag all resources"
  type        = string
  default     = "devops-project"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}