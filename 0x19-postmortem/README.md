# 0x19-postmortem
</hr>
### Duration: 2 hours (12:00 PM - 2:00 PM EST)
<b>Impact:</B> Users were unable to access the checkout page on our e-commerce website, resulting in a loss of potential sales. Approximately 20% of users were affected.

<b>Root Cause:</B> A recent update to the website's payment gateway integration introduced a bug that caused the checkout page to crash under certain circumstances.

### Timeline:

- <i> 12:00 PM </i> - The issue was first detected when our monitoring system alerted us to a spike in 500 errors on the checkout page.
- <i> 12:05 PM </i>- The engineering team was notified of the issue and began investigating.
- <i> 12:10 PM </i> - Initial investigations suggested that the issue was related to the website's database, and the team began examining the database logs and performing database queries to isolate the problem.
- <i> 12:20 PM </i> - Further investigations revealed that the issue was actually related to the payment gateway integration, and the team began examining the payment gateway logs and code.
- <i> 12:40 PM </i> - The team discovered a bug in the payment gateway code that was causing the checkout page to crash under certain conditions.
- <i> 1:00 PM </i> - The incident escalated to senior engineers and the payment gateway provider.
- <i> 1:30 PM </i> - The team worked with the payment gateway provider to develop and implement a fix for the issue.
- <i> 2:00 PM </i> - The issue was resolved, and users were able to access the checkout page again.

### Root Cause and Resolution:

The root cause of the issue was a bug in the website's payment gateway integration code. Specifically, the bug caused the checkout page to crash when users attempted to use a certain type of credit card.

To resolve the issue, the engineering team worked with the payment gateway provider to identify and fix the bug in the integration code. The fix involved updating the code to properly handle the problematic credit card type and ensuring that future updates would not introduce similar bugs.

### Corrective and Preventative Measures:

To prevent similar incidents from occurring in the future, the engineering team has implemented several corrective and preventative measures, including:

Conducting a thorough review of all payment gateway integrations to ensure they are functioning properly and are not susceptible to similar bugs.
Implementing more rigorous testing procedures for updates to the website and its integrations.
Improving monitoring and alerting systems to detect and respond to similar issues more quickly in the future. 
Developing and documenting incident response procedures to ensure that issues are escalated and resolved as quickly and efficiently as possible.

### Tasks to address the issue:

Review and update payment gateway integration code to ensure it is functioning properly.
Develop and implement additional testing procedures for website updates and integrations.
Update monitoring and alerting systems to detect and respond to similar issues more quickly.
Develop and document incident response procedures to ensure issues are resolved as efficiently as possible.

