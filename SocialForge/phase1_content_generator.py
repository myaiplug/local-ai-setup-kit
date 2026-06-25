#!/usr/bin/env python3
"""
SocialForge Phase 1 - Content Generator + Post Improver
Production Quality | No Corner Cutting

This module generates high-quality, platform-optimized social media content
and improves existing posts to Awwwards-level quality.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

llm = LLM(
    model=os.getenv("LLM_MODEL", "gpt-4o"),
    temperature=0.7
)

print("🚀 SocialForge Phase 1 - Content Generator Initialized\n")

# AGENTS

content_strategist = Agent(
    role="Content Strategist",
    goal="Create high-performing, platform-specific social media content that matches each platform's algorithm and audience",
    backstory="You are a world-class social media strategist who understands how algorithms work on TikTok, Instagram, X, Facebook, and YouTube in 2026. You know exactly what type of content performs best on each platform and how to write for maximum engagement.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

post_improver = Agent(
    role="Post Improver & Quality Controller",
    goal="Transform average social media posts into industry-leading, high-engagement content",
    backstory="You are an elite content editor with an eye for what makes posts go viral. You take weak or average posts and rewrite them with stronger hooks, better structure, emotional depth, and platform optimization while maintaining the original voice.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# CONTENT GENERATOR
def generate_platform_content(topic: str, platforms: list = None):
    if platforms is None:
        platforms = ["tiktok", "instagram", "x", "facebook", "youtube"]

    results = {}

    for platform in platforms:
        task = Task(
            description=f"Create a high-quality {platform} post about: {topic}\n\nRequirements:\n- Match the platform's current algorithm preferences (2026)\n- Use the correct character length and tone for {platform}\n- Include a strong hook in the first 1-3 seconds/lines\n- Optimize for engagement and conversation\n- Write in a natural, premium quality style (Awwwards level)\n- Include relevant emojis and formatting where appropriate",
            expected_output=f"A ready-to-post {platform} caption/post optimized for maximum reach and engagement.",
            agent=content_strategist
        )

        crew = Crew(agents=[content_strategist], tasks=[task], verbose=True)
        result = crew.kickoff()
        results[platform] = result

    return results

# POST IMPROVER
def improve_post(original_post: str, platform: str = "general", target_tone: str = "professional"):
    task = Task(
        description=f"Improve and upscale this {platform} post to Awwwards-winning quality:\n\nOriginal Post:\n{original_post}\n\nRequirements:\n- Strengthen the hook significantly\n- Improve structure, flow, and emotional impact\n- Optimize for {platform}'s algorithm\n- Adjust tone to: {target_tone}\n- Make it more engaging and likely to generate comments/shares\n- Keep the core message but elevate the execution\n- Make it feel premium and professionally written",
        expected_output="An improved, high-quality version of the post ready for publishing.",
        agent=post_improver
    )

    crew = Crew(agents=[post_improver], tasks=[task], verbose=True)
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print("=== SocialForge Phase 1 - Testing ===\n")

    print(">>> Generating content for topic: 'How AI is changing music production in 2026'\n")
    content = generate_platform_content(
        topic="How AI is changing music production in 2026",
        platforms=["tiktok", "instagram", "x"]
    )

    for platform, post in content.items():
        print(f"\n--- {platform.upper()} ---")
        print(post)
        print("-" * 50)

    print("\n\n>>> Improving a sample post...\n")
    weak_post = "AI is changing how we make beats. It's pretty cool."

    improved = improve_post(
        original_post=weak_post,
        platform="instagram",
        target_tone="inspirational but grounded"
    )

    print("Improved Version:")
    print(improved)