#!/usr/bin/env python3
import os
import sys
import argparse
import html

def generate_html_board(title, subtitle, output_file="vibe-board.html"):
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(repo_dir, "templates", "vibe-board-template.html")
    
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)

    biz_content = f"""
    <div class="grid">
      <div class="card">
        <h3>🎯 The Commercial Pitch</h3>
        <p><strong>{safe_title}</strong></p>
        <p style="color: var(--text-muted);">{safe_subtitle}</p>
      </div>
      <div class="card">
        <h3>💎 Grand Slam Offer</h3>
        <p><strong>Transformation:</strong> High perceived value with guaranteed risk-reversal.</p>
        <span class="badge">Pricing: $49 - $499/mo</span>
      </div>
      <div class="card">
        <h3>🧪 Day-1 Cashflow Test</h3>
        <p>Send 20 personalized 60-second video breakdowns to niche prospects. Goal: 2 paid pre-orders in 24 hours.</p>
      </div>
    </div>
    """

    mkt_content = """
    <div class="grid">
      <div class="card">
        <h3>🪝 Hook-Offer-Angle</h3>
        <p><strong>Pain Angle:</strong> "How much revenue did you leave on the table last month?"</p>
        <p><strong>Dream Angle:</strong> "Automate client acquisition and save 15 hours a week."</p>
      </div>
      <div class="card">
        <h3>📍 Target Watering Holes</h3>
        <ul style="color: var(--text-muted); padding-left: 1.2rem;">
          <li>Niche industry subreddits & Facebook operator groups</li>
          <li>Targeted LinkedIn founders & decision-makers</li>
          <li>Active Slack/Discord professional communities</li>
        </ul>
      </div>
    </div>
    """

    content_content = """
    <div class="grid">
      <div class="card">
        <h3>🎬 Short-Form Video Script (TikTok/Reels)</h3>
        <p><strong>3-Second Hook:</strong> "If you're still doing this manual task in 2026, you're burning cash."</p>
        <div class="prompt-box">
          <button class="copy-btn" onclick="copySnippet(this)">Copy Script Prompt</button>
          <pre>Generate a 45-second high-retention video script showing before-and-after client results with direct CTA to comment for the link.</pre>
        </div>
      </div>
      <div class="card">
        <h3>🧵 Long-form Authority Post</h3>
        <div class="prompt-box">
          <button class="copy-btn" onclick="copySnippet(this)">Copy Post Prompt</button>
          <pre>Write a high-converting LinkedIn/Facebook post exposing the hidden costs of the old way and introducing the new framework.</pre>
        </div>
      </div>
    </div>
    """

    sprint_content = f"""
    <div class="card">
      <h3>🚀 48-Hour Go-To-Market (GTM) Checklist</h3>
      <ul class="checklist">
        <li><input type="checkbox"> <span><strong>Hours 0-12:</strong> Finalize Grand Slam Offer & publish 1-page sales page (Framer/Carrd/Gumroad)</span></li>
        <li><input type="checkbox"> <span><strong>Hours 12-24:</strong> Package core deliverable / automated workflow / asset</span></li>
        <li><input type="checkbox"> <span><strong>Hours 24-36:</strong> Connect payment gateway (Stripe/VietQR/SePay) & onboarding automation</span></li>
        <li><input type="checkbox"> <span><strong>Hours 36-48:</strong> Soft launch outreach to 50 warm prospects & secure first paying customer</span></li>
      </ul>
      <div class="prompt-box" style="margin-top: 1.5rem;">
        <button class="copy-btn" onclick="copySnippet(this)">Copy Sales Copy Prompt</button>
        <pre>You are an expert copywriter. Write high-converting sales page copy and cold outreach DMs for: {safe_title}</pre>
      </div>
    </div>
    """

    output_html = template.replace("{{TITLE}}", safe_title)
    output_html = output_html.replace("{{SUBTITLE}}", safe_subtitle)
    output_html = output_html.replace("{{BIZ_CONTENT}}", biz_content)
    output_html = output_html.replace("{{MKT_CONTENT}}", mkt_content)
    output_html = output_html.replace("{{CONTENT_CONTENT}}", content_content)
    output_html = output_html.replace("{{SPRINT_CONTENT}}", sprint_content)

    out_dir = os.path.dirname(output_file)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_html)

    print(f"✓ Generated interactive Vibe Board: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate interactive HTML Vibe Board")
    parser.add_argument("--title", default="Productized AI Ops Agency", help="Project / Pitch Title")
    parser.add_argument("--subtitle", default="Turn manual workflows into automated client acquisition systems", help="Subtitle / Value Prop")
    parser.add_argument("--output", default="vibe-board.html", help="Output HTML file path")
    args = parser.parse_args()

    generate_html_board(args.title, args.subtitle, args.output)
