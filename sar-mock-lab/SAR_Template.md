# Security Architecture Review (SAR) - Mock Project

**System:** Example Web Application (AWS)
**Author:** Sharaden Cole
**Date:** [YYYY-MM-DD]
**Scope:** [Define scope boundaries here]

## Executive Summary
- Brief summary of the system, scope, and top 3 risks (quantified where possible).

## Architecture Overview
Insert high-level diagram and description of data flows and trust boundaries.

## Findings (High-level)
| ID | Resource | Risk Level | Summary | Business Impact | Recommendation |
|----|----------|------------|---------|-----------------|----------------|
| 1  | e.g., web-server | High | Example: Public S3 bucket with sensitive logs | Compliance, data exposure | Restrict bucket policy; enable encryption; add logging |

## Detailed Findings
- For each finding include: affected resource, evidence, risk score, business impact, remediation steps, owner, target date.

## Risk Register Link
Include CSV/central tracking location and reference the risk IDs used above.

## Remediation Plan & Prioritization
Short-term (0-30 days), Medium (30-90 days), Long-term (>90 days).

## Conclusion
Summary of next steps and suggested architecture changes to reduce systemic risk.
