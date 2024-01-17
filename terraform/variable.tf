variable "region" {
  description = "aws region"
  default     = "us-east-2"
}

variable "account_id" {
  default = 727477891012
}

variable "prefix" {
  description = "objects prefix"
  default     = "de-okkus"
}

# Prefix configuration and project common tags
locals {
  glue_bucket = "${var.prefix}-aws-glue-scripts-${var.account_id}"
  prefix      = var.prefix
  common_tags = {
    Environment = "dev"
    Project = "okonomikus"
  }
}

variable "bucket_names" {
  description = "s3 bucket names"
  type        = list(string)
  default = [
    "bronze",
    "silver",
    "gold",
    "aws-glue-scripts"
  ]
}

variable "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with this job."
  default     = null
}