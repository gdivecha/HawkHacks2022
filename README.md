# <strong>HawkHacks2022:</strong><br/> TALONS: Sink your talons into a future with heightened productivity

<img src=https://cdn.discordapp.com/attachments/975045520626163772/975402674373660682/189A5203-78EC-473B-A794-26793EF12D08.jpg width="500">

<strong>Description:</strong> :microscope:<br />
The hunt for productivity is preyed on by Talons, the sharpest discord bot! Talons is your peak performance sidekick armed with the pomodoro technique, reminders and SMS for your next mission.

<strong>Inspiration:</strong> :bulb:<br />
We noticed issues firsthand in terms of productivity and completing tasks. As students who religiously use discord, while we are on our laptops/desktops working, we miss reminders on our silent phones or forget to actually complete tasks or attends events. This inconvenience gave us the opportunity to create Talons, the discord bot. Talons brings a well rounded productivity experience, with a built in pomodoro technique, personal reminders with pings ans SMS.

<strong>What it does:</strong> :dart:<br />
Have you ever lost track of your tasks and reminders when you’re on discord? Have you ever felt that having a multi-purpose task-notifier could be beneficial to you? Our discord bot “Talons” is the perfect way to set up your important reminders and tasks that you so often forget. This discord bot is a multi-purpose productivity tool that will help you organize your tasks an stay on track using the following commands:
- $setup <phonenumber(e.g. +16477238263)> <emailAddress(e.g. talons.mlh@gmail.com)>
- $replaceNumber <phonenumber(e.g. +16477238263)> 
- $replaceEmail <emailAddress(e.g. talons.mlh@gmail$.com)>
- $addReminder <message(e.g. “walk your dog”)> <message(e.g. “20:12:33”)>
- $deleteReminder <message(e.g. “walk your dog”)> <message(e.g. “20:12:33”)>
- $showReminders
- $pomodoro <workTime(e.g. “00:50:00”)> <breakTime(e.g. “00:10:00”)>
- $startWorkTime
- $startBreakTime<br /><br />
Using these commands, you will be able to:
- Setup a phone number and an email address that you would like the reminder to be sent to
- Replace the phone number you inputted with a new one
- Replace the email address you inputted with a new one
- Add a reminder with the message and the intended time
- Delete a reminder with the message and the intended time
- Show your current reminders
- Add a pomodoro timer for your work and break routine
- Execute your work time routine
- Execute your break ime routine
……
This bot will send you an SMS wih your personalized message as a reminder, mention you in the discord channel and it can even be extended so that it can email you with a link you would like to join for a zoom meeting, just so you can keep track of your tasks. Our domain allows you to access our services as well.

<strong>How we built it:</strong> :question:<br />
We built it using Python, JavaScript, CSS, HTML, the nextCord API and the Twilio API. We used Python to develop the bot commands to work in sync with the nextCord API. We made several commands, but out biggest concern was coming up with a suitable database to manipulate different instances of the bot for each specific user. As the Discord IDs are very long, we considered using Hashtables, but we then found a better solution - Disctionaries, which would be very simple to implement and it would also allow us to be more flexible with our options. Then, we integrated the Twilio API into the code so that each time a reminder is passed, its corresponding message also gets sent to the user as an SMS. We also made the code extendable to even emails if need be in the future. We made the website using JavaScript, CSS and HTML and styled it to suit our purposes. Along with the description of our bot, the download button allows the user to navigate the gitHub repository as well.

<strong>Challenges we ran into:</strong> :face_with_spiral_eyes:	<br />
When developing this bot, we planned on combine many different APIs and platforms and so, it became harder to implement the timer and it was quite challenging to maintain different instances of different users at the same ime, without losing track of each one. We found our way around it using appropriate use fo object allocation. Alsong with this, our busy schedule only allowed us to be available at  certain time, which is why we were limited to the functionalities we finalized.

<strong>Accomplishments that we're proud of:</strong> :mechanical_arm:<br /> 
Considering our lack of experience with the development of discord bots, we were able to successfully create a fully functioning multi-purpose bot that can completely help you keep track of you reminders and allow you to stay focused on ech task. We are very proud that we were able to interconnect different APIs and programming languages to make the final project work.

<strong>What we learned:</strong> :chart_with_upwards_trend:<br />
We learned how fast we are able to grasp the functinalities and implementations of new APIs and this opens up an array of prospects for us to explore during future hackathons. Our main purpose for creating this bot was to help people understand their importance of time, and in fact, this bot even helped us while developing it as we were also able to list tasks that were to be done.

<strong>What's next for Talons:</strong> :eagle:<br />
We have made this project very modifiable and scalable for future projects as well. We have even made the functionality of emails a possibility in the future. This project is quite ambitious considering how much traffic discord sees daily. Servers are always a great way of introducing new bots and these bots are a game-changer as a lot of people are active on discord, while they keep their phones or reminders on silent mode. This can even be extended into a domain that we are planning on creating in the future.

<strong>Where to find our video:</strong> :link:<br />


<strong>**Note:**</strong> :old_key:<br />
The Discord Bot TOKEN and the Twilio account information has not been included in this submission for security purposes

<strong>By:</strong> :brain:<br />
Gaurav Divecha (gdivecha), Vikram Prashar, Hanana Gohir (hananagohir), & Mohammad Al-Shallabi (Malshalab)
