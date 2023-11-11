---
ObjectType: Exam
Context: 
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
aliases: 
tags: 
Done: 
Score: 
dueDate:
---
<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Exams/${filename}`);
_%>

## 📚 Relevant Topics

- 
## ❓ Questions

-  [ ] 

## 📝 Notes



> [!Danger] Relevant Files
> ```dataview
> TABLE 
> dateformat(file.ctime, "yyyy-MM-dd") as "Date"
> WHERE contains(file.name, this.file.name) and file.name != this.file.name
> ```




