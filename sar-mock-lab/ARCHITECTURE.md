# Architecture Notes - Example Web Application (AWS)

## High-level components
- ALB -> ECS (web) -> RDS (db)
- S3 buckets for logs
- IAM roles for services, developers, and CI/CD
- CloudTrail & Config enabled in the account(s)

## Trust boundaries & data flows
- User -> ALB (TLS) -> ECS (container) -> RDS (private subnet)
- ALB and public subnets are the primary internet-facing boundary
- Data classification: PII in RDS (encrypted at rest), logs in S3 (sensitive)

## Diagram (ASCII - substitute with real diagram in repo or README)
User ---> [ALB] ---> [ECS (app)] ---> [RDS - private]
                  \
                   -> [S3 - logs]
