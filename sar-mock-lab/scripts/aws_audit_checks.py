#!/usr/bin/env python3
"""
aws_audit_checks.py - non-destructive AWS audit checklist examples
Requires: AWS CLI configured with profile for a non-production account
This script demonstrates safe AWS queries you can run during a mock SAR.
"""

import subprocess, json, sys

def run(cmd):
    try:
        print("\n$ " + " ".join(cmd))
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8')
        print(out[:1000])
    except Exception as e:
        print("ERROR:", e)

def list_trails():
    run(["aws", "cloudtrail", "describe-trails"])

def check_s3_public(bucket):
    run(["aws", "s3api", "get-bucket-acl", "--bucket", bucket])

def list_iam_policies():
    run(["aws", "iam", "list-policies", "--scope", "Local"])

def main():
    print("Non-destructive AWS audit checklist - example outputs (mock)")
    list_trails()
    # Example: check_s3_public("app-logs")  # uncomment and replace with sandbox bucket
    list_iam_policies()

if __name__ == '__main__':
    main()
