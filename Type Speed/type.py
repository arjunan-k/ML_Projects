# ---------------------------------------------------------------------------------------------------------- #
import curses                               # Module to make a new layout in console.
from curses import wrapper                  # Initialize the module curses to make layout.
import random                               # To get a random string for this test.
import time                                 # To get the type speed in WPM.

# This are the strings fot the this type speed test.
STRING = ["On August, Apple made history by becoming the first trillion.",
          "Since 2010, Apple has been one of the most valuable companies in.",
          "Steve Jobs and Steve Wozniak co-founded Apple in 1977, introducing",
          "Bot performance and design are key drivers of the Apple brand",
          "The Apple drove the company's revenue until the mid-1980s,",
          "The 1984 release of the Macintosh was a leap forward for Apple.",
          "Sculley served as Apple's CEO until 1993 During those.",
          "Two CEOs, Michael Spindler and Gil Amelio, failed to turn",
          "Jobs believed a truly revolutionary product couldn't depend",
          "When Jobs overthrew Amelio and took Apple's reins once more."]


# A function to initialize the screen.
def start_screen(stdscr):
    stdscr.clear()                                          # Clear the screen.
    stdscr.addstr("Welcome to the Speed Typing Test!")      # Adding Strings in the screen.
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()                                        # To refresh screen after adding somethind to get new changes.
    stdscr.getkey()                                         # Wait for user to type something, then closes.


# To display the WPM in the console.
def display_text(stdscr, target, current, wpm=0):           # these are parameters. since wpm=0, it's optional no need to pass every time.
    stdscr.addstr(target)                                   # Add the text in position 0, 0.
    stdscr.addstr(1, 0, f"WPM: {wpm}")                      # 1, 0 denote 1 line dowm and move 0 to right.

    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(1))     # curses.colorpair(1) set the color of text green if we typed correctly.
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))     # curses.colorpair(2) set the color of text red if we typed wrongly.


# A function to find WPM.
def wpm_test(stdscr):                          # stdscr input clear screen for us and make the layout.
    target_text = random.choice(STRING)        # To get a random string fo the type test.
    current_text = []                          # List to store user's typing text.
    wpm = 0                                    # setting a variable wpm to initially zero.
    start_time = time.time()                   # Getting hold of time in second passed after Epoch.
    stdscr.nodelay(True)                       # This says donot delay waiting for the getkey().

    # A loop to check all of their input text letter by letter and calculate WPM.
    while True:
        time_elapsed = max(time.time() - start_time, 1)     # To get how many seconds passed. Max is used bcoz code runs so fast that it will be 0 at start.
        cpm = len(current_text) * (60 / time_elapsed)       # 30 char in 30s then our CPM = 60
        wpm = round((cpm / 5), 0)                           # Assuming each word have average length 5. Rounding to 0 ie integer.
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm=wpm)
        stdscr.refresh()
        if "".join(current_text) == target_text:            # To check user typed all and stop WPM.
            stdscr.nodelay(False)
            break

        try:                                               # Try method is to remove error even user doesn't type anything.
            key = stdscr.getkey()                          # Saves the typed in variable.

        except:                                            # If we didn't hit a key it loop agains and WPM counts.
            continue

        if ord(key) == 27:                                    # If they typed escape key program closes.
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):            # To remove the things they typed using backspace.
            # In different OS backspace will be represented differently. So "\b" "\x7f" denotes that.
            if len(current_text) > 0:
                current_text.pop()                            # pop remove the last text from the list current_text.

        elif len(current_text) < len(target_text):            # To stop the user to type more if they typed all.
            current_text.append(key)


# This function will give you a new Standard screen (stdscr) in the console.
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Setting some text colors.
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)       # 2 denote the id. We can use the id to use later.
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)     # 2nd is the color for text and 3rd is color for bg.

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test press any key to continue.")
        key = stdscr.getkey()
        if ord(key) == 27:      # 27 stands for escape key to break the program.
            break
        else:                   # Otherwise it will start type speed test with new text.
            continue

# Passing the main function to the wrappper function to run the program.
wrapper(main)
# ---------------------------------------------------------------------------------------------------------- #