import streamlit as st
import os
from pathlib import Path
import json
import time
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Interactive Study Tool - Economics",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        color: #000000 !important;
    }
    .feature-box h3, .feature-box h4,
    .feature-box p, .feature-box li {
        color: #000000 !important;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: #000000 !important;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 5px solid #1E88E5;
    }
    .bot-message {
        background-color: #F1F8E9;
        border-left: 5px solid #66BB6A;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'study_notes' not in st.session_state:
    st.session_state.study_notes = {}

# Economics content based on typical microeconomics chapters
ECONOMICS_KNOWLEDGE_BASE = {
    "demand": {
        "definition": "Demand refers to the quantity of a good or service that consumers are willing and able to purchase at various prices during a given period of time.",
        "law": "The Law of Demand states that, other things being equal (ceteris paribus), as the price of a good increases, the quantity demanded decreases, and vice versa.",
        "factors": [
            "Price of the commodity",
            "Income of the consumer",
            "Prices of related goods (substitutes and complements)",
            "Consumer preferences and tastes",
            "Consumer expectations about future prices",
            "Number of consumers in the market"
        ],
        "types": "Individual demand (single consumer) and Market demand (all consumers)"
    },
    "supply": {
        "definition": "Supply refers to the quantity of a good or service that producers are willing and able to offer for sale at various prices during a given period of time.",
        "law": "The Law of Supply states that, other things being equal, as the price of a good increases, the quantity supplied increases, and vice versa.",
        "factors": [
            "Price of the commodity",
            "Prices of inputs/factors of production",
            "Technology",
            "Number of sellers",
            "Government policies (taxes and subsidies)",
            "Expectations about future prices"
        ]
    },
    "equilibrium": {
        "definition": "Market equilibrium occurs when the quantity demanded equals the quantity supplied at a particular price, called the equilibrium price.",
        "concept": "At equilibrium, there is no tendency for the price to change as the market clears with no excess demand or supply.",
        "changes": "Shifts in demand or supply curves will create new equilibrium points with different prices and quantities."
    },
    "elasticity": {
        "definition": "Elasticity measures the responsiveness of quantity demanded or supplied to changes in price or other factors.",
        "types": [
            "Price Elasticity of Demand (PED): Responsiveness of quantity demanded to price changes",
            "Income Elasticity of Demand: Responsiveness to income changes",
            "Cross Elasticity of Demand: Responsiveness to changes in prices of related goods",
            "Price Elasticity of Supply: Responsiveness of quantity supplied to price changes"
        ],
        "formula": "Elasticity = (% Change in Quantity) / (% Change in Price)",
        "categories": {
            "elastic": "When elasticity > 1 (highly responsive)",
            "inelastic": "When elasticity < 1 (less responsive)",
            "unitary": "When elasticity = 1 (proportionate change)"
        }
    },
    "consumer_behavior": {
        "utility": "Utility is the satisfaction or pleasure derived from consuming a good or service.",
        "marginal_utility": "The additional satisfaction from consuming one more unit of a good.",
        "law_diminishing": "Law of Diminishing Marginal Utility: As consumption increases, the additional satisfaction from each additional unit decreases.",
        "consumer_equilibrium": "A consumer is in equilibrium when they maximize total utility given their budget constraint."
    },
    "production": {
        "definition": "Production is the process of transforming inputs (factors of production) into outputs (goods and services).",
        "factors": ["Land", "Labor", "Capital", "Entrepreneurship"],
        "short_run": "Period where at least one factor of production is fixed.",
        "long_run": "Period where all factors of production are variable.",
        "concepts": [
            "Total Product (TP): Total output produced",
            "Marginal Product (MP): Additional output from one more unit of input",
            "Average Product (AP): Output per unit of input"
        ]
    },
    "costs": {
        "fixed_costs": "Costs that do not vary with output level (e.g., rent, salaries)",
        "variable_costs": "Costs that vary directly with output level (e.g., raw materials)",
        "total_cost": "TC = Fixed Cost + Variable Cost",
        "marginal_cost": "The additional cost of producing one more unit of output",
        "average_cost": "Total cost divided by quantity of output"
    },
    "market_structures": {
        "perfect_competition": {
            "characteristics": "Many buyers and sellers, homogeneous products, free entry/exit, perfect information",
            "pricing": "Price takers - firms accept market price"
        },
        "monopoly": {
            "characteristics": "Single seller, unique product, barriers to entry, price maker",
            "pricing": "Firm has market power to set prices"
        },
        "monopolistic_competition": {
            "characteristics": "Many sellers, differentiated products, relatively free entry/exit",
            "pricing": "Some control over price due to product differentiation"
        },
        "oligopoly": {
            "characteristics": "Few large firms, interdependent decision-making, barriers to entry",
            "pricing": "Strategic pricing decisions considering rivals' reactions"
        }
    }
}

def get_ai_response(question):
    """Generate AI response based on question"""
    question_lower = question.lower()

    # Search through knowledge base
    response = ""

    # Check for greetings
    if any(word in question_lower for word in ["hello", "hi", "hey"]):
        return "Hello! I'm your AI Economics tutor. I'm here to help you understand economics concepts. Ask me anything about demand, supply, elasticity, consumer behavior, production, costs, or market structures!"

    # Check for specific topics
    if "demand" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["demand"]
        response = "**Understanding Demand:**\n\n"
        response += topic['definition'] + "\n\n"
        response += "**" + topic['law'] + "**\n\n"
        response += "**Factors affecting demand:**\n"
        for factor in topic['factors']:
            response += "- " + factor + "\n"
        response += "\n**Types:** " + topic['types']

    elif "supply" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["supply"]
        response = "**Understanding Supply:**\n\n"
        response += topic['definition'] + "\n\n"
        response += "**" + topic['law'] + "**\n\n"
        response += "**Factors affecting supply:**\n"
        for factor in topic['factors']:
            response += "- " + factor + "\n"

    elif "equilibrium" in question_lower or "market clearing" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["equilibrium"]
        response = "**Market Equilibrium:**\n\n"
        response += topic['definition'] + "\n\n"
        response += topic['concept'] + "\n\n"
        response += "**Important:** " + topic['changes']

    elif "elasticity" in question_lower or "elastic" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["elasticity"]
        response = "**Elasticity:**\n\n"
        response += topic['definition'] + "\n\n"
        response += "**Formula:** " + topic['formula'] + "\n\n"
        response += "**Types of Elasticity:**\n"
        for elas_type in topic['types']:
            response += "- " + elas_type + "\n"
        response += "\n**Categories:**\n"
        for category, description in topic['categories'].items():
            response += "- **" + category.title() + ":** " + description + "\n"

    elif any(word in question_lower for word in ["utility", "consumer", "satisfaction"]):
        topic = ECONOMICS_KNOWLEDGE_BASE["consumer_behavior"]
        response = "**Consumer Behavior:**\n\n"
        response += "**Utility:** " + topic['utility'] + "\n\n"
        response += "**Marginal Utility:** " + topic['marginal_utility'] + "\n\n"
        response += "**" + topic['law_diminishing'] + "**\n\n"
        response += "**Consumer Equilibrium:** " + topic['consumer_equilibrium']

    elif "production" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["production"]
        response = "**Production:**\n\n"
        response += topic['definition'] + "\n\n"
        response += "**Factors of Production:**\n"
        for factor in topic['factors']:
            response += "- " + factor + "\n"
        response += "\n**Short Run:** " + topic['short_run'] + "\n"
        response += "**Long Run:** " + topic['long_run'] + "\n\n"
        response += "**Key Concepts:**\n"
        for concept in topic['concepts']:
            response += "- " + concept + "\n"

    elif "cost" in question_lower:
        topic = ECONOMICS_KNOWLEDGE_BASE["costs"]
        response = "**Cost Concepts:**\n\n"
        response += "**Fixed Costs:** " + topic['fixed_costs'] + "\n\n"
        response += "**Variable Costs:** " + topic['variable_costs'] + "\n\n"
        response += "**Total Cost:** " + topic['total_cost'] + "\n\n"
        response += "**Marginal Cost:** " + topic['marginal_cost'] + "\n\n"
        response += "**Average Cost:** " + topic['average_cost']

    elif any(word in question_lower for word in ["market", "competition", "monopoly", "oligopoly"]):
        topic = ECONOMICS_KNOWLEDGE_BASE["market_structures"]
        response = "**Market Structures:**\n\n"
        for market_type, details in topic.items():
            response += "**" + market_type.replace('_', ' ').title() + ":**\n"
            response += "- Characteristics: " + details['characteristics'] + "\n"
            response += "- Pricing: " + details['pricing'] + "\n\n"

    elif "exam" in question_lower or "tip" in question_lower or "prepare" in question_lower:
        response = """**Exam Preparation Tips:**

1. **Understand Core Concepts:** Focus on laws of demand and supply, elasticity, and market equilibrium
2. **Practice Diagrams:** Be able to draw and explain supply-demand curves, shifts, and equilibrium changes
3. **Learn Formulas:** Memorize elasticity formulas and understand how to apply them
4. **Real-World Examples:** Connect concepts to current economic events
5. **Solve Numerical Problems:** Practice calculating elasticity, costs, and equilibrium prices
6. **Key Terms:** Create flashcards for important definitions
7. **Past Papers:** Review previous exam questions to understand patterns"""

    elif "difference" in question_lower:
        if "demand" in question_lower and "supply" in question_lower:
            response = """**Difference Between Demand and Supply:**

**Demand:**
- Consumer perspective
- Inverse relationship with price (Law of Demand)
- Shows buyer's willingness to purchase
- Affected by income, preferences, prices of related goods

**Supply:**
- Producer perspective  
- Direct relationship with price (Law of Supply)
- Shows seller's willingness to sell
- Affected by production costs, technology, number of sellers"""

    else:
        response = """I'd be happy to help you with economics! I can explain concepts about:

- **Demand and Supply:** Laws, factors, curves
- **Market Equilibrium:** Price determination
- **Elasticity:** Price, income, and cross elasticity
- **Consumer Behavior:** Utility theory
- **Production:** Factors, short run vs long run
- **Costs:** Fixed, variable, marginal costs
- **Market Structures:** Perfect competition, monopoly, oligopoly, monopolistic competition

Please ask a specific question about any of these topics!"""

    return response

def simulate_dialogue():
    """Generate pre-recorded teacher-student dialogue"""
    dialogues = [
        {
            "speaker": "Teacher",
            "text": "Welcome to today's lesson on Microeconomics! We'll be covering the fundamentals of demand and supply. Are you ready to begin?"
        },
        {
            "speaker": "Student",
            "text": "Yes, I'm ready! Can you explain what demand means in economics?"
        },
        {
            "speaker": "Teacher",
            "text": "Great question! Demand refers to the quantity of a good or service that consumers are willing and able to purchase at various prices during a given time period. The key words here are 'willing' and 'able' - both conditions must be met."
        },
        {
            "speaker": "Student",
            "text": "So if I want to buy something but can't afford it, that's not demand?"
        },
        {
            "speaker": "Teacher",
            "text": "Exactly! That would just be a desire, not economic demand. Now, there's an important principle called the Law of Demand. It states that as price increases, quantity demanded decreases, and vice versa, assuming all other factors remain constant."
        },
        {
            "speaker": "Student",
            "text": "That makes sense - when things get more expensive, people buy less. What about supply?"
        },
        {
            "speaker": "Teacher",
            "text": "Supply is the opposite side of the market. It's the quantity of a good that producers are willing and able to offer for sale at various prices. The Law of Supply states that as price increases, quantity supplied increases."
        },
        {
            "speaker": "Student",
            "text": "So sellers want to sell more when prices are higher because they can make more profit?"
        },
        {
            "speaker": "Teacher",
            "text": "Precisely! Higher prices incentivize producers to supply more. Now, when we bring demand and supply together, we get market equilibrium - the point where quantity demanded equals quantity supplied."
        },
        {
            "speaker": "Student",
            "text": "What happens if the market isn't at equilibrium?"
        },
        {
            "speaker": "Teacher",
            "text": "Excellent question! If price is above equilibrium, we get excess supply (surplus). If price is below equilibrium, we get excess demand (shortage). Market forces will push the price toward equilibrium."
        },
        {
            "speaker": "Student",
            "text": "This is really helpful! Can we talk about elasticity next time?"
        },
        {
            "speaker": "Teacher",
            "text": "Absolutely! Elasticity is crucial for understanding how responsive consumers and producers are to price changes. Keep studying, and you'll do great on your exam!"
        }
    ]
    return dialogues

# Main App Layout
st.markdown('<h1 class="main-header">📚 Interactive Economics Study Tool</h1>', unsafe_allow_html=True)
st.markdown("### Inspired by NotebookLM - Your AI-Powered Learning Companion")

# Create tabs for different features
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Overview", "💬 Interactive Q&A", "🎙️ Audio Dialogue", "📹 Video Resources"])

with tab1:
    st.header("Welcome to Your Economics Study Tool")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-box">
        <h3>🎓 What You'll Learn</h3>
        <ul>
            <li>Demand and Supply Analysis</li>
            <li>Market Equilibrium</li>
            <li>Price Elasticity</li>
            <li>Consumer Behavior Theory</li>
            <li>Production and Costs</li>
            <li>Market Structures</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
        <h3>✨ Features</h3>
        <ul>
            <li>AI-powered Q&A chatbot</li>
            <li>Teacher-Student dialogue simulations</li>
            <li>Video summaries and concepts</li>
            <li>Exam preparation tips</li>
            <li>Interactive learning experience</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📖 Study Material Overview")
    st.info("""
    **Chapter Topics Covered:**
    - Introduction to Microeconomics
    - Demand: Definition, Law, Determinants
    - Supply: Definition, Law, Determinants  
    - Market Equilibrium and Price Determination
    - Elasticity of Demand and Supply
    - Consumer Behavior and Utility Analysis
    - Production Function and Costs
    - Market Structures (Perfect Competition, Monopoly, etc.)
    """)

with tab2:
    st.header("💬 Ask Your Economics Questions")
    st.write("Chat with your AI tutor to get instant clarifications on any economics concept!")

    # Chat interface
    question = st.text_input("Type your question here:", placeholder="e.g., What is the law of demand?")

    col1, col2 = st.columns([1, 5])
    with col1:
        ask_button = st.button("Ask Question")
    with col2:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

    if ask_button and question:
        # Add user question to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": question,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

        # Generate AI response
        response = get_ai_response(question)

        # Add AI response to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

    # Display chat history
    st.markdown("---")
    st.subheader("Chat History")

    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown("""
                <div class="chat-message user-message">
                <strong>🙋 You ({}):</strong><br>
                {}
                </div>
                """.format(message['timestamp'], message['content']), unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="chat-message bot-message">
                <strong>🤖 AI Tutor ({}):</strong><br>
                {}
                </div>
                """.format(message['timestamp'], message['content']), unsafe_allow_html=True)
    else:
        st.info("👆 Start by asking a question above!")

    # Quick question suggestions
    st.markdown("---")
    st.subheader("📌 Quick Question Suggestions")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("What is demand?"):
            st.session_state.temp_question = "What is demand?"
    with col2:
        if st.button("Explain elasticity"):
            st.session_state.temp_question = "Explain elasticity"
    with col3:
        if st.button("Market equilibrium?"):
            st.session_state.temp_question = "What is market equilibrium?"

with tab3:
    st.header("🎙️ Teacher-Student Audio Dialogue")
    st.write("Listen to a simulated conversation between a teacher and student discussing economics concepts.")

    st.info("🔊 **Audio Feature:** This dialogue demonstrates interactive learning. In a full implementation, this would include text-to-speech audio generation.")

    if st.button("▶️ Play Dialogue Simulation"):
        dialogues = simulate_dialogue()

        st.markdown("---")
        for dialogue in dialogues:
            if dialogue["speaker"] == "Teacher":
                st.markdown("""
                <div class="chat-message bot-message">
                <strong>👨‍🏫 Teacher:</strong><br>
                {}
                </div>
                """.format(dialogue['text']), unsafe_allow_html=True)
                time.sleep(0.5)
            else:
                st.markdown("""
                <div class="chat-message user-message">
                <strong>👨‍🎓 Student:</strong><br>
                {}
                </div>
                """.format(dialogue['text']), unsafe_allow_html=True)
                time.sleep(0.5)

    st.markdown("---")
    st.subheader("📝 Dialogue Transcript")
    with st.expander("View Full Transcript"):
        dialogues = simulate_dialogue()
        for i, dialogue in enumerate(dialogues, 1):
            st.write("**{}. {}:** {}".format(i, dialogue['speaker'], dialogue['text']))

with tab4:
    st.header("📹 Video Resources & Summaries")
    st.write("Visual explanations and exam tips for better understanding.")

    st.subheader("🎥 Recommended Video Lectures")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-box">
        <h4>📺 Video 1: Microeconomics Fundamentals</h4>
        <p><strong>Topics Covered:</strong></p>
        <ul>
            <li>Introduction to Microeconomics</li>
            <li>Demand and Supply Basics</li>
            <li>Market Equilibrium</li>
            <li>Real-world Applications</li>
        </ul>
        <p><strong>Duration:</strong> ~30 minutes</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("🔗 [Watch Video 1](https://youtu.be/Ec19ljjvlCI)")

    with col2:
        st.markdown("""
        <div class="feature-box">
        <h4>📺 Video 2: Advanced Concepts</h4>
        <p><strong>Topics Covered:</strong></p>
        <ul>
            <li>Elasticity of Demand</li>
            <li>Consumer Behavior</li>
            <li>Production Theory</li>
            <li>Market Structures</li>
        </ul>
        <p><strong>Duration:</strong> ~25 minutes</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("🔗 [Watch Video 2](https://www.youtube.com/watch?v=Z_S0VA4jKes)")

    st.markdown("---")
    st.subheader("📊 Key Concepts Visualization")

    st.markdown("""
    ### Demand and Supply Curve

    The fundamental model of microeconomics shows:
    - **Demand Curve:** Slopes downward (inverse relationship between price and quantity)
    - **Supply Curve:** Slopes upward (direct relationship between price and quantity)
    - **Equilibrium Point:** Where the curves intersect

    ### Elasticity Spectrum

    | Type | Elasticity Value | Consumer Response |
    |------|------------------|-------------------|
    | Perfectly Inelastic | 0 | No response to price changes |
    | Inelastic | < 1 | Weak response to price changes |
    | Unit Elastic | = 1 | Proportional response |
    | Elastic | > 1 | Strong response to price changes |
    | Perfectly Elastic | ∞ | Infinite response |

    ### Market Structure Comparison

    | Feature | Perfect Competition | Monopoly | Oligopoly | Monopolistic Competition |
    |---------|-------------------|----------|-----------|--------------------------|
    | Number of Firms | Many | One | Few | Many |
    | Product Type | Homogeneous | Unique | Differentiated/Similar | Differentiated |
    | Entry Barriers | None | High | High | Low |
    | Price Control | None (Price Taker) | High (Price Maker) | Some | Some |
    """)

    st.markdown("---")
    st.subheader("🎯 Exam Tips Summary")

    st.success("""
    **Top 10 Exam Success Tips:**

    1. **Master the Graphs:** Practice drawing supply-demand diagrams until you can do them perfectly
    2. **Memorize Key Formulas:** Especially elasticity calculations
    3. **Understand, Don't Memorize:** Focus on WHY things happen, not just WHAT happens
    4. **Use Real Examples:** Connect theories to real-world scenarios (gas prices, food markets, etc.)
    5. **Practice Numerical Problems:** Work through calculation questions multiple times
    6. **Create Summary Sheets:** One-page notes for each major topic
    7. **Explain to Others:** Teaching concepts helps solidify your understanding
    8. **Time Management:** Practice past papers under timed conditions
    9. **Review Mistakes:** Learn from errors in practice questions
    10. **Stay Current:** Follow economic news to see theories in action
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📚 Interactive Study Tool | Built with Streamlit | Economics Learning Assistant</p>
    <p>💡 Tip: Use all features together for maximum learning effectiveness!</p>
</div>
""", unsafe_allow_html=True)