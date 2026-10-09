import tkinter as tk
import random

window = tk.Tk()

window.title("Rock. Paper. us? oh whatever.")
window.geometry("900x600")
window.configure(bg="#21152B")
window.resizable(False, False)

BG = "#21152B"
CIRCLE = "#493055"
SHADOW = "#100B14"
PINK = "#F8E8E0"
LIGHT_PINK = "#D9A8C7"
HOVER = "#63416D"

title = tk.Label(
    window,
    text="Rock. Paper. us? oh whatever.",
    font=("Literature", 30),
    fg=PINK,
    bg=BG
)

title.pack(pady=(30, 5))


subtitle = tk.Label(
    window,
    text="✦ choose your fate ✦",
    font=("Literature", 16),
    fg=LIGHT_PINK,
    bg=BG
)

subtitle.pack()


result = tk.Label(
    window,
    text="Choose your weapon.",
    font=("Literature", 17),
    fg=LIGHT_PINK,
    bg=BG
)

result.pack(pady=15)


canvas = tk.Canvas(
    window,
    width=900,
    height=400,
    bg=BG,
    highlightthickness=0
)

canvas.pack()


choices = ["Rock", "Paper", "Scissors"]


def play(player_choice):

    atom_choice = random.choice(choices)

    if player_choice == atom_choice:

        result.config(
            text=(
                f"You: {player_choice} |  "
                f"Atom: {atom_choice}\n"
                "Oh, it's a tie. Let's do it again."
            )
        )

    elif (
        (player_choice == "Rock" and atom_choice == "Scissors")
        or
        (player_choice == "Paper" and atom_choice == "Rock")
        or
        (player_choice == "Scissors" and atom_choice == "Paper")
    ):

        result.config(
            text=(
                f"You: {player_choice}  |  "
                f"Atom: {atom_choice}\n"
                "It was your day."
            )
        )

    # PLAYER LOSES
    else:

        result.config(
            text=(
                f"You: {player_choice}  |  "
                f"Atom: {atom_choice}\n"
                "Fahh, L bro."
            )
        )


def create_circle(x, name):

    shadow = canvas.create_oval(
        x - 90,
        155,
        x + 90,
        335,
        fill=SHADOW,
        outline=""
    )
    circle = canvas.create_oval(
        x - 90,
        145,
        x + 90,
        325,
        fill=CIRCLE,
        outline=LIGHT_PINK,
        width=3
    )
    text = canvas.create_text(
        x,
        235,
        text=name.upper(),
        font=("Literature", 17),
        fill=PINK
    )

    canvas.addtag_withtag(name, circle)
    canvas.addtag_withtag(name, text)


    canvas.tag_bind(
        name,
        "<Button-1>",
        lambda event: play(name)
    )



    canvas.tag_bind(
        name,
        "<Enter>",
        lambda event: canvas.itemconfig(
            circle,
            fill=HOVER
        )
    )

    canvas.tag_bind(
        name,
        "<Leave>",
        lambda event: canvas.itemconfig(
            circle,
            fill=CIRCLE
        )
    )



create_circle(180, "Rock")
create_circle(450, "Paper")
create_circle(720, "Scissors")


footer = tk.Label(
    window,
    text="one choice. one winner.",
    font=("Literature", 14),
    fg="#A987B0",
    bg=BG
)

footer.pack()
window.mainloop()