# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Answer:
- The hints were backwards because when it says the answer is higher than expected, it was usually lower than expected.
- New Game: Game Over: Start a New Game to try again.
- The number of attempts: Normal=8>Easy = 6.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

- I use ChatGPT and Github Copilot for this project.
- One of the AI suggestion that it fixes is fixing the Enter button: I in the past feel that the "enter" don't really work and after fixing the code, I could feel code is done quickly and refactored pretty well.
- One of the AI suggestion that was incorrect: Pytest running not correctly: I changed the prompts to make sure it covered all of the code it needs to be.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- I think I really knows that a bug is really fixed when I saw the bugs fixing it: The state function is truly correct in the sense it reduces most visible bugs in the program.
- Pytest run the code for me: it shows the checking part in system design is partly correct.
- AI do help me design test: check about hint messages and ranges, parse guess: It do have most of the code context (expressible by tokens) and check for numerous kinds of inputs.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

- In my own words, the secret numbers keep changing because the Game state is not stable: it keep changing because there were hidden spots of the games that are recreating random nonces and seeds.
- Streamlit "reruns" happens because of some issues: it creates/reset server again
- The keeping of game state ultimately gave the game a stable secret number.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---
This project have changed me a lot about AI generated code. I believe that AI generated code is sometimes fuzzy, hard to relate and error prone, which means a lot of problems for coding. I believe that I have to fix a lot of AI codes, understand significant issues with AI and correctness, test coverage of programs to avoid significant issues.