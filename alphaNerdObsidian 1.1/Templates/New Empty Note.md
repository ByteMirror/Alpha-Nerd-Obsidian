---
ObjectType: EmptyNote
Context: 
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags: 
summary:
---
<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/TheGarden/${filename}`);
_%>

<% tp.file.cursor() %>



