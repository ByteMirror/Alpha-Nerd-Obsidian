#Tutorial/Obsidian 

---


Use callouts

As of v0.14.0, Obsidian supports callout blocks, sometimes called "admonitions". Callout blocks are written as a blockquote, inspired by the "alert" syntax from Microsoft Docs.

Callouts are also supported natively on [Obsidian Publish](https://help.obsidian.md/Obsidian+Publish/Introduction+to+Obsidian+Publish).

Note

For compatibility reasons, if you're also using the Admonitions plugin, you should update it to at least v8.0.0 to avoid problems with the new callout system.

Use the following syntax to denote a callout block: `> [!INFO]`.

```markdown
> [!INFO]
> Here's a callout block.
> It supports **markdown**, [[Internal link|wikilinks]], and [[Embed files|embeds]]!
> ![[og-image.png]]
```

It will show up like this:

Info

Here's a callout block.  
It supports **markdown**, [wikilinks](https://help.obsidian.md/How+to/Internal+link) and [embeds](https://help.obsidian.md/How+to/Embed+files)!  
![og-image.png](https://publish-01.obsidian.md/access/f786db9fac45774fa4f0d8112e232d67/og-image.png)

### Types

By default, Obsidian supports several callout types and aliases. Each type comes with a different background color and icon.

To use these default styles, replace `INFO` in the examples with any of these types. Any unrecognized type will default to the "note" type, unless they are [customized](https://help.obsidian.md/How+to/Use+callouts#Customizations). The type identifier is case insensitive.

Note

```md
> [!note]
> Lorem ipsum dolor sit amet
```

---

Abstract

```md
> [!abstract]
> Lorem ipsum dolor sit amet
```

Aliases: `summary`, `tldr`

---

Info

```md
> [!info]
> Lorem ipsum dolor sit amet
```

---

Todo

```md
> [!todo]
> Lorem ipsum dolor sit amet
```

---

Tip

```md
> [!tip]
> Lorem ipsum dolor sit amet
```

Aliases: `hint`, `important`

---

Success

Aliases: `check`, `done`

---

Question

Aliases: `help`, `faq`

---

Warning

Aliases: `caution`, `attention`

---

Failure

Aliases: `fail`, `missing`

---

Danger

Alias: `error`

---

Bug

```md
> [!bug]
> Lorem ipsum dolor sit amet
```

---

Example

```md
> [!example]
> Lorem ipsum dolor sit amet
```

---

Quote

```md
> [!quote]
> Lorem ipsum dolor sit amet
```

Alias: `cite`

### Title and body

You can define the title of the callout block, and you can also have a callout without body content.

```markdown
> [!TIP] Callouts can have custom titles, which also supports ==markdown==!
```

Callouts can have custom titles, which also supports markdown!

### Folding

Additionally, you can create a folding callout by adding `+` (default expanded) or `-` (default collapsed) after the block.

```markdown
> [!FAQ]- Are callouts foldable?
> Yes! In a foldable callout, the contents are hidden until it is expanded.
```

Will show up as:

Are callouts foldable?

Yes! In a foldable callout, the contents are hidden until it is expanded.

### Nesting

You can also nest callouts multiple layers deep.

```markdown
> [!question] Can callouts be nested?
> > [!todo] Yes!, they can.
> > > [!example]  You can even use multiple layers of nesting.
```

Will result in:

Can callouts be nested?

Yes!, they can.

You can even use multiple layers of nesting.

### Customizations

Snippets and plugins can define custom callouts, too, or overwrite the default options. Callout types and icons are defined in CSS, where the color is an `r, g, b` tuple and the icon is the icon ID from any internally supported icon (like `lucide-info`). Alternatively, you can specify an SVG icon as a string.

```css
.callout[data-callout="my-callout-type"] {
    --callout-color: 0, 0, 0;
    --callout-icon: icon-id;
    --callout-icon: '<svg>...custom svg...</svg>';
}
```

### Developer Notes

We choose the syntax because:

-   it falls back to blockquotes in unsupported markdown renderers
-   it parses all Markdown, including links, embeds, etc.
-   it recognizes [Internal link's](https://help.obsidian.md/How+to/Internal+link) and will show up in [Backlinks](https://help.obsidian.md/Plugins/Backlinks), [Outgoing links](https://help.obsidian.md/Plugins/Outgoing+links), and [Graph view](https://help.obsidian.md/Plugins/Graph+view)
-   the spellchecker can spellcheck it.

