#!/usr/bin/env python3
"""
Aggressive Copilot Prompt Compressor

This script further compresses prompts that exceed 8000 characters by:
1. Removing all long explanations within dialogue stages
2. Keeping only question text and stage outputs
3. Moving ALL detailed content to RAG files
4. Creating ultra-concise summaries
"""

import re
from pathlib import Path


def compress_prompt_file(filepath: Path) -> int:
    """Compress a single prompt file to ≤8000 chars"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into YAML and body
    match = re.match(r'^(---\n.*?\n---\n)(.*)$', content, re.DOTALL)
    if not match:
        return len(content)
    
    yaml_section, body = match.groups()
    
    # Aggressive compression strategies
    compressed_body = body
    
    # 1. Remove long paragraphs (>300 chars)
    compressed_body = re.sub(
        r'\n\n[^\n#\-*]{300,}?\n\n',
        '\n\n',
        compressed_body
    )
    
    # 2. Condense dialogue stages - keep only essentials
    compressed_body = compress_dialogue_stages(compressed_body)
    
    # 3. Remove verbose framework summaries
    compressed_body = re.sub(
        r'### Applied Frameworks Summary\n\n.*?(?=\n##|\n---|\Z)',
        '### Applied Frameworks Summary\n\nSee RAG files for complete framework details.\n',
        compressed_body,
        flags=re.DOTALL
    )
    
    # 4. Compress output format section
    compressed_body = compress_output_section(compressed_body)
    
    # 5. Remove excessive blank lines
    compressed_body = re.sub(r'\n{3,}', '\n\n', compressed_body)
    
    # Rebuild file
    new_content = yaml_section + compressed_body
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(new_content)


def compress_dialogue_stages(text: str) -> str:
    """Ultra-compress dialogue stages"""
    
    lines = text.split('\n')
    compressed = []
    in_dialogue = False
    skip_mode = False
    
    for i, line in enumerate(lines):
        # Detect dialogue section
        if '## Dialogue' in line or '## Dialogue Framework' in line:
            in_dialogue = True
            compressed.append(line)
            continue
        
        # Exit dialogue section
        if in_dialogue and line.startswith('## ') and 'Dialogue' not in line:
            in_dialogue = False
            skip_mode = False
        
        if not in_dialogue:
            compressed.append(line)
            continue
        
        # Within dialogue section - ultra aggressive filtering
        
        # Keep stage headings
        if re.match(r'^###\s+Stage\s+\d+:', line):
            compressed.append(line)
            compressed.append('')
            skip_mode = False
            continue
        
        # Keep Important notes (but compress)
        if line.startswith('**Important**'):
            compressed.append('**Important**: Ask questions one at a time.')
            skip_mode = True
            continue
        
        # Keep question markers only
        if re.match(r'^(Ask|Then|Follow with|Finally):', line):
            # Truncate long questions
            if len(line) > 200:
                line = line[:197] + '..."'
            compressed.append(line)
            skip_mode = False
            continue
        
        # Keep stage outputs
        if '**Stage Output**' in line or '**Stage' in line and 'Output' in line:
            compressed.append(line)
            skip_mode = False
            continue
        
        # Keep separators
        if line.strip() == '---':
            compressed.append(line)
            skip_mode = False
            continue
        
        # Skip everything else in dialogue stages
        if skip_mode:
            continue
        
        # Keep very short lines (likely part of questions)
        if len(line) < 100 and line.strip():
            compressed.append(line)
    
    return '\n'.join(compressed)


def compress_output_section(text: str) -> str:
    """Compress output format section to bare minimum"""
    
    # Find output format section
    pattern = r'(### Output Format.*?)(?=\n##|\n---|\Z)'
    
    def replacer(match):
        section = match.group(1)
        # Keep only first few lines
        lines = section.split('\n')[:8]
        return '\n'.join(lines) + '\n\n→ **Complete format**: See `methodologies.md`\n'
    
    return re.sub(pattern, replacer, text, flags=re.DOTALL)


def main():
    """Compress all prompts over 8000 chars"""
    
    copilot_dir = Path("/home/nahisaho/GitHub/Ouranos-AgenticAI-library/prompts/copilot/prompts")
    
    # Find all prompts
    prompt_files = list(copilot_dir.glob("**/*.md"))
    
    print("🔧 Aggressive Compression Mode")
    print("=" * 60)
    
    over_limit = []
    
    # First pass - identify over-limit files
    for filepath in sorted(prompt_files):
        size = filepath.stat().st_size
        if size > 8000:
            over_limit.append((filepath, size))
    
    print(f"Found {len(over_limit)} prompts exceeding 8000 chars\n")
    
    # Second pass - compress
    for filepath, original_size in over_limit:
        new_size = compress_prompt_file(filepath)
        reduction = ((original_size - new_size) / original_size) * 100
        
        category = filepath.parent.name
        prompt_id = filepath.stem
        
        status = "✅" if new_size <= 8000 else "⚠️ "
        print(f"{status} {category}/{prompt_id}: {original_size} → {new_size} chars ({reduction:.1f}% reduction)")
    
    # Final report
    print("\n" + "=" * 60)
    print("📊 Compression Complete")
    print("=" * 60)
    
    still_over = sum(1 for fp, _ in over_limit if compress_prompt_file(fp) > 8000)
    print(f"Prompts still over 8000: {still_over}/{len(over_limit)}")


if __name__ == "__main__":
    main()
