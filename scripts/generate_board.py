#!/usr/bin/env python3
import os
import sys
import argparse

def generate_html_board(title, subtitle, output_file="vibe-board.html"):
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(repo_dir, "templates", "vibe-board-template.html")
    
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Default sample content if not provided
    biz_content = f"""
    <div class="grid">
      <div class="card">
        <h3>🎯 The Vibe Pitch</h3>
        <p><strong>{title}</strong></p>
        <p style="color: var(--text-muted);">{subtitle}</p>
      </div>
      <div class="card">
        <h3>🔪 The Wedge & Moat</h3>
        <p>Solves 1 high-friction bottleneck in under 60 seconds. High willingness to pay with zero feature bloat.</p>
        <span class="badge">Pricing: $19 - $49/mo</span>
      </div>
      <div class="card">
        <h3>🧪 Day-1 Smoke Test</h3>
        <p>Send 20 personalized 60-second Loom DMs to niche founders. Target: 3 pre-orders before writing code.</p>
      </div>
    </div>
    """

    mkt_content = """
    <div class="grid">
      <div class="card">
        <h3>🪝 Hook-Offer-Angle</h3>
        <p><strong>Angle:</strong> "Stop spending 4 hours manually editing every weekend."</p>
        <p><strong>Offer:</strong> 1-click transformation in 30 seconds with 100% money-back guarantee.</p>
      </div>
      <div class="card">
        <h3>📍 Watering Holes</h3>
        <ul style="color: var(--text-muted); padding-left: 1.2rem;">
          <li>Relevant niche subreddits (Top 3)</li>
          <li>X / Twitter Indie Hacker community</li>
          <li>Targeted Discord & Telegram operator groups</li>
        </ul>
      </div>
    </div>
    """

    content_content = """
    <div class="grid">
      <div class="card">
        <h3>🎬 Short-Form Video Script</h3>
        <p><strong>Hook (0-3s):</strong> "If you're still doing [X] by hand in 2026, stop."</p>
        <div class="prompt-box">
          <button class="copy-btn" onclick="copySnippet(this)">Copy Prompt</button>
          <pre>Generate a 45-second high-retention video script showing before-and-after workflow with 3-second visual hook.</pre>
        </div>
      </div>
      <div class="card">
        <h3>🧵 Viral Thread Outline</h3>
        <div class="prompt-box">
          <button class="copy-btn" onclick="copySnippet(this)">Copy Prompt</button>
          <pre>Write a 5-tweet build-in-public launch thread detailing problem, AI solution, tech stack, and waitlist CTA.</pre>
        </div>
      </div>
    </div>
    """

    sprint_content = """
    <div class="card">
      <h3>⚡ 48-Hour AI-Native Sprint Checklist</h3>
      <ul class="checklist">
        <li><input type="checkbox"> <span><strong>Hours 0-4:</strong> 1-page functional spec & Stitch/v0 wireframe mockup</span></li>
        <li><input type="checkbox"> <span><strong>Hours 4-24:</strong> Core functional happy-path MVP in Cursor/Claude Code</span></li>
        <li><input type="checkbox"> <span><strong>Hours 24-36:</strong> Landing page copy + Stripe/SePay checkout</span></li>
        <li><input type="checkbox"> <span><strong>Hours 36-48:</strong> Deploy to Vercel/Fly.io & soft launch to 50 beta testers</span></li>
      </ul>
      <div class="prompt-box" style="margin-top: 1.5rem;">
        <button class="copy-btn" onclick="copySnippet(this)">Copy Coding Prompt</button>
        <pre>You are an expert full-stack developer building an ultra-lean MVP in Next.js + Tailwind. Implement only the core happy path for: """ + title + """</pre>
      </div>
    </div>
    """

    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{SUBTITLE}}", subtitle)
    html = html.replace("{{BIZ_CONTENT}}", biz_content)
    html = html.replace("{{MKT_CONTENT}}", mkt_content)
    html = html.replace("{{CONTENT_CONTENT}}", content_content)
    html = html.replace("{{SPRINT_CONTENT}}", sprint_content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ Generated interactive Vibe Board: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate interactive HTML Vibe Board")
    parser.add_argument("--title", default="AI Audio Cleaner for Podcasters", help="Project / Pitch Title")
    parser.add_argument("--subtitle", default="Turn raw recordings into studio-mastered sound in 30 seconds", help="Subtitle / Value Prop")
    parser.add_argument("--output", default="vibe-board.html", help="Output HTML file path")
    args = parser.parse_args()

    generate_html_board(args.title, args.subtitle, args.output)
