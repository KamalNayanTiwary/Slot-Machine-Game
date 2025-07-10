import streamlit as st
import random

# --- Slot Machine Symbols ---
symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉']

# --- Session State Initialization ---
if 'balance' not in st.session_state:
    st.session_state.balance = 100  # Default starting balance
if 'reels' not in st.session_state:
    st.session_state.reels = ['❓', '❓', '❓']
if 'message' not in st.session_state:
    st.session_state.message = ''

# --- Header ---
st.title("🎰 Slot Machine Game")
st.write(f"💵 **Current Balance:** ${st.session_state.balance}")

# --- Bet Input ---
bet = st.number_input("Enter your bet amount ($)", min_value=1, max_value=st.session_state.balance, step=1)

# --- Play Button ---
if st.button("🎲 Spin"):
    if bet > st.session_state.balance:
        st.warning("You don't have enough balance to place this bet.")
    else:
        # Spin reels
        st.session_state.reels = [random.choice(symbols) for _ in range(3)]

        # Calculate payout
        r = st.session_state.reels
        if r[0] == r[1] == r[2]:
            payout = bet * 10
            st.session_state.message = f"🎉 Jackpot! You won ${payout}"
        elif r[0] == r[1] or r[0] == r[2] or r[1] == r[2]:
            payout = bet * 2
            st.session_state.message = f"✅ You won ${payout}"
        else:
            payout = 0
            st.session_state.message = "❌ You lost!"

        # Update balance
        st.session_state.balance += payout - bet

# --- Display Reels ---
st.markdown("### 🎰 Result")
reel_display = f"<h1 style='text-align: center;'>{' | '.join(st.session_state.reels)}</h1>"
st.markdown(reel_display, unsafe_allow_html=True)

# --- Message and Balance ---
if st.session_state.message:
    st.success(st.session_state.message if "won" in st.session_state.message else st.session_state.message)

# --- Game Over ---
if st.session_state.balance <= 0:
    st.error("💀 You are out of money! Game Over.")
    if st.button("🔄 Restart"):
        st.session_state.balance = 100
        st.session_state.reels = ['❓', '❓', '❓']
        st.session_state.message = ''
