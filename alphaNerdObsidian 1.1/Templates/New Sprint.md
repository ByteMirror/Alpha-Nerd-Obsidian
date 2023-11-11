---
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags:
  - FrontendClient
accpetanceCriteria: 
UserStory: 
URL: 
jiraStatus: 
ObjectType: Ticket
Context: BBraun
---

<% tp.file.cursor() %>


<%*
let filename = await tp.system.prompt("Enter the filename");
await tp.file.move(`/Work/Sprints/${filename}`);
%>
## 🗓️ Log


## ✔️ To-Do


## 🎓 New Knowledge


## 📋 Summary


## ✅ Completed Tickets
> [!FAQ] Completed Tickets
> ```dataview
> TABLE
date as "Date",
summary as "Summary"
FROM #ObjectType/Ticket 
WHERE contains(sprint, this.file.link) AND contains(jiraStatus, "done")
SORT date desc
> ```

## 🚧 In Progress Tickets


## ⚠️ Challenges and Impediments


## 💡 Lessons Learned


## 🚀 Next Steps


## ✏️ Additional Notes


## 🔍 Retrospective

