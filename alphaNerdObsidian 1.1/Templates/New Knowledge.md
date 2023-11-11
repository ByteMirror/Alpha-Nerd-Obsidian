---
ObjectType: Knowledge
Context: 
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
value: 
aliases: 
tags: 
people: 
summary: 
keywords:
---
<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Knowledge/${filename}`);
%>
## 🌟 Why is this useful?
<% tp.file.cursor() %>

## 🗒️ Notes


## 🌐 Resources







