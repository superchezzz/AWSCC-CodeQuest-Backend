import random

print("\t   🚀 Welcome to WebDev Simulator: Where Code Meets Creativity!Game!🌐\n\tNavigate through a branching path of projects, challenges, and opportunities.\nWill you focus on creating stunning user interfaces, optimizing server-side performance, or both?\n  The choices you make will shape your virtual career and determine the projects you tackle.")
print("\nWould you like to proceed? [Yes or No]")
proceed= input(">> ").capitalize()

if proceed == "Yes":
    print("Please enter your name:")
    name=input(">> ").capitalize()
    print(f"\t\t\tHello {name}! 🌐 Choose Your Development Path")
    print("\tForge your path through the interconnected roads of HTML, CSS, JavaScript, and beyond. ")
    print("Will you specialize in the front-end arts, master the server-side mysteries, or become a full-stack explorer? ")
    print("\tThe choice is yours. Every decision you make shapes your roadmap and defines your expertise!")
    print("\t\t\t[Front-end, Backend, or Full-stack]")
    dev_path=input(">> ").capitalize()

    if dev_path == "Front-end":
        print("\n\nWelcome to Front-end! Ready to shape the visual web? Dive into the world where creativity meets code! 💻✨")
        print("First Task: Learn HTML and CSS")
        proceed_html=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
        if proceed_html=="Yes":
            print("\nWow! Congratulation on finishing the first lesson!! It took you", random.randint(7,14),"days to master HTML and CSS😎😎😎")
            print("To know if you successfully master the HTML and CSS, you are assigned to create a blog post!")
            enter1= input("press Enter if you want to do this task.\ntype \"skip\" if you want to skip\n>> ").lower()
            if enter1=="":
                print(f"Wow! Great job {name}. It seems like you are ready to proceed to the next lesson!!")
            else:
                print(f"It's okay {name}! let's proceed to the next topic!")
            print("\n\nSecond Task: Learn JavaScript!")
            proceed_js=input("Would you like to proceed? [Yes or No]:\n>> ").capitalize()
            if proceed_js=="Yes":
                print("\nYou're close to the path of being a front-end developer{name}! It took you", random.randint(7,14),"days to learn the basics of JS!")
        else:
            print("aw")
    elif dev_path== "Back-end":
        print("Welcome to backend!")
    elif dev_path == "Full-stack":
        print("\tUnleash your coding prowess as a Full Stack Developer. From crafting seamless front-end\nexperiences to optimizing server-side performance, your skills shape the digital landscape. Ready\n\tto conquer both ends of the spectrum? Let's code the future together! 💻🌐")
    else:
        print("Invalid choice.")
elif proceed == "No":
    print("See you next time!")
else:
    print("Invalid choice.")
print("Thank you for playing WebDev Simulator Game!")