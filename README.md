# 📈 Higher Lower Followers Game 📉

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Game](https://img.shields.io/badge/Type-Console%20Game-orange.svg)]()
[![Day](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2014-red.svg)]()
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()

> 🎯 **Can you guess who has more followers?** Test your knowledge of social media popularity in this addictive guessing game!

## 🎮 About The Game

Higher Lower is an entertaining command-line game where you compare the follower counts of celebrities, brands, and organizations on social media. The goal is simple: guess which account has more followers and see how high you can score before making a wrong guess!

### 🌟 Features

- 🎲 **50+ Accounts** - Compare followers of celebrities, athletes, brands, and more
- 🏆 **Score Tracking** - See how many correct guesses you can make in a row
- 🎨 **ASCII Art** - Beautiful terminal graphics for an enhanced experience
- 🔄 **Continuous Play** - Accounts rotate seamlessly for endless fun
- 🌍 **Global Content** - Features accounts from around the world

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional packages required! 📦

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/qusai-Kagalwala/higher-lower.git
   cd higher-lower
   ```

2. **Run the game**
   ```bash
   python main.py
   ```

3. **Start playing!** 🎉

## 🎯 How to Play

1. 📺 The game shows you two accounts (A and B)
2. 🤔 Compare their descriptions and guess who has more followers
3. ⌨️ Type 'A' or 'B' and press Enter
4. ✅ If correct, your score increases and you get a new comparison
5. ❌ If wrong, the game ends and shows your final score
6. 🏆 Try to beat your high score!

### 📸 Game Preview

```
Compare A: Instagram, a Social media platform, from United States.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Cristiano Ronaldo, a Footballer, from Portugal.

Who has more followers? Type 'A' or 'B': 
```

## 📁 Project Structure

```
higher-lower/
│
├── main.py          # 🎮 Main game logic and loop
├── art.py           # 🎨 ASCII art for logo and VS display
├── game_data.py     # 📊 Account data with follower counts
└── README.md        # 📖 This file
```

## 🔧 Code Highlights

- **Clean Architecture**: Separated concerns with dedicated modules
- **Reusable Functions**: `format_data()` and `check_answer()` for modularity
- **Smart Game Flow**: Accounts rotate to create continuous gameplay
- **User Experience**: Screen clearing and consistent formatting

## 🎪 Sample Accounts

The game includes diverse accounts such as:

- 🌟 **Celebrities**: Ariana Grande, Dwayne Johnson, Taylor Swift
- ⚽ **Athletes**: Cristiano Ronaldo, Lionel Messi, LeBron James
- 🏢 **Brands**: Instagram, Nike, National Geographic
- 🎵 **Musicians**: Beyoncé, Justin Bieber, Billie Eilish
- And many more! 🎭

## 🛠️ Customization

Want to add your own accounts? Simply edit `game_data.py`:

```python
{
    'name': 'Your Account',
    'follower_count': 123,  # in millions
    'description': 'Account description',
    'country': 'Country'
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

### 💡 Ideas for Contributions

- 📊 Add more account data
- 🎨 Improve ASCII art
- 🏆 Add high score persistence
- 🌐 Add different categories/themes
- 📱 Create a GUI version

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 👩‍🏫 Inspired by Angela Yu's 100 Days of Code course
- 📱 Data represents approximate follower counts (may not reflect current numbers)
- 🎨 ASCII art created for enhanced terminal experience

## 📞 Contact

**Qusai Kagalwala** - [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)

Project Link: [https://github.com/qusai-Kagalwala/higher-lower](https://github.com/qusai-Kagalwala/higher-lower)

---

⭐ **Enjoyed the game?** Give this repo a star and share it with friends!
