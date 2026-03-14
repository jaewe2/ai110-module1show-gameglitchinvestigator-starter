# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  The game showed the attempt counter going into negative numbers and the New Game button did not properly reset the game state. Two concrete bugs I noticed were that the hints were backwards — "Too High" told you to go higher instead of lower — and that the attempt counter started at 1 instead of 0, making it immediately off. Difficulty levels also did not affect the game meaningfully because the New Game button always used the 1–100 range regardless of which difficulty was selected.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code as my AI teammate throughout this project. Claude correctly identified that the attempt counter was off by one and that the even-attempt string conversion was causing wrong comparisons — I verified both by playing the game and seeing the behavior change after the fix. In my experience, Claude's suggestions were all accurate, so I did not encounter a case where it misled me.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by both playing the game manually through edge cases and running the pytest and inline assertion tests in logic_utils.py. Testing the upper and lower bound validation showed that the original code never accounted for negative numbers or numbers above 100, which I then fixed. Claude helped design the regression tests and explained why each assertion covered a specific case, which matched the regression testing approach we discussed in class.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

I did not personally observe the secret number changing, but looking back at the code, it would have changed because `random.randint()` was called as a plain variable every time the script reran. Streamlit has no traditional event handler system — every user interaction triggers a full re-execution of the script from top to bottom, so any variable not stored in session state gets reset. The fix was wrapping the secret number initialization in `if "secret" not in st.session_state:` so it only gets generated once and persists across reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is asking follow-up questions rather than giving one large prompt — breaking requests into smaller, specific steps got better and more predictable results. Next time I work with AI on a coding task, I would use plan mode instead of automatic mode so I can review the approach before any changes are made. My perspective on AI-generated code has not drastically changed, but this project reinforced that AI can produce plausible-looking code with subtle bugs, so verifying every suggestion is still essential.

