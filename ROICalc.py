import streamlit as st


commission_rate = 0.025


# Streamlit app
def main():
    # App title
    st.title("BulkDelivery PRO ROI Calculator")

    st.markdown("#### How are the costs of BulkDelivery PRO calculated?")

    st.latex(r""" \text{Commission Rate} = 2.5\% """)
    st.latex(
        r"""
        \text{Cost of BulkDelivery PRO} = \text{Average Sale Price} \times \text{Commission Rate}
        """
    )

    st.latex(
        r""" \text{Cost of Phone Orders} = (\text{Time to Take Order} + \text{Time to Relay Order to Driver}) \times \text{Average Wage} """
    )

    st.markdown("#### How is the ROI calculated?")
    st.latex(
        r"""
        \text{ROI} = \frac{\text{Revenue BDP Order} - \text{Revenue Phone Order}}{\text{Revenue Phone Order}} \times 100
        """
    )

    st.markdown("## ROI Calculation:")

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

    st.markdown("## Conversion Rate Calculation:")

    num_of_calls = st.slider(
        "Number of calls per day:",
        min_value=0,
        value=10,
        max_value=50,
        step=1,
    )
    phone_conversion_rate = (
        st.number_input(
            "Phone conversion rate from looking to buying  (%)", value=2.0, step=0.1
        )
        / 100
    )
    avg_order_value = st.slider(
        "Average order value:", min_value=0, value=500, max_value=1000, step=10
    )

    bdp_conversion_rate = (
        st.number_input(
            "BDP conversion rate from looking to buying (%)", value=4.0, step=0.1
        )
        / 100
    )

    increase_in_order_value = st.slider(
        "Increase in order value(add value to accommodate commission):",
        min_value=0,
        value=50,
        max_value=100,
        step=1,
    )

    if st.button("Calculate Conversion Revenue"):
        phone_orders = num_of_calls * phone_conversion_rate
        bdp_orders = num_of_calls * bdp_conversion_rate
        phone_sales = phone_orders * avg_order_value
        bdp_sales = bdp_orders * (avg_order_value + increase_in_order_value)
        conversion_revenue = bdp_sales - phone_sales
        st.write(f"Phone Orders: {phone_orders:.2f}")
        st.write(f"BDP Orders: {bdp_orders:.2f}")
        st.write(f"Phone Sales: ${phone_sales:.2f}")
        st.write(f"BDP Sales: ${bdp_sales:.2f}")
        st.write(f"Increase in Sales: ${conversion_revenue:.2f}")


# Run the app
if __name__ == "__main__":
    main()
