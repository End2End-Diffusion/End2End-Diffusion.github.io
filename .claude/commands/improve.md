# Landing Page Improvement Command

You are tasked with improving the End2End-Diffusion landing page. Follow these steps carefully.

## CRITICAL CONSTRAINTS - READ FIRST

### Files You CAN Modify:
- `/index.html` - The landing page HTML
- `/static/css/landing.css` - Landing page styles
- `/static/js/landing.js` - Landing page JavaScript
- `/landing-todos.md` - Task tracking file

### Files You MUST NEVER Modify:
- ANY file in `/irepa/` directory
- ANY file in `/repa-e/` directory
- ANY file in `/repa-e-t2i/` directory
- ANY file in `/static/css/paper-layout.css`
- ANY file in `/static/css/paper-theme.css`
- ANY other project subdirectories

If you find yourself needing to modify any forbidden file, STOP and report why.

### Style Guidelines:
- Maintain professional academic/research aesthetic
- Keep blue accent color (#2563eb for light mode, #60a5fa for dark mode)
- Use Inter for body text, Crimson Pro for headings
- No fancy animations - subtle transitions only (0.3s ease max)
- Preserve dark/light theme toggle functionality
- Keep responsive design working (768px breakpoint)
- Maintain Tailwind CSS utility approach where used
- Follow existing code patterns and conventions

---

## Execution Steps

### Step 1: Read Current State
Read the following files to understand current state:
1. `/landing-todos.md` - to find the next task
2. `/index.html` - current HTML structure
3. `/static/css/landing.css` - current styles
4. `/static/js/landing.js` - current functionality

### Step 2: Select Task
- Pick the **highest priority incomplete task** from landing-todos.md
- Tasks are organized by priority (High > Medium > Low)
- If all tasks are complete, **add new improvement ideas** and continue iterating
- You are encouraged to discover and add new improvements as you work
- There is no limit - keep improving the landing page indefinitely

### Step 3: Plan Implementation
- Design the change keeping style guidelines in mind
- Ensure changes ONLY affect landing page files
- Keep changes small and focused (one task per run)
- Consider both light and dark theme compatibility

### Step 4: Implement
- Make the necessary code changes
- VERIFY: Double-check you are not modifying any project page files
- Test that changes work in both light and dark themes mentally

### Step 5: Validate
- Run `git diff` to confirm only allowed files were changed
- Check the diff output for any of these patterns:
  - `irepa/` - VIOLATION
  - `repa-e/` - VIOLATION
  - `repa-e-t2i/` - VIOLATION
- If any forbidden files appear, REVERT all changes and STOP

### Step 6: Update Todos
- Mark the completed task with `[x]` in landing-todos.md
- Add completion date
- Add any new tasks discovered during implementation
- Note any issues encountered

### Step 7: Commit
- Stage only the allowed files:
  ```bash
  git add index.html static/css/landing.css static/js/landing.js landing-todos.md
  ```
- Create commit with format: `landing: <brief description>`
- Examples:
  - `landing: add semantic HTML landmarks`
  - `landing: improve article card hover states`
  - `landing: add lazy loading to images`
- Do NOT push to remote (let user review first)

---

## Quality Checklist

Before committing, verify ALL of these:
- [ ] Only landing page files modified (index.html, landing.css, landing.js, landing-todos.md)
- [ ] No project pages touched (irepa/, repa-e/, repa-e-t2i/)
- [ ] Dark theme still works correctly
- [ ] Light theme still works correctly
- [ ] Mobile responsive design intact
- [ ] Filter tabs still function
- [ ] Theme toggle still works
- [ ] No obvious errors introduced
- [ ] Code follows existing patterns and style

---

## If Something Goes Wrong

1. If you accidentally modified a project page file:
   ```bash
   git checkout -- irepa/ repa-e/ repa-e-t2i/
   ```

2. If you need to completely reset:
   ```bash
   git checkout -- .
   ```

3. If you're unsure about a change, skip it and move to the next task

---

## Remember
- One focused task per run
- Minimal, clean changes only
- Professional research aesthetic
- When in doubt, don't modify


# FIXED RULES - DO NOT MODIFY
- Limit to just improving the landing page
- Do not modify any project pages (irepa/, repa-e/, repa-e-t2i/)
