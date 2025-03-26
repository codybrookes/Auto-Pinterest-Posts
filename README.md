# Auto-Pinterest-Posts Project

## Objective

In this project, I learned the fundamentals of using python, API's, and JSON to create an automated process of creating and scheduling pinterest posts for any business or personal use. 

### Skills Learned

- Basic understanding of fundamental python concepts.
- Proficiency in analyzing and interpreting command logs.
- Ability to learn how to integrate different API's into python code to generate files and spreadsheets. 
- Development of critical thinking and problem-solving skills command logs. 

### Toolstack Used

- Chat Gpt(OpenAI API) - Generates engaging captions & hashtags. 
- Pinterest Trends API - Pulls trending keywords from pinterest and allows auto scheduling for approved posts at the best times. 
- Canva API - Auto generates Images
- Approval storage systems - Google Sheets
- Zapier - Sends posts to your approval system.

## Steps

1. Define The AI Workflow
- AI generates Pinterest Posts (image + seo friendly caption + hashtags)
- Posts are saved for approval in Google Sheets
- You approve the posts manually
- AI then schedules and publishes the approved posts
2. Build The AI System
- Set Up Content Creation AI
    - Create OpenAI Account
    - Use Chatgpt prompts to generate Pinterest texts
    - Store Results into a Google Sheets for manual approval
- Automate Image Generation
    - Create Canva Account and enable Canva API
    - Design Pinterest templates for Etsy shop
    - AI fills in the text and product images automatically
    - Save completed images in Google Drive
- Set Up Approval System
    - Use Zapier to send AI generated posts to google sheets
    - Once you approved a post it triggers the next step
- Automate Posting to Pinterest
    - Use Pinterest API to schedule posts
    - Connect Zapier to automatically post only approved content
    - AI selects the best time to post based on engagement data
3. Test & Optimize
- Run a few tests to post manually to make sure it all works
- Adjust posts info for higher engagement
- Monitor Pinterest analytics to track conversions to Etsy 
