---
ObjectType: Recipe
cuisine: null
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
source: null
summary: null
tags: []
---

<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Recipes/${filename}`);
_%>

<% tp.file.cursor() %>



