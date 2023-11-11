---
ObjectType: DailyNote
dateCreated: <% tp.file.creation_date("YYYY-MM-DD") %>
tags: 
importance: 
meditation: "0"
mood: 
workHours: 
exercised: 0
---
## ✅ To-Do

 - [ ] <% tp.file.cursor() %>


> [!Hint]-  Today's Tasks
> > [!abstract] _ 
>> ###  ⚔️ Your 3 Daily Quests 
>> ```tasks
> >not done
> >hide tags
> >short mode
>> tags include #Status/DailyQuest 
>> ```
> ### 📋 Backlog 
> ```tasks
> not done
> short mode
> hide tags
> (due on or after 7 days ago and status.type is not done)
> path does not include {{query.file.path}}
> ```
> ### 🎉 Done Today
> ```tasks
> done 
> group by status
> short mode
> done today
> ```

> [!summary]-  Meetings, Events & Notes
> ## 💾 Today's Files
> ```button
name Create New Object
type command
action Templater: Create new note from template
color default
> ``` 
>```dataview
TABLE file.tags as "Tags"
WHERE file.cday = this.file.day 
WHERE file.name != this.file.name 
WHERE file.folder != this.file.folder
WHERE file.folder != "textgenerator/prompts/default"
WHERE file.folder != "textgenerator/prompts/local"
SORT file.ctime DESC

> [!warning]- Inbox
> ##  🔗 Choose one to process
> 
> ```dataview
> TABLE file.mday as "Last Modified"
> FROM #TVZ
> sort file.mtime desc
> ```


## 🎯 Direction

This is what you're working towards!

![[<% tp.date.now("YYYY") %>-W<% tp.date.now("ww"), %>#<% tp.date.now("YYYY") %>-W<% tp.date.now("ww"), %> Goals]]


## ⏳ What to remember today for in a year?

- [*] 

## 🫖 People to catch up with

```dataview
TABLE dateLastSpoken
where followUp=true and dateLastSpoken <= date(today) - dur(1 month) and contains(ObjectType, "Person")
```

## 🪴 Daily Review


### 🌟 I'm proud that...

-   

### 🙌 I'm grateful that...

-   

### 📅 Tomorrow, I will...

- [ ] 

## 🌙 End-of-day checklist

- [ ] Get to Inbox Zero 
- [ ] prep for tomorrow
- [ ] Meditate


## 📔 Log




