import streamlit as st
import math
from datetime import date

# Page config
st.set_page_config(page_title="ANDICODE - Startup Calculator", layout="wide")

# --- BRANDING BANNER ---
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h1>🚀 ANDICODE - STARTUP CALCULATOR (PRO VERSION)</h1>
    <p><em>Automated Business Suite</em></p>
    <p style="font-size: 12px; color: gray;">All Rights Reserved - Private Proprietor</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# Initialize session state for trial tracking
if 'trial_count' not in st.session_state:
    st.session_state.trial_count = 0

# --- TRIAL & SECURITY SYSTEM ---
def get_unlock_code():
    today = date.today().day
    return f"ANDI{today * 3 + 7}"

st.session_state.trial_count += 1

trial_expired = st.session_state.trial_count > 3

if trial_expired:
    st.warning("⚠️ FREE TRIAL EXPIRED: 3 free uses completed.")
    st.info("To unlock this app, contact the person who shared it with you.\nAn R10 airtime voucher is required to receive today's unlock code.")
    
    unlock_code = st.text_input("Enter unlock code:")
    if unlock_code:
        if unlock_code.strip().upper() == get_unlock_code():
            st.success("✅ Success! App unlocked for 3 more uses.")
            st.session_state.trial_count = 0
        else:
            st.error("❌ Invalid code. Please contact the supplier.")
            st.stop()

# --- USER INPUTS ---
col1, col2 = st.columns(2)

with col1:
    business = st.text_input("Business name:", placeholder="Enter your business name").strip().lower()
    location = st.text_input("Town/Location:", placeholder="Enter your town/location").strip().lower()
    rent = st.number_input("Monthly rent (R):", min_value=0, step=100, value=0)
    stock = st.number_input("Initial stock cost (R):", min_value=0, step=100, value=0)

with col2:
    transport = st.number_input("Transport costs (R):", min_value=0, step=100, value=0)
    sell = st.number_input("Selling price per item (R):", min_value=0, step=10, value=0)
    buy = st.number_input("Buying cost price per item (R):", min_value=0, step=10, value=0)
    have = st.number_input("Money you currently have (R):", min_value=0, step=100, value=0)

# --- GENERATE REPORT BUTTON ---
if st.button("📊 Generate Financial Report", use_container_width=True):
    if not business or not location:
        st.error("Please enter business name and location.")
    else:
        # --- FINANCIAL LOGIC ---
        total = rent + stock + transport
        profit = sell - buy
        need = total - have
        safe = total * 2

        # --- BUSINESS PLAN REPORT ---
        st.markdown("---")
        st.markdown(f"""
        <div style="text-align: center;">
            <h2>📈 FINANCIAL REPORT</h2>
            <h3>{business.upper()} ({location.upper()})</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")

        # Metrics display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Startup Capital", f"R{total:,}")
        with col2:
            st.metric("Safe Buffer (x2)", f"R{safe:,}")
        with col3:
            st.metric("Capital You Have", f"R{have:,}")

        # Shortfall display
        if need > 0:
            st.error(f"💔 **Shortfall / Deficit: R{need:,}**")
        else:
            st.success(f"🎉 **You are fully funded! No shortfall needed.**")

        # Profit per item
        st.info(f"💰 **Net Profit per Item Sold: R{profit:,}**")

        # --- CALCULATION TARGETS & SAVINGS ---
        if profit > 0:
            items_for_rent = math.ceil(rent / profit)
            st.warning(f"🎯 **Target: You must sell {items_for_rent} items per month just to cover rent.**")
            
            if need > 0:
                st.markdown("### 💳 Recommended Savings Plan")
                savings_col1, savings_col2, savings_col3 = st.columns(3)
                with savings_col1:
                    st.metric("Over 3 Months", f"R{math.ceil(need / 3):,}/month")
                with savings_col2:
                    st.metric("Over 6 Months", f"R{math.ceil(need / 6):,}/month")
                with savings_col3:
                    st.metric("Over 12 Months", f"R{math.ceil(need / 12):,}/month")
        else:
            st.error("⚠️ **WARNING**: Your selling price is equal to or lower than your buying price!\nYou must increase your selling price to make a profit.")

        # --- LOCAL WHOLESALER INTEGRATION ---
        st.markdown("---")
        if location and ("ladysmith" in location or "emnambithi" in location):
            st.success("📍 **Local Tip**: Source your stock from Boxer Wholesale, Save, or China Mall Ladysmith.")
        else:
            st.info("📍 **Local Tip**: Explore local independent wholesalers in your municipality for bulk discounts.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 12px; color: gray;">
    <p>© ANDICODE - All Rights Reserved | Private Proprietor</p>
</div>
""", unsafe_allow_html=True)
