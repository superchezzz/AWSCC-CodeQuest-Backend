import random

print("\t   🚀 Welcome to WebDev Simulator: Where Code Meets Creativity!Game!🌐\n\tNavigate through a branching path of projects, challenges, and opportunities.\nWill you focus on creating stunning user interfaces, optimizing server-side performance, or both?\n  The choices you make will shape your virtual career and determine the projects you tackle.")
print("\nWould you like to proceed? [Yes or No]")
proceed= input(">> ").capitalize()

if proceed == "Yes":
    print("Please enter your name:")
    name=input(">> ").capitalize()
    print(f"\t\t\tHello {name}! 🌐 Choose Your Development Path\n\tForge your path through the interconnected roads of HTML, CSS, JavaScript, and beyond. \nWill you specialize in the front-end arts, master the server-side mysteries, or become a full-stack explorer? \n\tThe choice is yours. Every decision you make shapes your roadmap and defines your expertise!")
    print("\t\t\t[Front-end, Backend, or Full-stack]")
    dev_path=input(">> ").capitalize()

    if dev_path == "Front-end":
        print("\n\nWelcome to Front-end! Ready to shape the visual web? Dive into the world where creativity meets code! 💻✨\nFirst Task: Learn HTML and CSS")
        proceed_html=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
        if proceed_html=="Yes":
            print("\nWow! Congratulation on finishing the first lesson!! It took you", random.randint(7,14),"days to master HTML and CSS😎😎😎\nTo know if you successfully master the HTML and CSS, you are assigned to create a blog post!")
            enter1= input("press Enter if you want to do this task.\ntype \"skip\" if you want to skip\n>> ").lower()
            if enter1=="":
                print(f"Wow! Great job {name}. It seems like you are ready to proceed to the next lesson!!")
            else:
                print(f"It's okay {name}! let's proceed to the next topic!")

            print("\n\nSecond Task: Learn Responsive Web Design!")
            proceed_responsive=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
            if proceed_responsive=="Yes":
                print(f"Bravo {name}! You've navigated through challenges and completed the task with excellence. It took you", random.randint(7,14),"days to understand media queries and flexible grid systems!😍😍")
                print("\n\nThird Task: Learn JavaScript!")
                proceed_js=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
                if proceed_js=="Yes":
                    print(f"You're doing great {name}! Or can I call you Master {name} >∼< 👉👈. It took you", random.randint(20,60),"days to learn the basics of JS!😍😍")
                    print("\n\nFourth Task: Explore Document Object Model (DOM) manipulation with JavaScript.")
                    proceed_dom=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
                    if proceed_dom=="Yes":
                        print(f"Your skills are unmatched {name}!You've completed the task like a pro :0 It took you", random.randint(10,20),"days to learn dynamic content updates and event handling.")
                        print("\nIt seems like you're ready to dive into popular frameworks like ReactJS, Angular, or Vue.js. \nFifth Task: Frontend Frameworks")
                        proceed_fwork=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
                        if proceed_fwork=="Yes":
                            framework=["React", "Angular", "Vue.js"]
                            print(f"Outstanding work Master {name}! You've successfully conquered the task and successsfully learned", random.choice(framework),". It took you", random.randint(60,90),"days to learn a JS Framework🥳🥳🥳")
                            print("\n\nYou've reached the finish line! The mission is accomplished, and your commitment to excellence is truly inspiring.\nBut it's not yet finished 😉 you must still develop and enhance your skills!\nYou must gain and build a great experience and apply to different companies. Show off your skilL! and earn a lot of money🤑🤑🤑")
                            front_job=input("Do you want to apply for a front-end developer job? [Yes or No]:\n>> ").capitalize()
                            if front_job == "Yes":
                                company=["Innofied", "Cyber Infrastructure Inc.", "Clarion Technologies","Finoit Technologies", "IndiaNIC Infotech Limited", "Consagous Technologies", "Konstant Infosolutions","Icecube Digital", "eSparkBiz", "Techwings", "Webspero solutions", "Speednet", "Highland Solutions", "Consensus Creative"]
                                print(f"What a great news {name}!!", random.choice(company), "hired you as a front-end developer and offer a salary of $", random.randint(30,60),f"per hour. Goodluck WebDev {name} on your journey!!")
                            elif front_job == "No":
                                print(f"It's okay {name}! Don't forget to enhance your skills and study everyday! Goodluck on your journey and see you next time Sensei🙇🙇🙇!")
                            else:
                                print("Invalid choice.")
                        elif proceed_fwork=="No":
                            print(f"It's okay {name}! Take a rest for a while! See you next time!")
                        else:
                            print("Invalid choice.")
                    elif proceed_dom=="No":
                        print(f"It's okay {name}! Take a rest for a while! See you next time!")
                    else:
                        print("Invalid choice.")
                elif proceed_js=="No":
                    print(f"It's okay {name}! Take a rest for a while! See you next time!")
                else:
                    print("Invalid choice.")
        else:
            print(f"Aw :<, see you next time {name}!")
    elif dev_path== "Back-end":
        print("\n\nWelcome to Back-end! Ready to build the backbone of the digital realm? Let's code the engine that powers innovation! 💻🚀✨\nFirst Task: Learn HTML and CSS")
        proceed_html=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
    elif dev_path == "Full-stack":
        print("\tUnleash your coding prowess as a Full Stack Developer. From crafting seamless front-end\nexperiences to optimizing server-side performance, your skills shape the digital landscape. Ready\n\tto conquer both ends of the spectrum? Let's code the future together! 💻🌐")
    else:
        print("Invalid choice.")
elif proceed == "No":
    print("See you next time!")
else:
    print("Invalid choice.")
print("Thank you for playing WebDev Simulator Game!")