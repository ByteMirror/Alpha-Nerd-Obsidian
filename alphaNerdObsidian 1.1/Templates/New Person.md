---
Alignment: null
Context: null
MTGColor: null
ObjectType: Person
aliases: null
birthday: null
company: null
cssclasses:
- table-max
- cards
- cards-cover
- cards-align-bottom
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
dateLastSpoken: null
email: null
followUp: false
languages: null
location: null
tags: []
title: null
---

<%*
let filename = await tp.system.prompt("Who should I add?");
await tp.file.move(`/Humans/${filename}`);
_%>

## 👤 About
<% tp.file.cursor() %>

## 🤝 How We Met


## 📜 History


## 👨‍👩‍👧‍👦 Family


## 🌈 Personality


### [[OGAS Framework]]
-  **Goal** 🎯 :
-  **Attitude** 🧠 :
-  **Stake** 🎲 :

### 🌟 Ideals, Bonds & Flaws
-  **Ideals** 💡 :
-  **Bonds** 💞 :
-  **Flaws** 🚫 :


## 🔪 Knives
(**Things that get them fired up**)
-  


## 📚 Log
-  



## 🔔 Mentions & Relations 

> [!FAQ]-  Related Files
> ```dataview
TABLE
date as "Date",
summary as "Summary" 
where contains(people, this.file.link) and ObjectType != "" and ObjectType != "Image"
sort date desc 


## 🖼️ Pictures with <%filename%>

> [!Done]- Gallery
> ```dataviewjs
> dv.table(
>     ['Preview', 'Title', 'Rating', 'People', 'Date'],
>     dv.pages()
>         .where(p => p.file.folder != "Templates")
>         .where(p => p.file.frontmatter.ObjectType === "Image")
>         .where(p => p.file.frontmatter.people && p.file.frontmatter.people.includes(`[[${dv.current().file.name}]]`))
>         .map(p => [`![[${p.file.path}]]`, p.file.link, p.rating, p.people, p.date])
> );
> ```
