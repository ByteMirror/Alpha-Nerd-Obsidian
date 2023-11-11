Markdown is a lightweight markup language used to display content on the web in a simple way. It's the most popular markup language because it's the easiest to get started with.

Markdown has different "flavours" or implementations that are slightly different in syntax. Obsidian notes are based on Markdown and are saved as `.md` files.

## Headings

```markdown
# This is heading 1
## This is heading 2
### This is heading 3
```

Looks like this:

# This is heading 1
## This is heading 2
### This is heading 3

## Link to Obsidian note

```markdown
[[Readme]]
```

Looks like this:

[[Readme]]

## Link to note but with link text

```markdown
[[Readme|This is the readme.]]
```

Looks like this:

[[Readme|This is the readme.]]

## Link to a public website

```markdown
[Nicole](https://nicolevanderhoeven.com)
```

Looks like this:

[Nicole](https://nicolevanderhoeven.com)

## Link to a section of a note

```markdown
[[Readme#What's in this vault?]]
```

Looks like this:

[[Readme#What's in this vault?]]

## Link to paragraph in note:

```markdown
[[Readme#^05990f]]
```

Looks like this:
[[Readme#^05990f]]

## Embed note or part of notes

Same as the previous five, but add a `!` at the start like:

```markdown
![[Readme#^05990f]]
```

Looks like this:

![[Readme#^05990f]]

## Bold text

```markdown
**super** important
```

Looks like this:

**super** important

## Italicize text

```markdown
*a little* important
```

Looks like this:

*a little* important

## Strikethrough text

```markdown
~~not important~~
```

Looks like this:

~~not important~~

## Highlight text

```markdown
==Remember this==
```

Looks like this:

==Remember this==

## Add block quote

```markdown
> Live long and prosper.
```

Looks like this:

> Live long and prosper.

## Embed image in vault

```markdown
![[notebook.png]]
```

Looks like this:

![[notebook.png]]

## Add horizontal rule

```markdown
---
```

Looks like this:

---

## List items (bulleted)

```markdown
- Item 1
- Item 2
```

Looks like this:

- Item 1
- Item 2

## List items (numbered)

```markdown
1. Item 1
2. Item 2
```

Looks like this:

1. Item 1
2. Item 2

## Add a checklist

```markdown
- [ ] Process notes
- [X] Finish [[book]] 
```

Looks like this:

- [ ] Process notes
- [X] Finish book

## Add in-line code

```markdown
Command: `git push`
```

Looks like this:

Command: `git push`

## Add callout

```markdown
> [!NOTE] Note
> This is a note.
```

Looks like this:

> [!NOTE] Note
> This is a note.

## Add code block

> ```python
> print('Hello world')
> ```

Looks like this:

```python
print('Hello world')
```

## Add a footnote

```markdown
... as Ahrens says. [^ahrens]
[^ahrens]: Ahrens, S.(2022).
```

Looks like this:

... as Ahrens says. [^ahrens]

[^ahrens]: Ahrens, S.(2022).

