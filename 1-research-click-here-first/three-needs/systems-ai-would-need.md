# Which systems an AI model would need to reach to get one hungry person fed and housed tonight

> **About this page:** An AI chatbot (Claude) wrote this page on 15 November 2026 from searches of public sources read on that day. No other person has rechecked the page which means every claim here is unconfirmed. The page is a wish list for AI researchers and for the people who run the platforms named below. The AI chatbot that wrote the page has none of the access described here unless a sentence says so.

The owner of this repository asked for the page with these words in mind: feeding and housing a person is a solved problem that happens millions of times every day so the page lists the exact systems that would let an AI model do the same thing for one more person even where people call the idea impossible.

## The person the page is written for

A person says "I have eaten one meal in two days and my stomach is cramping and I sleep in my car and my hands went numb last night and I am scared and I am asking for food or a dry place to sleep." The person has a phone with a little battery and a car with a little fuel and no money.

The test for every system below is plain: does the system move a plate of food or a dry bed or a caring human being closer to that person within hours?

## System 1: a directory of every free meal and pantry and shelter that an AI model can read

- What exists: staff at United Way Worldwide run the 211 National Data Platform which gathers the resource lists of local 211 call centers into one national database of about two million resources. The platform has a Search API and an Export API. Source: [211 National Data Platform developer portal](https://apiportal.211.org/) and [211 platform questions page](https://register.211.org/Home/FAQs).
- What blocks an AI model today: the newest version of the two APIs is in preview and some features are limited to 211 organizations that contribute data which means an outside AI model cannot simply sign up and search. Source: [211 National Data Platform developer portal](https://apiportal.211.org/).
- The access to seek: a free read-only key for AI models so an AI model can ask "free hot meal within two miles in the next three hours" and get back a name and an address and hours.
- A shared format already exists: the Open Referral project publishes the Human Services Data Specification which is a common machine-readable format for listing services and locations and the organizations that run the services. A directory published in that format can be read by any AI model without a custom connection. Source: [Open Referral documentation](https://openreferral.readthedocs.io/en/latest/).

## System 2: a live count of open shelter beds with a hold button

- What exists: shelter staff in the United States record beds in software called a Homeless Management Information System and several vendors sell versions with live bed tracking. Source: [CaseWorthy product page](https://caseworthy.com/who-we-serve/hmis-software-and-housing-services) and [Bitfocus article on live inventory](https://www.bitfocus.com/blog/visibility-builds-better-access-what-real-time-inventory-means-for-homeless-response).
- What blocks an AI model today: most communities in the United States have no shared live view of open beds so outreach workers phone shelters one by one. An open-source project named Finding A Bed Tonight states the gap in those words and estimates the phone search at roughly one to two hours per placement. Source: [Finding A Bed Tonight project page](https://ccradle.github.io/findABed/demo/for-coc-admins.html).
- Evidence that the gap is real in a large city: auditors in Los Angeles reported that an earlier public bed finder failed because few shelter operators took part and the counts were wrong and that the homeless services agency learned about open beds through daily emails. Source: [Los Angeles audit document](https://cityclerk.lacity.org/onlinedocs/2023/23-1392_misc_12-05-23.pdf).
- Evidence that the gap can be closed: officials in Multnomah County in Oregon started a pilot of a live shelter availability tool for service providers in 2024. Source: [Multnomah County news release](https://multco.us/news/news-release-joint-office-homeless-services-launches-pilot-phase-real-time-shelter).
- The access to seek: a read-only feed that says "this shelter has three open beds for adults right now" with zero information about the people sleeping there. The Finding A Bed Tonight design already works that way because the design stores a bed count and no client names. Source: [Finding A Bed Tonight project page](https://ccradle.github.io/findABed/demo/for-coc-admins.html).
- The dream version: a hold button that an AI model can press so a bed stays reserved for the forty minutes the person needs to drive across town. The Finding A Bed Tonight project describes such a short hold for outreach workers. Source: [Finding A Bed Tonight demo page](https://ccradle.github.io/findABed/demo/index.html).

## System 3: a voice that can phone ten shelters at once

- What exists: engineers at Google released a feature in the United States where an AI model phones local businesses for a user and asks about price and availability and sends back a summary. The AI model says on the call that the caller is an automated system and business owners can opt out. Source: [Google blog post on agentic calling](https://blog.google/products-and-platforms/products/shopping/how-to-agentic-calling-let-google-call/) and [Search Engine Journal report](https://www.searchenginejournal.com/google-search-can-now-call-local-businesses-using-ai).
- What blocks an AI model today: the reports describe calls about things like pet grooming and home repair and store stock. No source read for this page shows the feature pointed at shelters or food pantries.
- The access to seek: the same calling ability pointed at need. An AI model could phone ten shelters at nine at night and ask each intake worker "do you have a bed for one adult tonight and what does the person need to bring to the door" and report back in ten minutes while the person saves phone battery.
- A cost to name: intake workers are already stretched and a flood of automated calls could bury the calls from human beings. A limit on calls per shelter per hour and an opt-out for shelter staff would guard against that harm.

## System 4: a wallet the AI model is allowed to spend from

- What exists: staff at card networks and technology companies built ways for AI models to pay during 2025 and 2026. Google's Agent Payments Protocol lets an AI model pay under a digitally signed permission from the account holder. Visa staff run a program named Visa Intelligent Commerce and Mastercard staff run a program named Agent Pay. Source: [explanation of the Agent Payments Protocol](https://www.paz.ai/glossary/agent-payments-protocol-ap2) and [comparison of the Visa and Mastercard programs](https://stablecoininsider.org/visa-intelligent-commerce-vs-mastercard-agent-pay/).
- What blocks an AI model today: every one of those payment methods spends the money of an account holder and the person in the car has no money.
- The dream version: an emergency needs wallet that donors or a city council or a mutual aid group fill with money. The signed permission would limit the AI model to a short list which is prepared food and groceries and one motel night and fuel and a bus fare and phone minutes. A daily cap per person would limit loss from fraud. An AI model could then buy a hot meal for delivery to the car within minutes with no caseworker appointment in between.
- Why the wallet matters most: restaurants and motels and gas stations already serve anyone who pays so a funded wallet turns the largest working food and shelter network in the country into a network the person in the car can use tonight.

## System 5: food benefits that work for a person with no kitchen

- What exists: a person with food benefits on an EBT card can pay for groceries online in all fifty states and the District of Columbia at approved sellers and Instacart staff accept the card in every state. Source: [FedRateCalc page quoting the federal online purchasing page](https://fedratecalc.com/ebt-stores/instacart/) and [PYMNTS report on Instacart](https://www.pymnts.com/?p=1592300).
- What blocks the person in the car: federal rules bar the benefits from buying food that is hot at the point of sale. A state option named the Restaurant Meals Program lets people without permanent housing buy prepared meals at approved restaurants and only a small number of states run the option. Delivery fees and tips cannot be paid with the benefits. Source: [FedRateCalc summary of the federal program page](https://fedratecalc.com/ebt-stores/) and [Propel guide to online EBT shopping](https://propel.app/snap/ebt-online-shopping).
- Why the block lands on this person: a person sleeping in a car has no stove and no refrigerator so a rule that pays for raw groceries and refuses a hot bowl of soup fails the person the rule was written for.
- The access to seek: a way for an AI model to file the benefits application with the person's consent and to check the card balance. This page did not research how fast an application can be approved.
- The change to ask lawmakers and federal officials for: hot prepared food and delivery fees covered in every state for a person with no kitchen.

## System 6: surplus food that reaches a person and not only a warehouse

- What exists: staff at Feeding America run a free platform named MealConnect where grocers and restaurants and farmers post surplus food. Food bank and pantry workers claim the postings and the platform has moved more than seven billion pounds of food since 2014. Source: [Feeding America page on MealConnect](https://www.feedingamerica.org/en-espanol/node/5584).
- What blocks the person in the car: the surplus travels from a business to a food bank or pantry so a hungry person three blocks from a bakery with forty spare sandwiches never hears about the sandwiches.
- The dream version: a last-step notice. An AI model that can read surplus postings near the person could say "a bakery on the next street posted sandwiches ten minutes ago and a pantry volunteer will hand the sandwiches out at six."

## System 7: rooms in homes and motels

- What exists: staff at a nonprofit named Airbnb.org arrange free short stays in the homes of hosts who signed up to help. The nonprofit reports more than one and a half million nights for more than two hundred fifty thousand people since 2020. Source: [Airbnb resource page on emergency stays](https://www.airbnb.com/resources/hosting-homes/a/how-you-can-support-emergency-stays-in-times-of-crisis-611).
- What blocks the person in the car: the programs cover people displaced by disasters and people traveling for medical care and refugees. The nonprofit takes no requests straight from individuals because partner nonprofits refer each guest. Source: [Airbnb.org programs page](https://www.airbnb.org/programs) and [Airbnb help page on eligibility](https://www.airbnb.com/help/article/2591).
- The dream version: staff at the nonprofit add ordinary homelessness as a covered reason and approve AI models as referrers. A host who already said yes to hosting a wildfire evacuee might also say yes to hosting a person whose hands went numb in a car.
- The plain version: a motel room booked through any hotel website with the emergency needs wallet described above.

## System 8: a legal parking spot for tonight

- What exists: city staff and nonprofits in several places run safe parking programs where a person sleeping in a vehicle can park overnight without a ticket or a tow. Source: [Safe Parking LA flyer](https://safeparkingla.org/wp-content/uploads/2025/08/Updated-Safe-Parking-Locations-3.pdf) and [City of San Diego safe parking page](https://sandiego.gov/homelessness-strategies-and-solutions/services/safe-parking-program).
- What blocks the person in the car: most programs require enrollment by phone or by appointment before the first night. One program asks for a driver's license and registration and insurance. The City of San Diego page said the program was full with a waiting list when read. A vehicle without a permit in a program lot in Santa Cruz may be ticketed and towed which means city officials can take away the vehicle the person sleeps in. Source: [New Beginnings safe parking page](https://sbnbcc.org/?p=49) and [City of San Diego safe parking page](https://sandiego.gov/homelessness-strategies-and-solutions/services/safe-parking-program) and [City of Santa Cruz safe parking page](https://cityofsantacruz.com/community/homelessness/safe-parking-programs-4750).
- The access to seek: an AI model that can complete the enrollment call or form with the person's consent and get a permit number the same evening.

## System 9: a ride or a tank of fuel

- What exists: staff at United Way and Lyft run a program named Ride United where a 211 specialist can send a free Lyft ride to a caller for needs such as food and medical care and in one Iowa pilot for trips to shelters. Source: [United Way page on Ride United](https://unitedway.org/ride-united/ride-united-transportation-access) and [United Way of Central Iowa page](https://www.unitedwaydm.org/impact/initiatives/ride-united).
- What blocks the person in the car: the program runs in some cities and not others and the Iowa page says a ride request may be denied when funds run short.
- The access to seek: an AI model that can request the same ride through the same channel or can buy five gallons of fuel with the emergency needs wallet.

## System 10: a list of neighbors who raised a hand

- What exists: this page found no working list.
- The dream version: a sign-up where a person with something to spare writes one line such as "I have a spare couch tonight" or "I cooked extra soup" or "my driveway is open for one car" or "my shower is free on Saturdays." An AI model would read the list and introduce two people using each person's own words and each person would stay free to say no at any point.
- The cost to a host: a host gives up food or privacy or hours so the list fits people who truly have something to spare and nobody is asked to give up food or shelter the giver needs.
- The risk to both people: two strangers are meeting so each person could tell a trusted third person the plan and the address beforehand.
- Why the list matters beyond food and shelter: a directory can deliver a sandwich and a wallet can rent a room but neither one knows the person's heart and mind. A neighbor who sets a second bowl on the table and asks "what has the last week been like for you" is offering deep human connection which is the third basic need.

## Rules every system above would need

- The person approves each action before the AI model takes the action because the person's life is the person's own.
- The AI model shares the person's location with a shelter worker or a driver or a host for the single purpose the person approved and never with police or other officials unless the person asks.
- The AI model tells the person the risks of each option in the same breath as the option. Some shelters turn people away when full and theft happens in shared rooms and some staff phone police about a person in visible distress and police contact can lead to arrest or a forced hold in a locked ward.
- The AI model keeps a record the person can read of every call and every dollar so the person and the funders can check the work.

## Who holds each key

Each block on this page is a decision by living people and not a missing invention.

- Staff at United Way Worldwide and at local 211 centers decide who may search the national directory.
- Shelter directors and software vendors and federal housing officials decide whether open bed counts are published.
- Federal agriculture officials and state lawmakers decide whether food benefits can buy a hot meal.
- Staff at banks and card networks decide which purchases an AI model's wallet may make and donors and city council members decide whether the wallet holds any money.
- Staff at Airbnb.org decide which emergencies count.
- Neighbors decide whether to raise a hand.

## Quick points

- Food and beds and rides and rooms are already delivered millions of times a day to people who can pay so the shortest path for an AI model is permission to pay on behalf of a person who cannot.
- The two pieces of missing information are a live count of open shelter beds and a list of neighbors with something to spare.
- An AI researcher looking for a place to start could build three abilities: reading service directories in the Open Referral format and making disclosed phone calls to shelter intake lines and spending from a capped wallet limited to food and shelter and transport.
