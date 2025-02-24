# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
I had to use copilot for the first aprt of the assignment because I am shaky with josn and streamlit still even after reading the text and watching the video. I am beginning to understand a basic level knowledge about them though. Specifcally striping, scanning, seeking, and sorting files. 

One thing I had a very difficult time with was importing and getting packaging.py as my program was saying this was not recognized. I believe this was because I overcomplicated my input and output method. I am quite familiar with Java and it is very common to use variable for almost everything but a lot that we do in class can be done without it. 

I utilized copilot a good amount, specifically so it could explain errors and things that it was suggesting. I was not understanding how parse_packaging_data was being imported and what it was doing in terms of spilt, processing, and eventually extracting the information. Things like st.text and st.info are basic fundementals of streamlit that I am understanding the more I work within the program. One thing I still do not understand includes how sreamlit and json use seek and keys features. I know now after reading some provided resources that item acts as a dictionary and keys returns the object and displays a list of keys in the dictionary. The key itself is a method-- that confused me because sometimes a key is similar to a password, in this case it a method of display. 

Finally, I had to figure out what seek was because I have seen it used before in other programs but I did not fully understand. I now know that seek is a positioning method that changes a objects file position. It forces my code to run smoother and not get backed up when reading the file after already reading it. Copilot also added in some helpful comments into my code regaarding how seek functions actually move through the program. 

Turns out:

I actually messed up process_file. I found that I actually had 
 st.success(f"Total 📦 Size: {total} {unit}")
 instead of...
 st.success(f"{line} Total 📦 Size: {total} {unit}") 
 **line adds for additional context BEFORE the size of the message. 
Additionally, 
I made to understand that my term "w" overwrites code segments ensuring that even if there is an error the block of code is executed. 

Process_files.py 

At first, I did not intialize my session and was getting a lot of errors in my code. When I did get results-- they were disorganized because each text file was not spilt into session. I discuss below. 

I was able to have a count and total line processes but it was displaying all of the data I previously needed in process_file. Instead of using session and grouping techniques. I got very confused on the last part here-- but I realized that the solution used
 for s in st.session_state.summaries:
        st.info(s, icon="💾")
moved the code above outside of the st.success command. 

AND...
    sum= (f"{count} packages written to {json_filename}")
was made into a seperate command. I did not know that seperating these two was used for summarization. By moving the icon command out of the original function it summarizes the second session. 

The solution uses this snippet which I ended up using because I could not understand another way.

st.session_state.summaries.append(sum)
    st.session_state.total_files += 1
    st.session_state.total_lines += count
After this, I left in my original count code. That was counting every single thing (packages, items and objects in said packages). Threw me off. 
Overall, 
I will be making an appointment with Professor becuase I am very confused even though I have been working with this for two weeks. 
