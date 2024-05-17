# Issue Summary:
<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/holberton-system_engineering-devops/master/0x19-postmortem/image.gif" width=100% height=100% />
</p>
- **Duration:** 2 hours (April 5, 2024, 10:00 AM to 12:00 PM PDT)
- **Impact:** The API service was completely down, resulting in a 50% user base unable to access critical functionalities.
- **Root Cause:** A misconfiguration in the database connection pool settings led to excessive resource consumption and service unavailability.

# Timeline:

- 10:00 AM PDT: Issue detected via monitoring alerts showing a spike in error rates.
- Actions taken: Engaged database and backend teams to investigate potential database-related issues due to the high error rates.
- Misleading paths: Initially focused on database performance issues but found no anomalies in database metrics.
- Escalated incident: Elevated to senior backend engineers and database administrators for deeper analysis and troubleshooting.
- 12:00 PM PDT: Issue resolved by adjusting database connection pool settings to optimal values, restoring API functionality.

# Root Cause and Resolution:

The root cause was identified as a misconfiguration in the database connection pool settings. The pool was set to allow an excessive number of connections, leading to resource exhaustion and service unavailability. This was fixed by adjusting the connection pool settings to limit the maximum number of connections and optimizing resource allocation.

# Corrective and Preventative Measures:

## Improvements/Fixes:
1. Implement automated monitoring and alerting for database connection pool usage and resource consumption.
2. Conduct regular performance audits and capacity planning to avoid similar resource exhaustion issues in the future.

## Tasks to Address the Issue:
1. Patch database connection pool settings to limit maximum connections and optimize resource allocation.
2. Enhance monitoring and alerting mechanisms to proactively detect and respond to resource exhaustion issues.
3. Conduct post-incident review and analysis to identify any additional vulnerabilities or areas for improvement in the system architecture.

This postmortem analysis highlights the critical impact of misconfigurations on system performance and the importance of proactive monitoring, rapid incident response, and continuous improvement in infrastructure management practices.
