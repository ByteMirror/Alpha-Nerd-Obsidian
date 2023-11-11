---
Alignment: null
MTGColor: null
ObjectType: Pet
aliases: null
birthday: null
cssclasses:
- table-max
- cards
- cards-cover
- cards-align-bottom
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags: []
---

<%*
let filename = await tp.system.prompt("Who should I add?");
await tp.file.move(`/Pets/${filename}`);
_%>

## 👤 About
<% tp.file.cursor() %>


## 🌻 Medical Information
- Create note for doctors visits
- Create note for medical documents
## 🤝 How We Met


## 📚 Log
-  



## 🔔 Mentions

> [!FAQ] Mentions
> ```dataview
> TABLE
> date as "Date",
> summary as "Summary" 
> where contains(people, this.file.link)
> sort date desc 
> ```



