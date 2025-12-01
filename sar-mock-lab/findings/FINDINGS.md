# Findings - Example Mock SAR Lab

## Finding 1 - Public S3 logs
**Resource:** s3://app-logs
**Severity:** High
**Evidence:** `aws s3api get-bucket-acl --bucket app-logs` returned public READ grants.
**Risk:** Sensitive logs could be accessed publicly, leading to data exposure and regulatory risk.
**Recommendation:** Set bucket ACL to private, add bucket policy restricting access, enable SSE-KMS, enable logging to centralized bucket.
**Owner:** CloudOps
**Target Date:** 2025-12-15

## Finding 2 - Overly permissive IAM role
**Resource:** arn:aws:iam::123456789012:role/dev-role
**Severity:** Critical
**Evidence:** Policy includes `*` resource and `iam:*` actions in attached policy.
**Risk:** High potential for lateral movement and account takeover.
**Recommendation:** Remove wildcard permissions, apply least privilege, implement role review process and permission boundaries.
**Owner:** IAM Team
**Target Date:** 2025-12-01
