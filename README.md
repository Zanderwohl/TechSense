# TechSense
A free hard Sci Fi RPG with variable crunch.

## Welcome to TechSense!

TS (for short) aims to provide a crunch-lite space adventure with a hard sci-fi background. Inspired by the works of authors like Robert Heinlein and Ursula K. Le Guin, TS aims to give truly alien experiences without delving into space-fantasy or space-opera. We designed this system to keep things at least a little realistic, without bogging players down with excessive math or killyjoy-type limits on what you can do.


Almost completely devoid of combat, TS instead focuses on role-playing and acquiring the skills necessary to traverse the universe. Skills are easy to acquire and level up, but take a lot of work to perfect. 


We hope you enjoy playing, but remember: if you don’t like something, change it, and ignore any rules that ruin your fun. If ”fun” to you is always following all the charts and calculating orbital transfers and insertations, then stick to that. If it means skipping by all that and just spending some fuel, then that’s fine too. This is only a guide, after all. The most important part is the people at the table.

## People

You'll probably want at least four people to play: one game master, and three players.Seven is probably the largest comfortable group.

## The Files

The only game book so far is Rules.pdf, which provides the rules framework for the game. It does not quite provide enough information to play as of yet.

### Changing the Rulebook

The rulebook for TechSense is written in some variety of LaTeX, with lots of packages tacked on. you can modify the files with any TeX editor, though I use TeXworks. TeXworks is tempramental, so I don't recommend it, strictly speaking.

After modifying the rulebook, typeset the rule.tex file, which references all the component .tex files that contain the rules themselves. Typeset twice if the table of contents is wrong or does not exist.

If changes are made to the skills tables or other tables, generate_skills.py and generate_table.py may need to be run. They can be run with

```
python generate_skills.py
```

or

```
python generate_table.py
```

respectively. Of course, you will need Python installed. I used Python 3.8.
