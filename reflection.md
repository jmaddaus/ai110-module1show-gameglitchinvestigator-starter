<!-- @format -->

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The game loaded into a new game automatically when it was loaded.
Bug 1: The hints appear to be incorrect. I started at 50 and logarithmically followed hints, ending up at the limit and was told the secret was the other direction.
Bug 2: New Game button doesn't appear to work.
Bug 3: The attempts left appear to be off by one, and if you do a new game, it credits you an extra (at least display), and if you refresh the page it shows the correct value.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude.
The AI suggested that the hint logic was reversed (e.g. if the guess was below the answer, it incorrectly hinted to go lower). I reviewed the code and validated that the logic was incorrect.
I didn't run into any cases where the AI gave incorrect or misleading responses this time.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I determined if a bug was fixed by test suite, as well as by testing the application live.
The test suite injected values to assert outputs for various functions as unit tests to determine if expected results were yielded by the input. Additionally, functional tests of the app determined the behavior was corrected.
The AI was able to help write unit tests effectively, but in this case it made more sense for me to test the gameplay since it was a simple loop.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number wasn't exactly changing - but the problem is the reverse suggestions implied it was dancing around.
Streamlit repeats input and output in sequence and session state is the concept of a declaratively tracking the state of a user session by tracking state changes and data.
I fixed the the hint so you could tell which direction the number really was from your guess.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I use a lot of similar techniques when doing agentic engineering, and will continue to use them. I should spend more time proactively investigating areas (especially CSS) without overdescribing spatial relations.
I definitely prefer agents vs the chat only component. It is 'riskier' if you don't bound it due to the propensity of agents to take actions, but it is more fluid.
This project didn't really change how I think about AI generated code, but it was interesting to look at a different stack that I normally don't come across.
