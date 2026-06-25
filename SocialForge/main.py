#!/usr/bin/env python3
"""
SocialForge Phase 1 - Main Interface
Simple CLI to use Content Generator and Post Improver
"""

from phase1_content_generator import generate_platform_content, improve_post

def main():
    print("=== SocialForge Phase 1 ===")
    print("1. Generate content from topic")
    print("2. Improve existing post")
    choice = input("\nChoose option (1 or 2): ").strip()

    if choice == "1":
        topic = input("Enter your topic/idea: ")
        platforms_input = input("Platforms (comma separated, e.g. tiktok,instagram,x): ")
        platforms = [p.strip() for p in platforms_input.split(",")]

        print("\nGenerating content...\n")
        results = generate_platform_content(topic, platforms)

        for platform, content in results.items():
            print(f"\n=== {platform.upper()} ===")
            print(content)
            print("-" * 60)

    elif choice == "2":
        print("\nPaste your original post (press Enter twice when done):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        original_post = "\n".join(lines)

        platform = input("Platform (tiktok/instagram/x/facebook/youtube): ").strip().lower() or "general"
        tone = input("Desired tone (e.g. professional, casual, motivational): ").strip() or "professional"

        print("\nImproving post...\n")
        improved = improve_post(original_post, platform, tone)

        print("=== IMPROVED VERSION ===")
        print(improved)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()