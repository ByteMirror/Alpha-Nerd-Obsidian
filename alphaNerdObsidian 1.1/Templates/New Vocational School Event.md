---
ObjectType: Event
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
date: 
startTime: 
endTime: 
aliases: 
tags: []
Project: 
summary: 
people: 
completed: false
title:
---
<%*
let filename = await tp.system.prompt("Enter Event Name");
await tp.file.move(`/Calendar Views/Vocational School/${filename}`);
_%>

## 📝 Notes
-      <% tp.file.cursor() %>

## ✅ Action Items
-      [ ]

