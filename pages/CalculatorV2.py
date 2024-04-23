import streamlit as st
import numpy as np


st.set_page_config(page_title="ROI Calculator", page_icon=":chart_with_upwards_trend:")


def calculatorV2():
    st.title("BulkDelivery PRO ROI Calculator V2")

    st.markdown("## Updated version of the ROI Calculator")
    st.markdown("### Revised after meeting on 4/18/2024")
    st.markdown("This current version includes:")
    st.markdown("- the number of orders in a day that can be taken by phone ordering.")
    st.markdown("- the increase of sales due to the online ordering system.")
    st.markdown("- both daily and monthly values.")

    avg_sale_price = st.slider(
        "Average sale price:",
        min_value=0,
        value=500,
        max_value=1000,
        step=10,
    )

    avg_num_orders = st.slider(
        "Average number of orders per day:",
        min_value=0,
        value=3,
        max_value=20,
        step=1,
    )

    avg_time_to_take_order = st.slider(
        "Average time to take an order (minutes):",
        min_value=0,
        value=5,
        max_value=20,
        step=1,
    )

    avg_time_organize_delivery = st.slider(
        "Average time to organize delivery with driver (minutes):",
        min_value=0,
        value=10,
        max_value=30,
        step=1,
    )

    people_taking_orders = st.slider(
        "Number of people taking orders:",
        min_value=1,
        value=2,
        max_value=5,
        step=1,
    )

    avg_worker_wage = st.slider(
        "Hourly wage of someone that takes orders:",
        min_value=7.25,
        value=16.25,
        max_value=30.0,
        step=0.25,
    )

    bdp_order_rate = st.number_input(
        "Increase in sales due to online ordering system (%)*:",
        min_value=0,
        value=20,
        step=10,
    )

    st.write(
        "*This value should be based on BDP's historical data and should not be an input from the user."
    )

    # Calculate ROI
    if st.button("Calculate ROI"):

        commission_rate = 0.025

        cost_cust = (
            people_taking_orders
            * (
                (avg_time_organize_delivery + avg_time_to_take_order)
                * avg_worker_wage
                / 60
            )
            / avg_num_orders
        )

        cust_sales = (avg_sale_price * avg_num_orders) - cost_cust

        bdp_orders = int(np.round(avg_num_orders * (1 + bdp_order_rate / 100)))

        cost_bdp = (avg_sale_price * bdp_orders) * commission_rate

        bdp_sales = (avg_sale_price * bdp_orders) - cost_bdp

        roi = ((bdp_sales - cust_sales) / cust_sales) * 100

        st.markdown("### Daily Values")
        st.write(f"Cost of Phone ordering per order made: ${cost_cust:.2f}")
        st.write(f"Cost of BDP online ordering per order made: ${cost_bdp:.2f}")
        st.write(
            f"Phone Ordering Revenue on {avg_num_orders} orders: ${cust_sales:.2f}"
        )
        st.write(
            f"BDP Online Ordering Revenue on {bdp_orders} orders: ${bdp_sales:.2f}"
        )

        st.markdown(f"#### Daily ROI: {roi:.2f}%")

        st.markdown("### Monthly Values")
        st.markdown(
            "*Assuming an average of 21 working days in a month and an average 30 days for BDP online ordering because orders can be take at any time.*"
        )

        monthly_cust_cost = cost_cust * 21
        monthly_bdp_cost = cost_bdp * 30

        avg_monthly_orders = avg_num_orders * 21
        avg_monthly_orders_bdp = bdp_orders * 30

        monthly_cust_sales = cust_sales * 22
        monthly_bdp_sales = bdp_sales * 30

        monthly_roi = (
            (monthly_bdp_sales - monthly_cust_sales) / monthly_cust_sales
        ) * 100

        st.write(f"Cost of Phone ordering per order made: ${monthly_cust_cost:.2f}")
        st.write(f"Cost of BDP online ordering per order made: ${monthly_bdp_cost:.2f}")
        st.write(
            f"Phone Ordering Revenue on {avg_monthly_orders} orders: ${monthly_cust_sales:.2f}"
        )
        st.write(
            f"BDP Online Ordering Revenue on {avg_monthly_orders_bdp} orders: ${monthly_bdp_sales:.2f}"
        )

        st.markdown(f"#### Monthly ROI: {monthly_roi:.2f}%")


if __name__ == "__main__":
    calculatorV2()
