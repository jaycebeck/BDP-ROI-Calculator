import streamlit as st


commission_rate = 0.025

st.set_page_config(page_title="ROI Calculator", page_icon=":chart_with_upwards_trend:")


# Streamlit app
def calculator():
    # App title
    st.title("BulkDelivery PRO ROI Calculator")

    st.markdown("## Same version as presented Thursday 4/18/2024")

    avg_time_to_take_order = st.slider(
        "Average time to take an order (minutes):",
        min_value=0,
        value=5,
        max_value=20,
        step=1,
    )

    avg_worker_wage = st.slider(
        "Hourly wage of someone that takes orders:",
        min_value=7.25,
        value=16.25,
        max_value=30.0,
        step=0.25,
    )

    avg_sale_price = st.slider(
        "Average sale price:",
        min_value=0,
        value=500,
        max_value=1000,
        step=10,
    )

    avg_time_organize_delivery = st.slider(
        "Average time to organize delivery (minutes):",
        min_value=0,
        value=10,
        max_value=30,
        step=1,
    )
    # Calculate ROI
    if st.button("Calculate ROI"):

        commission_rate = 0.025

        cost_cust = (
            (avg_time_organize_delivery + avg_time_to_take_order) * avg_worker_wage / 60
        )

        cust_sales = avg_sale_price - cost_cust

        cost_bdp = avg_sale_price * commission_rate

        bdp_sales = avg_sale_price - cost_bdp

        gain = cost_cust - cost_bdp

        roi = ((bdp_sales - cust_sales) / cust_sales) * 100

        st.write(f"Cost of Phone ordering per order made: ${cost_cust:.2f}")
        st.write(f"Cost of BDP online ordering per order made: ${cost_bdp:.2f}")
        st.write(f"Phone Ordering Revenue on single order: ${cust_sales:.2f}")
        st.write(f"BDP Revenue on single order: ${bdp_sales:.2f}")
        st.write(f"ROI: {roi:.2f}%")


# Run the app
if __name__ == "__main__":
    calculator()
