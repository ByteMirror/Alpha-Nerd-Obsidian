---
ObjectType: Assignment
Context: 
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
dueDate: 
tags: 
resources: 
status: false
summary: 
people:
---
<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Assignments/${filename}`);
_%>


> [!Tipp] Task
> Contents

## 📝 Notes
-      <% tp.file.cursor() %>



