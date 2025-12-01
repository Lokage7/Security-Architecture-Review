# SAR Mock Lab - Governance, Risk & Compliance (GRC) Interview Prep
**Author:** Sharaden Cole
**Purpose:** Step-by-step lab to simulate a Security Architecture Review (SAR) and maintain a Cybersecurity Risk Register. Use this repo to reference during interviews, reproduce the lab, and expand into a portfolio project.

## Overview
This lab walks through a mock SAR on an AWS-hosted application. It follows a realistic process you can present in interviews:
1. Define scope
2. Map architecture (data flows & trust boundaries)
3. Identify assets, threats, and quantify risk
4. Review and test security controls
5. Document findings (SAR deliverable & risk register)
6. Provide remediation recommendations
7. Reflect on business impact and next steps

The repo includes templates, example findings, scripts (audit checklist examples), and a SAR report template you can point to during interviews.

## Contents
- `README.md` - this file
- `SAR_Template.md` - SAR report template
- `risk_register_example.csv` - example risk register
- `findings/` - example findings and remediation notes
- `scripts/aws_audit_checks.py` - example local script with AWS CLI checks (safe, non-destructive commands)
- `ARCHITECTURE.md` - high level architecture diagram and notes
- `LICENSE` - MIT

## How to use
1. Clone locally or download the zip.
2. Update `ARCHITECTURE.md` with your system diagram and notes.
3. Run non-destructive audit commands locally (see `scripts/aws_audit_checks.py` and README guidance).
4. Populate `risk_register_example.csv` with your prioritized findings.
5. Use `SAR_Template.md` to assemble a short SAR deliverable for interviews.

**Note:** This lab is intentionally environment-agnostic. Do not run destructive scripts against production systems. Replace example resource names with sandbox/test accounts when practicing.
