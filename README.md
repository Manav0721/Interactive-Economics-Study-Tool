<div align="center">

# Interactive Economics Study Tool 📚

<p>An AI-powered study tool inspired by NotebookLM, designed to help students learn microeconomics through interactive Q&A, dialogue simulations, and video resources.</p>

</div>

<h2 align="center">🎯 Features</h2>

### 1. 📊 Overview Dashboard
- Complete study material overview
- Topics covered in the economics chapter
- Learning objectives and key features
- Visual feature boxes with learning topics

### 2. 💬 Interactive Q&A Chatbot
- Ask any economics question and get instant AI responses
- Real-time chat interface with conversation history
- Quick question suggestion buttons
- Topics covered:
  - ✅ Demand and Supply
  - ✅ Market Equilibrium
  - ✅ Elasticity (Price, Income, Cross)
  - ✅ Consumer Behavior and Utility
  - ✅ Production Theory
  - ✅ Cost Analysis
  - ✅ Market Structures

### 3. 🎙️ Audio Dialogue Mode
- Simulated teacher-student conversations
- Interactive learning through dialogue
- 12 comprehensive conversation exchanges
- Full transcript viewer
- Step-by-step concept explanations

### 4. 📹 Video Resources & Summaries
- Links to YouTube video lectures
- Video summaries and key takeaways
- Visual concept explanations with tables
- Comparison charts for market structures
- Exam preparation tips and strategies

---

<h2 align="center">🚀 Quick Start Guide</h2>

### Installation and Running

**Step 1:** Install dependencies
```bash
pip install streamlit PyPDF2
```

**Step 2:** Run the application
```bash
streamlit run app.py
```
Or if the above doesn't work:
```bash
python -m streamlit run app.py
```

**Step 3:** The app will open automatically at `http://localhost:8501`

---

<h2 align="center">💻 System Requirements</h2>

- **Python:** 3.8 or higher
- **Operating System:** Windows, Mac, or Linux
- **Browser:** Any modern web browser (Chrome, Firefox, Edge, Safari)
- **Internet:** Required for initial package installation

---

<h2 align="center">📚 Topics Covered</h2>

### Microeconomics Fundamentals

**1. Demand Analysis**
- Definition and Law of Demand
- Factors affecting demand
- Individual vs Market demand
- Demand curves and shifts

**2. Supply Analysis**
- Definition and Law of Supply
- Factors affecting supply
- Supply curves and shifts
- Producer behavior

**3. Market Equilibrium**
- Equilibrium price and quantity
- Surplus and shortage concepts
- Market clearing mechanisms
- Changes in equilibrium

**4. Elasticity**
- Price Elasticity of Demand (PED)
- Income Elasticity of Demand
- Cross Elasticity of Demand
- Price Elasticity of Supply
- Elasticity formulas and calculations

**5. Consumer Behavior**
- Utility theory
- Total and Marginal utility
- Law of Diminishing Marginal Utility
- Consumer equilibrium
- Budget constraints

**6. Production Theory**
- Factors of production (Land, Labor, Capital, Entrepreneurship)
- Short run vs Long run
- Total, Marginal, and Average product
- Production functions

**7. Cost Analysis**
- Fixed and Variable costs
- Total, Marginal, and Average costs
- Cost curves and relationships
- Economies of scale

**8. Market Structures**
- Perfect Competition
- Monopoly
- Oligopoly
- Monopolistic Competition
- Characteristics and pricing strategies

---

<h2 align="center">📖 How to Use</h2>

### Interactive Q&A Tab
1. Navigate to the "Interactive Q&A" tab
2. Type your economics question in the input field
3. Click "Ask Question" to get instant AI responses
4. View your conversation history below
5. Use "Clear Chat" to start a fresh conversation
6. Try quick question buttons for instant topics

### Audio Dialogue Tab
1. Go to the "Audio Dialogue" tab
2. Click "▶️ Play Dialogue Simulation"
3. Read through the teacher-student conversation
4. Learn concepts through interactive dialogue
5. Expand "View Full Transcript" for the complete conversation

### Video Resources Tab
1. Visit the "Video Resources" tab
2. Click on provided YouTube video links
3. Review video summaries and key concepts
4. Study the comparison tables and charts
5. Read exam tips for better preparation

### Overview Tab
1. Start here to understand all features
2. Review topics covered in the chapter
3. See what you'll learn
4. Get familiar with the tool's capabilities

---

<h2 align="center">💡 Sample Questions to Try</h2>

### Basic Concepts
- "What is demand?"
- "Explain the law of supply"
- "What is market equilibrium?"
- "Define elasticity"

### Detailed Explanations
- "What factors affect demand?"
- "How do you calculate elasticity?"
- "Explain consumer behavior and utility"
- "What is the difference between demand and supply?"

### Advanced Topics
- "What are the types of market structures?"
- "Explain perfect competition"
- "What is the law of diminishing marginal utility?"
- "How do costs affect production decisions?"

### Exam Preparation
- "Give me exam preparation tips"
- "What are the key formulas I need to know?"
- "How should I prepare for economics exam?"

---

<h2 align="center">🎨 User Interface Features</h2>

✓ **Clean, modern dark theme interface**  
✓ **Color-coded chat messages** (Blue for user, Green for AI)  
✓ **Responsive design** (works on desktop, tablet, mobile)  
✓ **Tab-based navigation** for easy access  
✓ **Interactive buttons** for quick actions  
✓ **Organized content sections** with clear headings  
✓ **Professional styling** with custom CSS  
✓ **Easy-to-read formatting** with proper spacing  

---

<h2 align="center">🛠️ Project Structure</h2>

```
APP/
│
├── .venv/                # Virtual environment (if using venv)
├── app.py                # Main Streamlit application (604 lines)
└── README.md             # This documentation file
```

**Note:** This is a minimal, focused project structure. All economics knowledge and functionality is embedded within `app.py`.

---

<h2 align="center">🔧 Technologies Used</h2>

- **Streamlit** - Web application framework
- **Python 3.8+** - Core programming language
- **PyPDF2** - PDF processing capabilities
- **Custom Knowledge Base** - Curated economics content
- **HTML/CSS** - Custom styling and UI components

---

<h2 align="center">⚠️ Troubleshooting</h2>

### Issue: "streamlit: command not found"
**Solution:** Run using Python module syntax:
```bash
python -m streamlit run app.py
```

### Issue: Port already in use
**Solution:** Use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Issue: Module not found
**Solution:** Install dependencies:
```bash
pip install --upgrade streamlit PyPDF2
```

### Issue: White text not visible
**Solution:** The CSS has been updated with proper text colors. Make sure you have the latest version of app.py

### Issue: Python not recognized
**Solution:** Use full Python path:
```bash
C:/Python312/python.exe launcher.py
```

---

<h2 align="center">✅ Assignment Requirements Met</h2>

✅ **Interactive Q&A Mode** - AI chatbot for student questions and clarifications  
✅ **Audio Dialogue Simulation** - Teacher-student conversation format  
✅ **Video Integration** - Links and summaries for YouTube videos  
✅ **Study Material Coverage** - All major economics concepts included  
✅ **Working Code** - Fully functional Streamlit application  
✅ **User-Friendly Interface** - Clean, intuitive design with tabs  
✅ **Professional Documentation** - Complete README and setup guide  

---

<h2 align="center">📊 Project Statistics</h2>

- **Total Lines of Code:** 500+
- **Features Implemented:** 4 major tabs
- **Topics Covered:** 8 main economic areas
- **Sample Dialogues:** 12 conversation exchanges
- **Knowledge Base Entries:** 8 comprehensive categories
- **Video Resources:** 2 YouTube lectures integrated
- **Documentation:** Complete README with examples

---

<h2 align="center">🎓 Learning Benefits</h2>

1. **Active Learning:** Ask questions as you study
2. **Visual Learning:** Video resources and comparison tables
3. **Conversational Learning:** Dialogue simulations
4. **Self-Paced:** Study at your own speed
5. **Comprehensive:** All topics in one place
6. **Interactive:** Engage with content actively
7. **Exam Ready:** Tips and strategies included
8. **Accessible:** Works offline after installation

---

<h2 align="center">📹 Input Sources</h2>

This study tool is based on:
- **Economics Chapter:** Microeconomics fundamentals PDF
- **Video 1:** [Microeconomics Concepts](https://youtu.be/Ec19ljjvlCI)
- **Video 2:** [Advanced Economics Topics](https://www.youtube.com/watch?v=Z_S0VA4jKes)

---

<h2 align="center">🚀 Deployment Options</h2>

### Option 1: Local (Current)
Run on your computer using the launcher or command line

### Option 2: Streamlit Cloud (Free)
1. Push code to GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy in one click
5. Get a public URL to share

### Option 3: Heroku
Deploy as a web application for broader access

### Option 4: Docker
Create a containerized deployment for consistent environment

---

<h2 align="center">🌟 Future Enhancements (Optional)</h2>

- [ ] Real text-to-speech audio generation
- [ ] PDF upload and processing functionality
- [ ] Integration with GPT-4 for advanced responses
- [ ] YouTube video transcript extraction
- [ ] Personalized study plans based on progress
- [ ] Quiz mode with scoring
- [ ] Flashcard generation
- [ ] Note-taking capabilities
- [ ] Export chat history as PDF
- [ ] Multi-language support

---

<h2 align="center">👨‍💻 Usage Tips</h2>

1. **Start with Overview:** Understand what's available before diving in
2. **Use Q&A Actively:** Don't hesitate to ask follow-up questions
3. **Read Dialogues:** See how concepts are explained conversationally
4. **Watch Videos:** Visual learning reinforces text-based learning
5. **Review Exam Tips:** Before assessments, check the tips section
6. **Try Quick Buttons:** Use suggestion buttons for instant explanations
7. **Clear Chat:** Start fresh when switching topics
8. **Bookmark Important:** Take notes of key explanations

---

<h2 align="center">📝 License</h2>

This project is created for educational purposes as part of an academic assignment.

---

<h2 align="center">🤝 Support</h2>

If you encounter any issues:
1. Check the Troubleshooting section above
2. Verify Python and pip are properly installed
3. Ensure you have internet connection for first-time setup
4. Try using `python -m streamlit run app.py` if the standard command doesn't work

---

<h2 align="center">🎉 Getting Started - Quick Commands</h2>

```bash
# Navigate to project folder
cd C:/Users/MANAV/Downloads/APP

# Install dependencies (first time only)
pip install streamlit PyPDF2

# Run the application
streamlit run app.py

# Alternative if above doesn't work
python -m streamlit run app.py
```

---

<div align="center">

**Happy Learning! 📖✨**

*Master economics concepts with AI-powered interactive assistance*

</div>

---

<div align="center">

**Created by:** Student Assignment Project  
**Framework:** Streamlit + Python  
**Purpose:** Interactive Economics Study Tool  
**Inspired by:** Google NotebookLM  

</div>
