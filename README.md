# 🗺️ Guess the Indian State – A Python Turtle Geography Game 🇮🇳

> 🎯 *How well do you know India's geography? Test your knowledge by guessing all 28 states on a blank map!*  
> Built using **Python Turtle Graphics** + **Pandas** + your brain 🧠

---

## 🌟 Features

- 🐢 Turtle graphics-based visual interaction  
- 🗃️ CSV-powered data lookup for (x, y) coordinates  
- ✅ Real-time state name rendering on the map  
- 📁 Missing guesses saved in a CSV for future learning  
- 🧠 Great for learning Python and Indian geography together

---

## 🧩 How It Works

1. A blank Indian map is loaded using Turtle (`.gif` image)
2. User is prompted to guess a state’s name
3. If correct:
   - Name is written on the map at correct coordinates
   - Score increases
4. If user types `Exit`:
   - Remaining states are saved in `Missing_States.csv`
5. Game ends when all 28 states are guessed ✅

---
### 1️⃣ Install Requirements
```bash
pip install pandas
