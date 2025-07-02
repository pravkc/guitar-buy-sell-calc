import streamlit as st

st.set_page_config(page_title="Guitar Pricing Calculator", page_icon="🎸")
st.title("🎸 Guitar Pricing Calculator (USD → AUD)")

guitar_price_usd = st.number_input("Enter guitar purchase price (USD)", min_value=0.0, step=10.0)

# Fixed cost parameters
us_shipping = 55
warehouse_fee = 10
intl_shipping = 50
insurance_rate = 0.02
usd_to_aud = 1.5
gst_rate = 0.10

if guitar_price_usd > 0:
    # Cost calculations
    insurance = guitar_price_usd * insurance_rate
    total_cost_usd = guitar_price_usd + us_shipping + warehouse_fee + intl_shipping + insurance
    total_cost_aud = total_cost_usd * usd_to_aud
    gst = total_cost_aud * gst_rate
    landed_cost_aud = total_cost_aud + gst
    landed_cost_usd = landed_cost_aud / usd_to_aud

    st.markdown("## 🧾 Cost Breakdown (USD)")
    st.write(f"• **Guitar price:** ${guitar_price_usd:.2f}")
    st.write(f"• **US domestic shipping:** ${us_shipping:.2f}")
    st.write(f"• **Warehouse/repacking fee:** ${warehouse_fee:.2f}")
    st.write(f"• **International shipping:** ${intl_shipping:.2f}")
    st.write(f"• **Insurance (2%):** ${insurance:.2f}")
    st.write(f"**→ Total before conversion:** ${total_cost_usd:.2f}")

    st.markdown("## 💱 Currency Conversion")
    st.write(f"• **USD to AUD rate:** {usd_to_aud}")
    st.write(f"• **Converted cost (AUD):** ${total_cost_aud:.2f}")

    st.markdown("## 🛃 Import Cost (Australia)")
    st.write(f"• **GST (10%):** ${gst:.2f}")
    st.write(f"**→ Landed cost in AUD (incl. GST):** ${landed_cost_aud:.2f}")
    st.write(f"• **Landed cost in USD (for reference):** ${landed_cost_usd:.2f}")

    st.markdown("## 💰 Recommended Sale Prices + Profits")

    st.write("### Profit Scenarios (AUD)")
    st.markdown("| Margin | Sale Price (AUD) | Profit (AUD) |")
    st.markdown("|--------|------------------|---------------|")

    for margin in [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]:
        sell_price = landed_cost_aud * (1 + margin)
        profit = sell_price - landed_cost_aud
        st.markdown(f"| {int(margin*100)}% | ${sell_price:.2f} | ${profit:.2f} |")