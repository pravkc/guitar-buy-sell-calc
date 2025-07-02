import streamlit as st

st.title("🎸 Guitar Pricing Calculator (USD → AUD)")

guitar_price_usd = st.number_input("Enter guitar purchase price (USD)", min_value=0.0, step=10.0)

# Cost Parameters
us_shipping = 55
warehouse_fee = 10
intl_shipping = 50
insurance_rate = 0.02
usd_to_aud = 1.5
gst_rate = 0.10
profit_margin = 0.40

if guitar_price_usd > 0:
    insurance = guitar_price_usd * insurance_rate
    total_cost_usd = guitar_price_usd + us_shipping + warehouse_fee + intl_shipping + insurance
    total_cost_aud = total_cost_usd * usd_to_aud
    gst = total_cost_aud * gst_rate
    landed_cost_aud = total_cost_aud + gst
    landed_cost_usd = landed_cost_aud / usd_to_aud
    sell_price_aud = landed_cost_aud * (1 + profit_margin)

    st.markdown("### 📊 Cost Breakdown:")
    st.write(f"**Purchase Price (USD):** ${guitar_price_usd:.2f}")
    st.write(f"**Total Cost (USD):** ${total_cost_usd:.2f}")
    st.write(f"**Landed Cost (USD):** ${landed_cost_usd:.2f}")
    st.write(f"**Landed Cost (AUD, incl. GST):** ${landed_cost_aud:.2f}")
    st.write(f"**Recommended Sell Price (AUD, 40% profit):** ${sell_price_aud:.2f}")
