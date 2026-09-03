#!/usr/bin/env python3
import os
import sys

def validate_skill(skill_path):
    skill_name = os.path.basename(skill_path)
    skill_md = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md):
        print(f"❌ SKILL.md not found in {skill_path}")
        return False

    with open(skill_md, "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    if line_count > 300:
        print(f"❌ [{skill_name}] SKILL.md exceeds 300 lines ({line_count} lines)")
        return False
    print(f"✓ [{skill_name}] SKILL.md line count: {line_count} (< 300)")

    content = "".join(lines)
    if not content.startswith("---"):
        print(f"❌ [{skill_name}] Missing opening YAML frontmatter '---'")
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"❌ [{skill_name}] Invalid YAML frontmatter delimiter")
        return False

    frontmatter = parts[1]
    required_keys = ["name:", "description:", "user-invocable:", "when_to_use:"]
    for key in required_keys:
        if key not in frontmatter:
            print(f"❌ [{skill_name}] Missing required frontmatter key: {key}")
            return False

    # Check description length
    desc_line = [l for l in frontmatter.splitlines() if l.strip().startswith("description:")]
    if desc_line:
        desc_text = desc_line[0].split("description:", 1)[1].strip().strip('"')
        if len(desc_text) > 1024:
            print(f"❌ [{skill_name}] Description exceeds 1024 chars ({len(desc_text)} chars)")
            return False
        print(f"✓ [{skill_name}] Description length: {len(desc_text)} chars (<= 1024)")

    # Check references line counts
    refs_dir = os.path.join(skill_path, "references")
    if os.path.exists(refs_dir):
        for ref_file in os.listdir(refs_dir):
            if ref_file.endswith(".md"):
                ref_path = os.path.join(refs_dir, ref_file)
                with open(ref_path, "r", encoding="utf-8") as rf:
                    ref_lines = len(rf.readlines())
                if ref_lines > 300:
                    print(f"❌ [{skill_name}] Reference {ref_file} exceeds 300 lines ({ref_lines} lines)")
                    return False
                print(f"✓ [{skill_name}] Reference {ref_file}: {ref_lines} lines (< 300)")

    return True

def validate_all():
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(repo_dir, "skills")
    
    all_passed = True
    for item in sorted(os.listdir(skills_dir)):
        item_path = os.path.join(skills_dir, item)
        if os.path.isdir(item_path):
            print(f"\nValidating skill: {item}...")
            if not validate_skill(item_path):
                all_passed = False

    if all_passed:
        print("\n🎉 ALL 5 SKILLS VALIDATED SUCCESSFULLY!")
        return 0
    else:
        print("\n❌ SOME SKILLS FAILED VALIDATION!")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        success = validate_skill(sys.argv[1])
        sys.exit(0 if success else 1)
    else:
        sys.exit(validate_all())
