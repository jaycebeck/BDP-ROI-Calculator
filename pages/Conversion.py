import streamlit as st


def conversion():
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

    if st.button("Calculate Conversion Revenue(Test)"):
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


if __name__ == "__main__":
    conversion()
