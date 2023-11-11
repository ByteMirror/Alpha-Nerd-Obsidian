---
ObjectType: Video
Context: 
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
value: 
tags: 
summary: 
people:
---
<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Videos/${filename}`);
const url = await tp.system.prompt("Please enter a URL:");
tR += "![]("+url+")";
%>

```button
name Start Note Taking
type command
action Media Extended: Open Media from Link
color default
```
## Video Notes

<% tp.file.cursor() %>

