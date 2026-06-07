# How to Set Up This Portfolio in Notion

## Page Hierarchy to Create

```
🏠 [Portfolio Home]  ← public, top-level page
  👋 About Me
  💼 Case Studies
      🔐 Signzy: AI-Powered KYC Onboarding
      🤖 Deloitte: GenAI Contact Center
      🏦 Sapiens: Enterprise Insurance Platform
      🛍️ Iksula: E-commerce Personalization
  🔍 Teardowns
      CRED — Product Teardown
  📁 Artifacts & Work Samples
```

---

## Step-by-Step Setup

### 1. Create the top-level Portfolio Home page

- New page → title: **Shraddha Singh — PM Portfolio**
- Set a cover image (try Unsplash → search "fintech" or "abstract blue")
- Set a page icon (emoji: 🏠 or a person emoji)
- **Enable "Share to web"** → this gives you a public URL to share with hiring managers

### 2. Import each file

For each `.md` file in this folder:

1. Create a new sub-page under the correct parent (see hierarchy above)
2. Either:
   - **Option A (Paste):** Open the `.md` file, copy all content, paste directly into Notion — it preserves most markdown formatting automatically
   - **Option B (Import):** Notion → click `...` menu → Import → Markdown & CSV → select the `.md` file
3. Review after import — tables, callouts, and toggles may need minor adjustment

### 3. Set up the home page as a hub

The home page (`00-home.md`) is designed as a visual hub. After importing:

- Each "→ [Link text]" line should become a **link to the sub-page** (type `@` and search the page name)
- Add a **Divider** block between sections
- Consider adding **callout blocks** for the "At a Glance" section:
  - `/callout` → choose a relevant emoji → paste the key stats

### 4. Make it visually clean (Notion-specific tips)

**Typography:**
- Use `H1` for the main title, `H2` for section headers, `H3` for sub-sections
- Keep body text as default paragraph — don't use small text

**Results / metrics blocks:**
In each case study, format the "Results at a Glance" table as a Notion database (simple table works fine)

**Callout blocks for key insights:**
Wrap key quotes or decisions in callout blocks:
```
💡 Insight: [key learning or decision]
```

**Toggle blocks for detail:**
Consider wrapping the longer "Process" sections in toggles to keep the page scannable:
```
▶ Process (click to expand)
  [full process content]
```

### 5. Upload the artifacts

Upload the actual files from `portfolio/assets/` as attachments in the Artifacts page:
- `ShraddhaSingh JPMC.pdf` — embed directly (Notion renders PDFs inline)
- `Product Requirements Document - CSPM (1).docx` — upload as file block
- `Order Management System Process Diagram.drawio` — upload as file block (Notion can't render drawio natively — consider exporting to PNG first)
- `HydroPod-Revolutionizing-Home-Agriculture (1).pptx` — upload as file block or export key slides to PNG and embed as images

### 6. Sharing settings

**For job applications:**
- Top-level page → Share → Share to web → ON
- Set "Allow duplicate" OFF (prevents people from copying your portfolio)
- Set "Allow comments" OFF (cleaner experience for reviewers)
- Copy the shareable link → use this in your resume, cover letters, and LinkedIn

**For LinkedIn:**
- Add the Notion URL to your LinkedIn profile's "Featured" section
- Also add it to the "Websites" field in your LinkedIn contact info

---

## Notion Formatting Quick Reference

| What | How in Notion |
|---|---|
| Heading 1 | Type `# ` then text, or `/h1` |
| Heading 2 | Type `## ` or `/h2` |
| Callout block | `/callout` |
| Toggle block | `/toggle` |
| Divider | `---` or `/divider` |
| Simple table | `/simple table` |
| File upload | `/file` or drag-and-drop |
| Link to another page | `@` then type the page name |
| Code block | `/code` |

---

## What Hiring Managers Will See

When you share the Notion link, they land on your **Portfolio Home** page. The page is designed to communicate:

1. **In 10 seconds:** Name, domain (Fintech/Insurtech/GenAI), 3 headline metrics, link to case studies
2. **In 2 minutes:** Read one case study of their choice — structured to show product thinking depth
3. **In 5 minutes:** About Me page shows personality, working style, and self-awareness
4. **On demand:** Artifacts for any recruiter who wants to see actual deliverables

The goal is to make every layer richer without making the top layer overwhelming.

---

## Maintenance

- Update **Sapiens case study** every 3–6 months as more results come in (it's a current role)
- Add a **new teardown** every quarter — shows you're constantly thinking about products
- Keep the **home page metrics** current — if you hit a new result, update the "At a Glance" table
- Before sharing with a specific company, check if their domain (Insurtech, Fintech, etc.) is front-loaded on the home page
