---
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
cssclasses:
  - table-max
  - cards
  - cards-cover
  - cards-align-bottom
ObjectType: Creator
Context: 
aliases: 
company: 
tags: 
profession:
---

<%*
let filename = await tp.system.prompt("Who should I add?");
await tp.file.move(`/Humans/Creators/${filename}`);
_%>

## 👤 About 


### 📝 Biography
- **Known For**:
- **Place of Origin**:


### 🎨 Artistic Style 
- **Genres**:
- **Influences**:
- **Notable Works**:
- **Themes**:


## 🤝 How I Discovered <%filename%>


### 📅 First Encounter
- **Date**:
- **Medium** (Book, Album, Exhibition, etc.):


## 💡 Key Insights & Highlights


### ✍️ Quotes
- "Quote 1"
- "Quote 2"


### 🌟 Key Learnings / Thoughts
- Learning/Thought 1
- Learning/Thought 2


## 📚 Body of Work
```dataviewjs
dv.table(
    ['Thumbnail', 'Date', 'Title', 'Category', 'URL'],
    dv.pages("#creation")
	    .where(p => p.file.frontmatter.creator && p.file.frontmatter.creator.includes(`[[${dv.current().file.name}]]`))
        .map(a => [
            `![](${a.thumbnail})`,
            a.date,
            a.file.link,
            a.category,
            `[Link](${a.url})`,
        ])
);
```


