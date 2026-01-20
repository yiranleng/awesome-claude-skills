# Content Analysis Guide for Weekly Reports

This guide provides detailed instructions for analyzing Confluence content and categorizing it into weekly report sections.

## Table of Contents

1. [Understanding the Two-Week Structure](#understanding-the-two-week-structure)
2. [Identifying PM Requirements (Key Projects)](#identifying-pm-requirements)
3. [Categorizing Other Work](#categorizing-other-work)
4. [Extracting Next Week Plan](#extracting-next-week-plan)
5. [Handling Various Formats](#handling-various-formats)
6. [Example Analysis](#example-analysis)

---

## Understanding the Two-Week Structure

User provides TWO Confluence pages each time:

```
┌─────────────────────────────────────────────────────┐
│  This Week's Page (本周)                            │
│  ↓                                                   │
│  Use for: Highlight + Others sections               │
│  (已完成/进行中的工作)                               │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Next Week's Page (下周)                            │
│  ↓                                                   │
│  Use for: Next Week Plan section                    │
│  (计划要做的工作)                                    │
└─────────────────────────────────────────────────────┘
```

**Critical**: Do NOT mix content between pages. Each page serves a specific purpose in the report structure.

---

## Identifying PM Requirements (Key Projects)

### What are PM Requirements?

Tasks, features, or projects that originate from Product Manager (PM) requests. These should be highlighted as key projects in the weekly report.

### How to Identify

Look for these **indicators**:

#### 1. Explicit Mentions
- "PM requirement"
- "Product requirement"
- "PRD" (Product Requirements Document)
- "Feature request from PM"
- "PM-xxx" (PM name or ID)

#### 2. Context Clues
- Requirements with high business impact
- New features or major enhancements
- Items linked to product roadmap
- Tasks with PRD documents attached
- Strategic initiatives

#### 3. Source/Assignor
- Tasks assigned by PM team members
- Items from product planning meetings
- Requirements from product backlog

### Classification Strategy

```
IF task mentions:
  - "PM requirement" OR
  - "PRD" OR  
  - "Product feature" OR
  - Links to PRD document OR
  - Assigned by known PM
THEN:
  Category = "Key Projects" (Highlight section)
  Group by: Project/Team name
ELSE:
  Category = "Others" section
```

### Example Categorization

**This is a Key Project** ✓
```
- DataSuite Asset Profile Extraction (ChatBI scenario) TD & Planning
  Source: PM requirement PRD-12345
  Owner: Product Team
```

**This is NOT a Key Project** ✗
```
- Fix bug in user login flow
  Source: Bug report
  Owner: Engineering Team
```

---

## Categorizing Other Work

### What Goes in "Others"?

Everything from **this week's page** that is NOT a PM requirement:

#### Common Types:

1. **Testing & QA**
   - "Testing XX feature - 80% complete"
   - "QA for YY module"
   - "Integration testing"

2. **Bug Fixes**
   - "Fixed XX bug"
   - "Resolved YY issue"

3. **Technical Work**
   - "Refactoring ZZ module"
   - "Performance optimization"
   - "Code review"

4. **Meetings & Alignment**
   - "Requirements alignment meeting"
   - "Technical discussion"
   - "Team sync"

5. **Documentation**
   - "Updated technical docs"
   - "API documentation"

### Grouping Strategy

Group related items together for better readability:

```
Others:
> Q4 Requirements QA Testing
> - Alarm Center Testing 80%
> - Asset Transfer Testing 90%

> Q1 Requirements Alignment
> - Kafka Quota Requirement (PRD)
> - DGC Q1 Requirement Alignment
```

---

## Extracting Next Week Plan

### Source

Extract from **next week's Confluence page** ONLY.

### What to Include

- Planned features to develop
- Scheduled reviews or meetings
- Testing activities
- Requirements to analyze
- Any task marked for next week

### Date-Based Extraction

Look for:
- Explicit dates (e.g., "2026-01-27 to 2026-01-31")
- "Next week" mentions
- "Planned for" statements
- Tasks in "Todo" or "Planned" status on next week's page

### Format

Use simple bullet points:

```
Next Week Plan:
- RAM Q4 features Develop & Testing
- DataService & RAM & Metamart Q1 features PRD Review Develop  
- Metamart User Profile TD
```

---

## Handling Various Formats

Confluence content appears in many formats. Here's how to handle them:

### Format 1: Structured Tasks with Status

```
Confluence Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Task: DataSuite Asset Profile Extraction
Status: In Progress (80%)
Type: PM Requirement
Owner: John Doe
Due: 2026-01-20
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analysis:
- Type = "PM Requirement" → Highlight
- Status shows progress
- Extract: "DataSuite Asset Profile Extraction (ChatBI scenario) TD & Planning"
```

### Format 2: Bullet Lists

```
Confluence Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This Week:
• Testing Alarm Center feature - 80%
• Asset Transfer testing - 90%  
• Meeting with PM for Q1 planning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analysis:
- Testing items → Others
- PM meeting → Could be Key Projects if related to requirements
```

### Format 3: Tables

```
Confluence Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Task Name              | Status | Type        |
|------------------------|--------|-------------|
| Feature A Development  | Done   | PM Req      |
| Bug Fix #123          | Done   | Engineering |
| Code Review           | Done   | Team        |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analysis:
- Row 1: "PM Req" → Highlight
- Row 2-3: → Others
```

### Format 4: Unstructured Text

```
Confluence Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Worked on DataSuite profile extraction this week as requested by PM.
Also did some testing on the alarm center and fixed a few bugs.
Next week planning to work on Metamart user profile design.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analysis:
- "requested by PM" → Highlight: DataSuite profile extraction
- "testing" and "bugs" → Others
- "Next week planning" → Next Week Plan
```

### Key Parsing Principles

1. **Be flexible**: Don't expect rigid structure
2. **Look for keywords**: PM, requirement, testing, bug, etc.
3. **Use context**: Task relationships and mentions
4. **Preserve meaning**: Extract the essence, not exact text
5. **Group logically**: Combine related items

---

## Example Analysis

### Scenario

User provides two Confluence pages:

**This Week's Page:**
```
Week of Jan 13-19, 2026

Projects:
1. DataSuite Asset Profile Extraction
   - Type: PM Requirement
   - Status: Planning & TD complete
   - Next: Development phase

2. CPO Security Requirements
   - Type: PM Requirement  
   - Status: First batch shared with CPO team
   - Ongoing work

3. Metamart Diana Topic POC
   - Type: Internal research
   - Status: POC complete

Other Work:
- Q4 Alarm Center Testing: 80% complete
- Q4 Asset Transfer Testing: 90% complete
- Q1 Requirement alignment meetings
```

**Next Week's Page:**
```
Week of Jan 20-26, 2026

Planned Work:
1. RAM Q4 features development and testing
2. DataService Q1 features PRD review
3. Metamart User Profile Technical Design
4. JDK 21 upgrade investigation
```

### Analysis Result

**Highlight Section:**
```
**Key Projects - RAM**
- DataSuite Asset Profile Extraction (ChatBI scenario) TD & Planning
- CPO Security Requirements Support OnGoing (Already shared with CPO team with the first batch data)

**Key Projects - Metamart**  
- Diana Topic POC
```

**Others Section:**
```
> Q4 Requirements QA Testing
> - Alarm Center Testing 80%
> - Asset Transfer Testing 90%

> Q1 Requirements
> - DGC Q1 Requirement Alignment
```

**Next Week Plan:**
```
- RAM Q4 features Develop & Testing
- DataService Q1 features PRD Review Develop
- Metamart User Profile TD
- JDK 21 upgrade investigation
```

### Reasoning

1. **Items 1-2 from this week** → PM Requirements → Highlight under "Key Projects - RAM"
2. **Item 3 from this week** → Internal work but significant → Highlight under "Key Projects - Metamart"
3. **Testing items** → Others (grouped as "Q4 Requirements QA Testing")
4. **Q1 meetings** → Others (grouped as "Q1 Requirements")
5. **All planned work from next week's page** → Next Week Plan

---

## Tips for Accurate Analysis

1. **Read both pages fully** before categorizing
2. **Look for PM signals** explicitly
3. **When in doubt**, ask user for clarification on whether something is a PM requirement
4. **Preserve user's grouping** when it makes sense (e.g., by project, by quarter)
5. **Be concise but clear** in extracted descriptions
6. **Maintain consistency** in naming (e.g., always "RAM Q4" not sometimes "Q4 RAM")

---

## Common Pitfalls to Avoid

❌ **DON'T** mix content from this week and next week pages
❌ **DON'T** put non-PM work in Highlight just because it's important
❌ **DON'T** over-simplify - preserve context and details
❌ **DON'T** ignore progress indicators (80%, Done, etc.)
❌ **DON'T** lose project groupings (RAM, Metamart, etc.)

✅ **DO** separate by PM vs non-PM first
✅ **DO** use date context to determine timing
✅ **DO** preserve the user's terminology and project names
✅ **DO** group related items logically
✅ **DO** maintain professional tone in final output
