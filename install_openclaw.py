#!/usr/bin/env python3
"""
OpenClaw Production Installer
Installs everything necessary for OpenClaw + enhanced context files
"""

import subprocess
import sys
import os

def run(cmd):
    print(f"→ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

print("=== OpenClaw Production Installer ===\n")

print("[1/5] Creating OpenClaw directory structure...")
os.makedirs("openclaw/context", exist_ok=True)
os.makedirs("openclaw/agents", exist_ok=True)
os.makedirs("openclaw/logs", exist_ok=True)

print("[2/5] Installing core dependencies...")
run("pip install crewai crewai-tools python-dotenv requests pyyaml")

print("[3/5] Checking for Ollama...")
try:
    subprocess.run(["ollama", "--version"], check=True, capture_output=True)
except:
    print("Installing Ollama...")
    if sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
        run("curl -fsSL https://ollama.com/install.sh | sh")

print("[4/5] Pulling recommended models...")
for model in ["llama3.1:8b", "phi3.5:3.8b", "qwen2.5:7b"]:
    run(f"ollama pull {model}")

print("[5/5] Creating enhanced context files...")
with open("openclaw/context/SECURITY_GUARDRAILS.md", "w") as f:
    f.write("# OpenClaw Security Guardrails\n\n## Core Protection Rules\n1. Never harm the user's system without confirmation.\n2. Never expose sensitive data.\n3. Always validate inputs and outputs.\n4. Ask for confirmation on high-risk actions.\n5. Prioritize user privacy and safety above all.\n")

with open("openclaw/context/BRANDING_CONTEXT.md", "w") as f:
    f.write("# OpenClaw Brand Voice\n\nTone: Dark cinematic, confident, precise.\nVisual Language: Neon cyan/magenta, glassmorphism, anti-gravity, cyber-HUD.\nCommunication: Direct, elegant, protective of user goals.\n")

print("\n\u2705 OpenClaw installation complete!")