import os
import re
import yaml
from pathlib import Path

# Function to parse the frontmatter from a Markdown file
def parse_frontmatter(file_content):
    pattern = re.compile(r'^---\s+(.*?)\s+---', re.DOTALL)
    match = pattern.search(file_content)
    if match:
        frontmatter_str = match.group(1)
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML frontmatter: {e}")
            return None, 0
        return frontmatter, match.end()
    return {}, 0

# Function to update the frontmatter
def update_frontmatter(frontmatter):
    updated = False
    new_tags = []
    if 'tags' in frontmatter and isinstance(frontmatter['tags'], list):
        for tag in frontmatter['tags']:
            parts = tag.split('/')
            if len(parts) > 1:
                if parts[0] == 'ObjectType' and len(parts) > 2:
                    frontmatter['ObjectType'] = parts[1]
                    new_tags.extend(parts[2:])
                    updated = True
                elif parts[0] == 'ObjectType':
                    frontmatter['ObjectType'] = parts[1]
                    updated = True
                elif parts[0] == 'Context' and len(parts) > 2:
                    frontmatter['Context'] = parts[1]
                    new_tags.extend(parts[2:])
                    updated = True
                elif parts[0] == 'Context':
                    frontmatter['Context'] = parts[1]
                    updated = True
            else:
                new_tags.append(tag)
        frontmatter['tags'] = new_tags
    return frontmatter, updated

# Ask for the file path
user_path = input("Enter the path to your markdown files: ")
path_to_process = Path(user_path)

# Check if the provided path is valid
if not path_to_process.exists():
    print(f"The path {user_path} does not exist.")
else:
    # Counter for the number of files processed
    file_count = 0

    # Iterate over Markdown files in the directory and subdirectories
    for md_file in path_to_process.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        frontmatter, content_start = parse_frontmatter(content)
        if frontmatter is not None:
            updated_frontmatter, updated = update_frontmatter(frontmatter)
            if updated:
                new_content = '---\n' + yaml.dump(updated_frontmatter) + '---\n' + content[content_start:]
                
                with open(md_file, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated frontmatter for: {md_file}")
            else:
                print(f"No ObjectType or Context tag found in: {md_file}")
        else:
            print(f"Skipping due to YAML error: {md_file}")
        
        file_count += 1

    print(f"Frontmatter update complete. Total files processed: {file_count}")
