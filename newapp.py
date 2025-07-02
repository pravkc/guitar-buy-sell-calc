import streamlit as st

st.set_page_config(page_title="Pedal & Gear Flip Calculator", page_icon="🎛️")
st.title("🎛️ Pedal & Recording Gear Flip Calculator (USD → AUD)")

pedal_price_usd = st.number_input("Enter gear purchase price (USD)", min_value=0.0, step=5.0)

# Typical pedal shipping & cost structure
us_shipping = 15             # From seller to US warehouse
warehouse_fee = 5            # Warehouse repackaging
intl_shipping = 25           # To Australia
insurance_rate = 0.01        # 1% insurance for small gear
usd_to_aud = 1.5             # Exchange rate
gst_rate = 0.10              # Import GST (AU)

if pedal_price_usd > 0:
    insurance = pedal_price_usd * insurance_rate
    total_cost_usd = pedal_price_usd + us_shipping + warehouse_fee + intl_shipping + insurance
    total_cost_aud = total_cost_usd * usd_to_aud
    gst = total_cost_aud * gst_rate
    landed_cost_aud = total_cost_aud + gst
    landed_cost_usd = landed_cost_aud / usd_to_aud

    st.markdown("## 🧾 Cost Breakdown (USD)")
    st.write(f"• **Gear price:** ${pedal_price_usd:.2f}")
    st.write(f"• **US shipping to warehouse:** ${us_shipping:.2f}")
    st.write(f"• **Warehouse fee:** ${warehouse_fee:.2f}")
    st.write(f"• **International shipping:** ${intl_shipping:.2f}")
    st.write(f"• **Insurance (1%):** ${insurance:.2f}")
    st.write(f"**→ Total before conversion:** ${total_cost_usd:.2f}")

    st.markdown("## 💱 Conversion & Tax")
    st.write(f"• **Exchange rate (USD → AUD):** {usd_to_aud}")
    st.write(f"• **Converted cost (AUD):** ${total_cost_aud:.2f}")
    st.write(f"• **GST (10%):** ${gst:.2f}")
    st.write(f"**→ Landed cost (AUD, incl. GST):** ${landed_cost_aud:.2f}")
    st.write(f"• **Landed cost in USD (for reference):** ${landed_cost_usd:.2f}")

    st.markdown("## 💰 Suggested Selling Prices & Profit")
    st.markdown("| Margin | Sale Price (AUD) | Profit (AUD) |")
    st.markdown("|--------|------------------|---------------|")
    for margin in [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]:
        sell_price = landed_cost_aud * (1 + margin)
        profit = sell_price - landed_cost_aud
        st.markdown(f"| {int(margin*100)}% | ${sell_price:.2f} | ${profit:.2f} |")