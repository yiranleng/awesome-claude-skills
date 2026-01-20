---
name: weekly-report
description: Generate formatted weekly work reports from Confluence pages and send via Gmail. Use when the user asks to create weekly reports, work summaries, status updates from Confluence content, or needs to generate and send weekly email reports with sections like Highlights, Others, and Next Week Plan.
---

# Weekly Report Generator

## Overview

This skill helps generate formatted weekly work reports by extracting content from Confluence pages and formatting them into professional email reports. It can automatically open Gmail and populate the email draft.

## Fixed Configuration

- **Recipient (收件人)**: ke.wang
- **Sender (发件人)**: xiaoxu.wu

These values are fixed and should be used automatically without asking the user.

## Workflow

### 1. Collect Confluence Links

User will provide **TWO Confluence page URLs**:
- **本周（This Week）**: Current week's work content
- **下一周（Next Week）**: Next week's work content

Example format:
- `https://confluence.shopee.io/pages/viewpage.action?pageId=3050869460` (本周)
- `https://confluence.shopee.io/pages/viewpage.action?pageId=3050871438` (下周)

**Important**: Each time the skill is used, user will provide NEW Confluence URLs. Always ask for both pages.

### 2. Check Authentication

Before fetching Confluence content, check if the user needs to log in:
- If pages require authentication, prompt user to log in first
- Wait for user confirmation before proceeding

### 3. Fetch Confluence Content

Fetch content from BOTH Confluence pages:

```bash
# Fetch this week's content
python scripts/fetch_confluence.py <this_week_url> --output this_week.json

# Fetch next week's content  
python scripts/fetch_confluence.py <next_week_url> --output next_week.json
```

**Note**: If authentication fails, prompt user to log in via browser first, then continue.

### 4. Analyze and Categorize Content

**CRITICAL CATEGORIZATION RULES:**

#### Identify Content Sources
- **From PM (Product Manager)** → **Highlight** section as "Key Projects"
- **Everything else** → **Others** section

#### Determine Time-based Sections
- **This week's Confluence page** → Use for **Highlight** and **Others** sections (已完成/进行中的工作)
- **Next week's Confluence page** → Use for **Next Week Plan** section (计划要做的工作)

#### Content Classification Guidelines

**Highlight Section:**
- Only include tasks/projects that come from PM requirements
- Format: Organize by project category/team
  - Example: "**Key Projects - RAM**", "**Key Projects - Metamart**"
- Include: Major features, significant deliverables, important milestones
- Look for keywords: "Requirements", "Feature", "Project", "PRD", "Planning"

**Others Section:**
- Include all non-PM work from this week's page
- Examples: Testing, bug fixes, technical debt, meetings, reviews, documentation
- Format: Group related items
- Use `>` prefix for grouping

**Next Week Plan Section:**
- Extract planned work from next week's Confluence page
- Include: Upcoming features, scheduled tasks, planned development
- Consider dates/deadlines mentioned in the content

### 5. Handle Various Confluence Formats

Confluence content may vary in format but will contain similar information:
- Tasks and subtasks (各种任务项)
- Progress indicators (进度情况: 80%, 90%, Done, In Progress, etc.)
- Dates and deadlines
- Links to PRDs, documents
- Owner/assignee information

**Flexible parsing approach:**
- Don't expect fixed structure
- Extract key information: task names, status, dates, context
- Identify PM requirements by: source, tags, or explicit mentions
- Use date context to determine timing (this week vs next week)

See `references/content-analysis.md` for detailed analysis patterns.

### 6. Generate Email Report

After categorizing all content, generate the formatted report. The report should be naturally written in Chinese or English based on content language, but follow the standard structure.

### 7. Open Gmail Draft

After generating the report, automatically open Gmail with the content:

```bash
python scripts/open_gmail.py --subject "Weekly Report" --body-file report.txt --to "ke.wang@shopee.com"
```

This will:
- Open Gmail in the default browser
- Create a new compose window with pre-filled content
- Pre-fill recipient as ke.wang@shopee.com
- Leave the draft ready for user to review and send

## Report Format Guidelines

### Section Hierarchy

```
Greeting + Introduction
↓
Highlight (Major Items)
  • Category 1
    - Project 1
    - Project 2
  • Category 2
    - Project 3
↓
Others (Additional Items)
  > Group 1
  > • Sub-item 1
  > • Sub-item 2
↓
Next Week Plan
  • Planned Item 1
  • Planned Item 2
↓
Closing + Signature
```

### Formatting Rules

1. **Highlight section**: Use `•` for categories, `-` for projects
2. **Others section**: Use `>` for grouping, `>•` for items
3. **Next Week Plan**: Use `•` for action items
4. **Emphasis**: Bold important keywords (e.g., `**Key Projects - RAM**`)
5. **Spacing**: Add blank lines between major sections

## Example Usage

**User:** "帮我生成本周的工作周报"

**Assistant Workflow:**
1. **Ask for both Confluence URLs**: "请提供本周和下周的Confluence链接"
2. **Check authentication**: Verify user is logged in to Confluence
3. **Fetch content from both pages**: 
   - This week's page (for Highlight + Others)
   - Next week's page (for Next Week Plan)
4. **Analyze content with categorization rules**:
   - Identify PM requirements → Highlight (Key Projects)
   - Identify other work → Others
   - Extract next week's tasks → Next Week Plan
5. **Generate formatted report**: 
   - Use recipient: "Ke Wang"
   - Use sender: "xiaoxu.wu" or "Xiaoxu Wu"
6. **Open Gmail**: Launch browser with pre-filled draft to ke.wang@shopee.com

## Key Reminders

1. **Always request TWO Confluence URLs** (this week + next week)
2. **NEW URLs each time** - don't reuse old links
3. **PM requirements = Key Projects** (Highlight section)
4. **Everything else = Others** (except next week's content)
5. **Handle flexible formats** - Confluence structure varies
6. **Use date context** to determine timing
7. **Fixed recipient**: ke.wang (Ke Wang) - do NOT ask user
8. **Fixed sender**: xiaoxu.wu (Xiaoxu Wu) - use automatically

## Important References

### Content Analysis Guide
For detailed guidance on analyzing Confluence content and categorizing into report sections, see:

**`references/content-analysis.md`**

This reference includes:
- Understanding the two-week structure
- Identifying PM requirements vs other work
- Handling various Confluence formats
- Complete example analysis with reasoning

**When to read**: Before analyzing Confluence content for the first time, or when unsure about categorization.

## Scripts Reference

### fetch_confluence.py
Fetches content from Confluence pages with authentication support.

**Usage:**
```bash
python scripts/fetch_confluence.py <url> --output <file.json>
```

### generate_report.py
Transforms categorized content into structured weekly report format.

**Usage:**
```bash
python scripts/generate_report.py --recipient "Name" --highlights "..." --others "..." --next-week "..."
```

### open_gmail.py
Opens Gmail composer with pre-filled email content.

**Usage:**
```bash
python scripts/open_gmail.py --subject "Weekly Report" --body-file report.txt
```

## Assets Reference

### config.json
Fixed configuration for recipient and sender information:
- Recipient: Ke Wang (ke.wang@shopee.com)
- Sender: Xiaoxu Wu (xiaoxu.wu@shopee.com)

### email_template.txt
Standard email template with pre-filled recipient and sender names.
