#!/usr/bin/env python3
"""
Copilot Prompt Converter

This script converts full English prompts (10k-15k chars) to Copilot-optimized versions
(≤8000 chars) by extracting detailed content into RAG files.

Strategy:
- Keep: Dialogue structure, framework names, stage objectives, key questions
- Move to RAG: Framework definitions, detailed examples, step-by-step methodologies

Output:
- prompts/copilot/prompts/{category}/{id}.md (≤8000 chars)
- prompts/copilot/rag/{category}/{id}/frameworks.md (framework details)
- prompts/copilot/rag/{category}/{id}/examples.md (usage examples)
- prompts/copilot/rag/{category}/{id}/methodologies.md (step-by-step procedures)
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Tuple
from datetime import date


class CopilotPromptConverter:
    """Converts EN prompts to Copilot format with RAG support"""
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.stats = {
            'total': 0,
            'converted': 0,
            'failed': 0,
            'skipped': 0
        }
    
    def convert_all_prompts(self):
        """Convert all EN prompts to Copilot format"""
        print("🚀 Starting Copilot Prompt Conversion")
        print(f"Source: {self.source_dir}")
        print(f"Target: {self.target_dir}")
        print("-" * 60)
        
        # Get all prompt files
        prompt_files = list(self.source_dir.glob("**/*.md"))
        prompt_files = [f for f in prompt_files if f.name != "README.md"]
        
        self.stats['total'] = len(prompt_files)
        print(f"Found {len(prompt_files)} prompts to convert\n")
        
        # Convert each prompt
        for prompt_file in sorted(prompt_files):
            category = prompt_file.parent.name
            prompt_id = prompt_file.stem
            
            # Skip if already converted
            target_file = self.target_dir / "prompts" / category / f"{prompt_id}.md"
            if target_file.exists():
                print(f"⏭️  Skipping {category}/{prompt_id} (already exists)")
                self.stats['skipped'] += 1
                continue
            
            try:
                self.convert_prompt(prompt_file, category, prompt_id)
                self.stats['converted'] += 1
                print(f"✅ Converted {category}/{prompt_id}")
            except Exception as e:
                self.stats['failed'] += 1
                print(f"❌ Failed {category}/{prompt_id}: {e}")
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 Conversion Summary")
        print("=" * 60)
        print(f"Total prompts: {self.stats['total']}")
        print(f"✅ Converted: {self.stats['converted']}")
        print(f"⏭️  Skipped: {self.stats['skipped']}")
        print(f"❌ Failed: {self.stats['failed']}")
    
    def convert_prompt(self, source_file: Path, category: str, prompt_id: str):
        """Convert a single prompt to Copilot format"""
        
        # Read source file
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse YAML front matter and content
        yaml_data, body = self.parse_front_matter(content)
        
        # Extract components
        role_section = self.extract_section(body, "## Role")
        dialogue_section = self.extract_section(body, "## Dialogue Flow")
        frameworks_section = self.extract_section(body, "## Applied Expertise and Frameworks")
        output_section = self.extract_section(body, "## Output Format")
        examples_section = self.extract_section(body, "## Usage Example")
        notes_section = self.extract_section(body, "## Important Notes")
        
        # Build Copilot prompt (compressed)
        copilot_prompt = self.build_copilot_prompt(
            yaml_data, role_section, dialogue_section, 
            output_section, category, prompt_id
        )
        
        # Build RAG files
        frameworks_rag = self.build_frameworks_rag(frameworks_section, yaml_data)
        examples_rag = self.build_examples_rag(examples_section, dialogue_section, yaml_data)
        methodologies_rag = self.build_methodologies_rag(
            frameworks_section, output_section, notes_section, yaml_data
        )
        
        # Create directories
        prompt_dir = self.target_dir / "prompts" / category
        rag_dir = self.target_dir / "rag" / category / prompt_id
        prompt_dir.mkdir(parents=True, exist_ok=True)
        rag_dir.mkdir(parents=True, exist_ok=True)
        
        # Write files
        self.write_file(prompt_dir / f"{prompt_id}.md", copilot_prompt)
        self.write_file(rag_dir / "frameworks.md", frameworks_rag)
        self.write_file(rag_dir / "examples.md", examples_rag)
        self.write_file(rag_dir / "methodologies.md", methodologies_rag)
    
    def parse_front_matter(self, content: str) -> Tuple[Dict, str]:
        """Parse YAML front matter and body"""
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if match:
            yaml_str, body = match.groups()
            yaml_data = yaml.safe_load(yaml_str)
            return yaml_data, body
        return {}, content
    
    def extract_section(self, content: str, heading: str) -> str:
        """Extract content between heading and next same-level heading"""
        pattern = rf'{re.escape(heading)}(.*?)(?=\n## |\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ""
    
    def build_copilot_prompt(self, yaml_data: Dict, role: str, dialogue: str, 
                            output: str, category: str, prompt_id: str) -> str:
        """Build compressed Copilot prompt (≤8000 chars)"""
        
        # Update YAML metadata
        yaml_data['updated'] = str(date.today())
        yaml_data['optimized_for'] = 'copilot'
        yaml_data['rag_files'] = ['frameworks.md', 'examples.md', 'methodologies.md']
        yaml_data.pop('character_count', None)
        
        # Compress role section
        role_compressed = self.compress_role(role)
        
        # Compress dialogue section
        dialogue_compressed = self.compress_dialogue(dialogue)
        
        # Add RAG references
        rag_reference = f"\n**RAG Support**: This prompt uses RAG files for detailed frameworks, methodologies, and examples. Reference `rag/{category}/{prompt_id}/frameworks.md` for framework definitions, `examples.md` for usage scenarios, and `methodologies.md` for step-by-step procedures.\n"
        
        # Build final prompt
        yaml_str = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        prompt = f"""---
{yaml_str.strip()}
---

{role_compressed}

{rag_reference}
---

{dialogue_compressed}

---

## Quick Reference

### Applied Frameworks Summary

{self.extract_framework_summary(yaml_data)}

→ **Full framework details**: See `rag/{category}/{prompt_id}/frameworks.md`

### Output Format

{self.compress_output_format(output)}

→ **Complete templates and examples**: See `rag/{category}/{prompt_id}/methodologies.md`

---

## Version Information

- **Version**: {yaml_data.get('version', '1.0.0')}
- **Created**: {yaml_data.get('created', str(date.today()))}
- **Updated**: {yaml_data.get('updated', str(date.today()))}
- **Status**: Active
- **Optimized for**: Microsoft Copilot Agent Builder
"""
        
        # Validate character count
        char_count = len(prompt)
        if char_count > 8000:
            print(f"  ⚠️  Warning: {prompt_id} is {char_count} chars (>{8000})")
        
        return prompt
    
    def compress_role(self, role: str) -> str:
        """Compress role section by removing verbose descriptions"""
        # Keep first paragraph and expertise list
        lines = role.split('\n')
        compressed = []
        in_expertise = False
        
        for line in lines:
            # Keep heading
            if line.startswith('## Role'):
                compressed.append(line)
            # Keep first paragraph (mission statement)
            elif line.strip() and not line.startswith('-') and not in_expertise:
                compressed.append(line)
            # Start expertise list
            elif line.strip().startswith('Your expertise'):
                compressed.append(line)
                in_expertise = True
            # Keep expertise items
            elif in_expertise and line.strip().startswith('-'):
                compressed.append(line)
            # End expertise list
            elif in_expertise and not line.strip().startswith('-'):
                break
        
        return '\n'.join(compressed[:10])  # Limit to 10 lines
    
    def compress_dialogue(self, dialogue: str) -> str:
        """Compress dialogue section by keeping structure, removing verbosity"""
        # Ultra-aggressive: Keep ONLY stage headings, questions, outputs
        
        lines = dialogue.split('\n')
        compressed = []
        
        for line in lines:
            # Stage headings
            if re.match(r'^###\s+Stage\s+\d+:', line):
                compressed.append(line)
                compressed.append('')
            # Important notes - ultra compress
            elif line.startswith('**Important**'):
                compressed.append('**Important**: Ask one question at a time.')
                compressed.append('')
            # Questions - truncate if too long
            elif re.match(r'^(Ask|Then|Follow with|Finally):', line):
                if len(line) > 150:
                    line = line[:147] + '..."'
                compressed.append(line)
            # Stage outputs - keep brief
            elif '**Stage Output**' in line:
                compressed.append(line)
                compressed.append('')
            # Separators
            elif line.strip() == '---':
                compressed.append(line)
        
        return '\n'.join(compressed)
    
    def compress_output_format(self, output: str) -> str:
        """Compress output format to key points only"""
        # Keep headings and brief descriptions, remove examples
        lines = output.split('\n')
        compressed = []
        
        for i, line in enumerate(lines):
            # Keep section headings
            if line.startswith('#'):
                compressed.append(line)
            # Keep brief bullets
            elif line.strip().startswith('-') and len(line) < 150:
                compressed.append(line)
            # Keep numbered lists (brief)
            elif re.match(r'^\d+\.', line.strip()) and len(line) < 150:
                compressed.append(line)
            # Add separators
            elif line.strip() == '' and compressed and compressed[-1].strip() != '':
                compressed.append('')
            
            # Limit total lines
            if len(compressed) > 30:
                compressed.append("\n→ **Complete format details**: See RAG files")
                break
        
        return '\n'.join(compressed[:35])
    
    def extract_framework_summary(self, yaml_data: Dict) -> str:
        """Extract brief framework summary from YAML"""
        frameworks = yaml_data.get('frameworks', [])
        if not frameworks:
            return "No frameworks specified"
        
        return ', '.join(f"**{fw}**" for fw in frameworks[:5])
    
    def build_frameworks_rag(self, frameworks_section: str, yaml_data: Dict) -> str:
        """Build frameworks.md RAG file with full framework details"""
        
        frameworks = yaml_data.get('frameworks', [])
        prompt_id = yaml_data.get('id', 'unknown')
        category = yaml_data.get('category', 'general')
        
        rag = f"""# Frameworks for {yaml_data.get('id', 'Prompt').replace('-', ' ').title()}

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

{frameworks_section if frameworks_section else "Framework details will be populated here."}

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other logically.

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives.

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches.

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it

---

## Version Information

- **Version**: {yaml_data.get('version', '1.0.0')}
- **Last Updated**: {date.today()}
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/{category}/{prompt_id}.md`
  - Examples: `rag/{category}/{prompt_id}/examples.md`
  - Methodologies: `rag/{category}/{prompt_id}/methodologies.md`
"""
        
        return rag
    
    def build_examples_rag(self, examples_section: str, dialogue_section: str, 
                          yaml_data: Dict) -> str:
        """Build examples.md RAG file with usage examples"""
        
        prompt_id = yaml_data.get('id', 'unknown')
        category = yaml_data.get('category', 'general')
        
        rag = f"""# Examples for {yaml_data.get('id', 'Prompt').replace('-', ' ').title()}

This file provides concrete usage examples and scenarios demonstrating this prompt in action.

---

{examples_section if examples_section else "Usage examples will be populated here."}

---

## Dialogue Quality Tips

### Creating Natural Flow

Build on user responses naturally, showing domain expertise and genuine engagement.

### Demonstrating Expertise

Use domain-specific knowledge to provide valuable insights and guidance.

### Adaptive Responses

Adjust depth and complexity based on user's expertise level and responses.

---

## Version Information

- **Version**: {yaml_data.get('version', '1.0.0')}
- **Last Updated**: {date.today()}
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/{category}/{prompt_id}.md`
  - Frameworks: `rag/{category}/{prompt_id}/frameworks.md`
  - Methodologies: `rag/{category}/{prompt_id}/methodologies.md`
"""
        
        return rag
    
    def build_methodologies_rag(self, frameworks_section: str, output_section: str,
                               notes_section: str, yaml_data: Dict) -> str:
        """Build methodologies.md RAG file with step-by-step procedures"""
        
        prompt_id = yaml_data.get('id', 'unknown')
        category = yaml_data.get('category', 'general')
        
        rag = f"""# Methodologies for {yaml_data.get('id', 'Prompt').replace('-', ' ').title()}

This file provides step-by-step procedures, validation checklists, and best practices.

---

## Process Overview

This section provides detailed step-by-step guidance for executing this prompt effectively.

---

## Output Format Details

{output_section if output_section else "Output format details will be populated here."}

---

## Important Notes and Best Practices

{notes_section if notes_section else "Best practices will be populated here."}

---

## Quality Checkpoints

Before finalizing outputs, verify:

- [ ] All objectives clearly addressed
- [ ] Frameworks properly applied
- [ ] Output format matches specifications
- [ ] Quality standards met
- [ ] User requirements fulfilled

---

## Common Issues and Solutions

This section addresses frequently encountered challenges and their solutions.

---

## Version Information

- **Version**: {yaml_data.get('version', '1.0.0')}
- **Last Updated**: {date.today()}
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/{category}/{prompt_id}.md`
  - Frameworks: `rag/{category}/{prompt_id}/frameworks.md`
  - Examples: `rag/{category}/{prompt_id}/examples.md`
"""
        
        return rag
    
    def write_file(self, filepath: Path, content: str):
        """Write content to file"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    """Main execution"""
    # Define paths
    source_dir = "/home/nahisaho/GitHub/Ouranos-AgenticAI-library/prompts/en/prompts"
    target_dir = "/home/nahisaho/GitHub/Ouranos-AgenticAI-library/prompts/copilot"
    
    # Create converter and run
    converter = CopilotPromptConverter(source_dir, target_dir)
    converter.convert_all_prompts()


if __name__ == "__main__":
    main()
