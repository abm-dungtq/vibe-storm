# Standalone Execution Bridge

How to take the output of `vibe-storm` and immediately build it in your favorite AI coding environment.

---

## 1. Executing in Cursor IDE

1. Open your project directory in Cursor.
2. In the Composer window (`Cmd + I` or `Ctrl + I`), set mode to **Agent**.
3. Paste the generated **48h Sprint Prompt Pack**:
   ```text
   You are building the MVP for [Project Name].
   Read the Vibe Working contract below and implement the single happy path:
   [PASTE VIBE PITCH & WEDGE]
   Rules:
   - Modern Next.js App Router + TypeScript + Tailwind CSS.
   - Use Lucide icons and shadcn/ui patterns.
   - No multi-tenancy or complex role auth in this pass.
   - Deliver a functioning UI with simulated/mocked backend API first.
   ```
4. Let Cursor scaffold the files and review the diffs.

---

## 2. Executing in Claude Code

Run inside your terminal:
```bash
claude "I want to build an MVP for [Project Name]. Here is the 48h sprint spec: [PASTE SPEC]. Please create the project structure and build the core functionality step by step."
```

---

## 3. Executing in Antigravity / Gemini CLI

Within the Antigravity IDE:
- Create an implementation plan or prompt the model directly with the Vibe Pitch and 48-hour sprint roadmap.
- Use built-in terminal tools to run `npx create-next-app@latest` and install necessary packages.

---

## 4. Minimal Payment Integration Recipes

### Stripe Checkout (One-time or Subscription)
- Use standard Next.js route handler (`app/api/checkout/route.ts`).
- Create a Stripe checkout session with `stripe.checkout.sessions.create()`.
- Redirect client using URL returned from the session.

### VietQR / SePay (Vietnam Market)
- Generate dynamic VietQR images with account number, bank bin, and amount.
- Set up a webhook endpoint (`app/api/webhooks/sepay/route.ts`) to verify incoming transactions via transaction content regex.
