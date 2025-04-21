# main.tf

# Define the required Terraform version
terraform {
    required_version = ">= 1.0.0"
}

# Provider configuration (example: HashiCorp's random provider)
provider "random" {}

# Resource to generate a random string
resource "random_string" "hello_world" {
    length  = 12
    special = false
    upper   = true
}

# Output the generated string
output "hello_world_output" {
    value = random_string.hello_world.result
}