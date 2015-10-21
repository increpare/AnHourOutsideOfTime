from copy import deepcopy

starthistory = [
	["time","Friday 14:29pm"],
	["left","See you at 8?"],
	["right","Sounds good! See you there."],
	["left","It's a date :D"]
]

options = [
	["time","Saturday 2:13am"],
	["options",
		"Yaaaar - I'm home",
		"Hey, I got back home",
		"Yo, back in one piece"
	],
	["time","Saturday 2:15am"],
	["options",
		"Thanks for the great night out",
		"You're lovely!",
		"Was a pleasure to meet you"],
	["time","Saturday 2:20am"],
	["options",
		"Is everything ok?",
		"Ping",
		"Yo!"],
	["time","Saturday 2:35am"],
	["options",
		"Are you there?",
		"Hey hey!",
		"PING PING"],
	["time","Saturday 2:52am"],
	["options",
		"Hey, is everything ok?",
		"What's up?",
		"Are you alright?"],
	["time","Saturday 3:01am"],
	["options",
		"Did I do something wrong?",
		"What happened?",
		"Are you still up?"],
	["time","Saturday 3:15am"],
	["options",
		"Hey, did I do something wrong?",
		"Are you annoyed with me?",
		"Why aren't you messagine me?"],
	["time","Saturday 3:30am"],
	["options",
		"Did I say something wrong?",
		"I thought you were really cool :(",
		"PING"],
	["time","Saturday 3:45am"],
	["options",
		"I thought you might like me - guess I was wrong",
		"I was looking forward to meet you again :(",
		"Maybe I should have gone home with you..."],
	["time","Saturday 3:48am"],
	["options",
		"You're no different from all men",
		"I suppose I wasn't your \"type\" then",
		"You're as shallow as the rest of them"],
	["time","Saturday 3:51am"],
	["options",
		"Wanna bang now?",
		"Gimme a call if you wanna have sex now?",
		"*take dick pick*"],
	["time","Saturday 4:00am	"],
	["options",
		"you know what fuck you",
		"fuck you you don't know what you're missing",
		"you really blew it!"],
	["time","Saturday 4:03am"],
	["options",
		"selfish cunt",
		"you're so fucking rude",
		"I'll just have to find someone else"],
	["time","Saturday 4:05am"],
	["options",
		"fuck you!",
		"fuck you!",
		"fuck you!"]
]

header = """
<html>
<head>
<style>
.messageouter {
    width:100%;

    /* Firefox */
    display:-moz-box;
    -moz-box-pack:center;
    -moz-box-align:center;

    /* Safari and Chrome */
    display:-webkit-box;
    -webkit-box-pack:center;
    -webkit-box-align:center;

    /* W3C */
    display:box;
    box-pack:center;
    box-align:center;
}

.date {
	text-align: center;
}

.messagewindow {
  width:500px;
}
.messageboxleft {
	position:relative;
	left:0%;
	width:70%;
	margin:5px;
	border:1px solid black;
	border-radius:5px;
	padding:5px;
	min-height: 50px;
}
.messageboxright {
	position:relative;
	left:30%;
	width:70%;
	margin:5px;
	border:1px solid black;
	border-radius:5px;
	padding:5px;
	width:70%;
	min-height: 50px;
}
.iconleft{ 
	display:inline-block;
	float:left;
	width:50px;
	margin-right: 5px;
	height:50px;
	left:0;
	background-color:purple;
}
.iconright {
	margin-left: 5px;
	display:inline-block;
	float:right;
	right:0;
	width:50px;
	height:50px;
	background-color:blue;
}
.options {
	position:relative;
	left:30%;
	width:70%;
	margin:5px;
	border:1px solid black;
	border-radius:5px;
	padding:5px;
	width:70%;
	min-height: 50px;
}
</style>
</head>
<body>
	<div class="messageouter">
	<div class="messagewindow">
"""

footer = """
	</div>
	</div>
</body>
</html>
"""

def printPage(history,choicelist,pastchoices):
	line = "PRINTPAGE " +str(history)+str(pastchoices)
	f = open("bin/"+pastchoices+".html",'w')
	f.write(line) # python will convert \n to os.linesep
	f.close()

def generatePages(position,curhistory,pastchoices):
	if position==len(options):
		printPage(curhistory,pastchoices,"")
		return	

	line = options[position]
	curhistory=deepcopy(curhistory)
	if line[0]=="time":		
		curhistory.append(line)
		generatePages(position+1,curhistory,pastchoices)
		return

	printPage(curhistory,line,pastchoices)

	for i in range(1,len(line)):
		newhistory = deepcopy(curhistory)
		newhistory.append(["right",line[i]])
		generatePages(position+1,newhistory,pastchoices+str(i))		

generatePages(0,deepcopy(starthistory),"")