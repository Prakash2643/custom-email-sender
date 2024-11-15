Objective
Create a custom email-sending application with a front-end dashboard that performs the following tasks:

Reads data from a Google Sheet or CSV file for email customization.

Allows users to connect their email account.

Accepts a customizable prompt for personalizing each email.

Customizes and sends emails using an LLM or other content-generation approach.

Displays real-time status and analytics for sent emails.

Provides email scheduling, throttling, and delivery tracking using an Email Service Provider (ESP) integration.

Detailed Requirements
1. Data Connection
Input Data: Allow users to connect a Google Sheet or upload a CSV file containing email data with columns like Company Name, Location, Email, and Products.

2. Email Integration
Account Connection: Provide an option for users to connect their email account for sending emails using either a personal account (e.g., Gmail, Outlook) or a configured ESP.

Implementation Tips: Use OAuth2 for secure email service connections or provide configurations for SMTP/ESP integration.

3. Customizable Prompt Box for Email Content
Prompt Box: Allow users to input a customizable prompt with placeholders, such as {Company Name} or {Location}, which will be replaced by actual values from each row in the dataset.

4. Column Detection and Dynamic Field Replacement
Auto-detect Columns: Automatically detect columns in the dataset and allow users to insert these fields as placeholders in the prompt box.

5. Email Customization and Sending
Content Generation: For each row, generate a custom message based on the user’s prompt and row data. Use LLMs API to generate a response.

Email Sending: Customize the content for each recipient and send the email.

6. Email Scheduling and Throttling
Scheduling: Allow users to schedule emails for specific times. Provide options to schedule all emails for a specific time or stagger them over intervals. If possible, allow setting different schedules for individual or batch emails (e.g., send 50 emails per hour).

Throttling: Provide the option to throttle email sending to stay within provider limits (e.g., send X emails per minute or hour). Include a user-configurable rate-limiting option.

Implementation Tips: Store scheduling data in a database or use in-memory scheduling libraries. Implement a queuing system, such as Celery, or use time-based functions in the chosen framework to manage scheduling and throttling.

7. Real-Time Analytics for Sent Emails
Analytics Dashboard: Provide real-time analytics on sent emails, such as:

Total Emails Sent

Emails Pending

Emails Scheduled

Emails Failed

Response Rate (if available)

Implementation Tips: Use a background job to update email status metrics regularly. Display analytics using charts or counters on the dashboard, updating the data in real-time or at regular intervals.

8. Email Delivery Tracking with ESP Integration
ESP Integration: Integrate with an Email Service Provider (ESP) such as SendGrid, Amazon SES, or Mailgun to track email delivery. Display delivery statuses, such as Delivered, Opened, Bounced, and Failed, on the dashboard.

Example ESPs: Use the SendGrid API for delivery tracking and to access event-based data.
